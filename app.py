# imports
import pandas as pd
import altair as alt
import dash_bootstrap_components as dbc
from dash import dash, html, dcc, Input, Output

# read in data
drag = pd.read_csv('data/drag.csv')


app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP])


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    # "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

title = html.Div(
    [
        html.H1("Drag Racer Dashboard", className="display-4"),
        html.Hr(),
    ],
    style={'padding': '2rem 1rem'}
)

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


content = html.Div(style=CONTENT_STYLE)

app.layout = html.Div([title, sidebar, content])

if __name__ == '__main__':
    app.run_server(debug=True)