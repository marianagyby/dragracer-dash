# imports
import pandas as pd
import altair as alt
import dash_bootstrap_components as dbc
from dash import dash, html, dcc, Input, Output

# read in data
drag = pd.read_csv('../data/drag.csv')

# Function to extract astrology signs
def get_astrology_sign(dob):
    day = dob.day
    month = dob.month

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    else:
        return "Invalid date"


# Start of app code
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server


# Style arguments for sidebar
SIDEBAR_STYLE = {
    # "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa"
}

# Style for the main content
CONTENT_STYLE = {
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem" 
}

# App Title
title = html.Div(
    [
        html.H2("Drag Race Dashboard", className="display-4"),
        html.Hr(),
        dbc.Label("Explore the ages and astrological signs of Queens from RuPaul's Drag Race!",
                  style={"font-size": "22px"})
    ],
    style={'padding': '2rem 1rem'}
)

# App Sidebar
sidebar = html.Div(
    [                          
        html.P("Filters", className="lead"),
        html.Hr(), 
        dbc.Label("Season"),
        dcc.Dropdown(
            id='season',            
            options=[{'label': season, 'value': season} for season in sorted(drag['season'].unique())],
            multi=True,
            placeholder='Select Season',
            style={'width': '100%'}
        ),
        html.Br(),
        dbc.Label("Age"),
        dcc.RangeSlider(
            id='age',
            min=drag['age'].min(),
            max=drag['age'].max(),
            step=1,
            value=[drag['age'].min(), drag['age'].max()],
            tooltip={"placement": "bottom", "always_visible": False},
            marks={
                20: {'label': '20'},
                25: {'label': '25'},
                30: {'label': '30'},
                35: {'label': '35'},
                40: {'label': '40'},
                45: {'label': '45'},
                50: {'label': '50'}            
            }
        )
    ],
    style=SIDEBAR_STYLE,
)

# App main panel 
content = html.Div([
    html.H4("Age Distribution"),
    html.Iframe(id='plot1', style={'width': '70%', "height": "400px"}),
    html.Br(),
    html.H4("Astrological Signs"),
    html.Iframe(id='plot2', style={'width': '70%', "height": "350px"}),
], style=CONTENT_STYLE)

# App layout
app.layout = html.Div([title,
                       dbc.Row([dbc.Col([sidebar], md=3),
                                dbc.Col([content], md=9)
                                ])
                    ])

# Update content based on user inputs
@app.callback(
    [Output('plot1', 'srcDoc'), Output('plot2', 'srcDoc')],
    [Input('season', 'value'), Input('age', 'value')]
)
def update_plots(seasons, age_range):
    # Filter data based on selected seasons
    if seasons:
        filtered_drag = drag[drag['season'].isin(seasons)]
    else:
        filtered_drag = drag

    # Filter data based on selected age range
    filtered_drag = filtered_drag[(filtered_drag['age'] >= age_range[0]) & (filtered_drag['age'] <= age_range[1])]

    # Plot 1: Age distribution
    df1 = filtered_drag.drop_duplicates(subset=['contestant'])
    plot1 = alt.Chart(df1).mark_bar(color="#b19cd9").encode(
        alt.X('age', bin=alt.Bin(maxbins=30), title="Age"),
        alt.Y('count()', title="Count")
    ).to_html()

    # Plot 2: Astrology sign distribution
    ## Convert the 'dob' column to datetime format
    df2 = filtered_drag.drop_duplicates(subset=['contestant']).dropna(subset=['dob'])
    df2['dob'] = pd.to_datetime(df2['dob'])

    ## Create the 'astrology_sign' column using 'get_astrology_sign' function
    df2['astrology_sign'] = df2['dob'].apply(get_astrology_sign)
    df2 = df2.dropna(subset=['astrology_sign'])

    # count by astrology sign
    astro_counts = df2.groupby('astrology_sign').agg({'contestant': 'nunique'}).reset_index()
    astro_counts = astro_counts.rename(columns={'contestant': 'count'})

    contestant_names = df2[['astrology_sign', 'contestant']].groupby('astrology_sign')['contestant'].apply(list).reset_index()
    contestant_names['contestant_names'] = contestant_names['contestant'].apply(lambda x: ', '.join(x))
    astro_counts_names = astro_counts.merge(contestant_names[['astrology_sign', 'contestant_names', 'contestant']], on='astrology_sign')

    plot2 = alt.Chart(astro_counts_names).mark_bar(color="#b19cd9").encode(
        alt.Y('astrology_sign', sort='-x', title="Sign"),
        alt.X('count', title="Count"),
        alt.Color("contestant", title="Queens", scale=alt.Scale(scheme='set3')),
        tooltip="contestant_names"
    ).to_html()

    # Return the plots
    return plot1, plot2


if __name__ == '__main__':
    app.run_server(debug=True)