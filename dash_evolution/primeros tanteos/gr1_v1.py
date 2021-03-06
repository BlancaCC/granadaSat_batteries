# -*- coding: utf-8 -*-
# First graphic
# Author Blanca Cano
# fuente de inspiración:
# https://github.com/plotly/dash-core-components/pull/74

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

#open data file
df = pd.read_csv('df.csv' , header=None)


app = dash.Dash()

colors = {
    'background': '#f9f9f9',
    'text': '#1e1807'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Batteries charge',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dict(
        title='yaxis title'
    ),

    html.Div(children='Current in time', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    # Current and voltage same graphic
    dcc.Graph(
        id='example-graph-2',
        figure={ 
            'data': [
                { 'x': df[2] ,'y': df[0], 'type':'scatter' , 'name':'Current' } #current
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
