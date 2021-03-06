# Basic dash library
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
# import csv
import pandas as pd

# plot dessing
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools

#typography
from loremipsum import get_sentences




#open data file, columns' mean  votage,current,time,capacity
 
df = pd.read_csv('df.csv' , header=None)

# Get values grahp
voltage = go.Scatter(
    y = df[0],
    x = df [2],
    name = 'voltage'
)
current = go.Scatter(
    y = df[1],
    x = df [2],
    name = 'current'
)

capacity = go.Scatter(
    y=df [3],
    x=df [2],
    name = 'capacity'
 )

fig_voltage = tools.make_subplots()
fig_voltage.append_trace( voltage , 1 ,1)
fig_voltage['layout'].update(height=600, width=600, title='voltage')

fig_current = tools.make_subplots()
fig_current.append_trace( current , 1 ,1)
fig_current['layout'].update(height=600, width=600, title='current')

fig_capacity = tools.make_subplots()
fig_capacity.append_trace( capacity , 1 ,1)
fig_capacity['layout'].update(height=600, width=600, title='capacity')

fig = [ fig_voltage , fig_current , fig_capacity ]

# Tests representes
# T1	High Vacuum test
# T2	Capacity and Internal Resistance vs Temperature
# T3	Self-Discharge Test
# T4	LEO Cycling
# T5	EMF vs SOC
# T6	Reduced pressure 30 % DOD Cycling
# T7	Reduced pressure 80% DOD Cycling

#Start graph
app = dash.Dash()
app.layout = html.Div([
    html.H1('Results'),
    # Select test
    html.Label('Test selection:'),
    dcc.Tabs(
        id = 'tabs',
        tabs=[
            {'label': 'Voltage' , 'value' : 0},
            {'label': 'Current' , 'value' : 1},
            {'label': 'Capacity' , 'value' : 2},
            {'label': 'LEO Cycling', 'value':  4},
            {'label': 'LEO Cycling', 'value':  5},
            {'label': 'Reduced pressure 30 % DOD Cycling', 'value':  6},
            {'label': 'Reduced pressure 80% DOD Cycling', 'value':  7}
            
        ]
        #,        vertical=True
    ),
    dcc.Graph(
        id = 'Graph'
        )
   # html.Div( id = 'cache' , style={'display':'none'})
]
, style={
        'width': '80%',
        'fontFamily': 'Sans-Serif',
        'margin-left': 'auto',
        'margin-right': 'auto'
    })

@app.callback(Output('Graph', 'figure'), [Input('tabs', 'value')])
def update_graph(value):
    return fig[value % 3]


if __name__ == '__main__':
    app.run_server(debug=True)
