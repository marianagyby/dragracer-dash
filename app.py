# imports
import pandas as pd
import altair as alt
from dash import dash, html

# read in data
drag = pd.read_csv('data/drag.csv')


app = dash.Dash(__name__)

app.layout = html.Div('Drag Race Dashboard!')

if __name__ == '__main__':
    app.run_server(debug=True)