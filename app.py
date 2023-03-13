from dash import dash, html


app = dash.Dash(__name__)

app.layout = html.Div('Drag Race Dashboard!')

if __name__ == '__main__':
    app.run_server(debug=True)