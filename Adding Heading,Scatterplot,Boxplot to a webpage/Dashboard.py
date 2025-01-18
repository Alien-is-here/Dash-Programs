import pandas as pd
import plotly.graph_objs as go
import dash
import dash_html_components as html
import dash_core_components as dcc

# Assuming "gapminder.csv" is in the working directory
data = pd.read_csv("gapminder.csv")

print(data.head())
app = dash.Dash()

app.layout = html.Div(
    children=[
        # Header Div
        html.Div(
            children=[
                html.H1(
                    "MY FIRST DASHBOARD",
                    style={
                        'color': 'red',
                        'text-align': 'center',
                        'font-size': '24px',
                        'margin': '0',
                        'line-height': '50px'  # Center text vertically
                    }
                )
            ],
            style={
                'border': '1px black solid',
                'width': '100%',
                'height': '50px',
                'box-sizing': 'border-box'  # Prevent overflow
            }
        ),
        # Scatter Plot Div
        html.Div(
            children=[
                dcc.Graph(
                    id='scatterplot',
                    figure={
                        'data': [
                            go.Scatter(
                                x=data['pop'],
                                y=data['gdpPercap'],
                                mode='markers'
                            )
                        ],
                        'layout': go.Layout(title='Scatter Plot')
                    }
                )
            ],
            style={
                'border': '1px black solid',
                'float': 'left',
                'width': '49.7%',
                'height': '350px'
            }
        ),
        # Empty Div
        html.Div(
            children=[
                dcc.Graph(
                    id='box-plot',
                    figure={
                        'data': [
                            go.Box(
                                x=data['pop'],

                            )
                        ],
                        'layout': go.Layout(title='BoxPlot')
                    }
                )
            ], style={
                'border': '1px black solid',
                'float': 'left',
                'width': '49.7%',
                'height': '350px'
            }
        )])

if __name__ == '__main__':
    app.run_server()
