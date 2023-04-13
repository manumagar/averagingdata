import pandas as pd
import plotly.graph_objs as go
import dash
from dash import dcc 
from dash import html 

data = pd.read_csv("data.csv")

app = dash.Dash(__name__)

# to create a dictionary for the dropdown options
dropdown_options = [{'label': 'Temperature', 'value': 'temp'}, {'label': 'Humidity', 'value': 'humi'}]

# calculate the average, minimum, and maximum values of temperature and humidity
temp_avg = round(data['temp'].mean(), 2)
temp_min = round(data['temp'].min(), 2)
temp_max = round(data['temp'].max(), 2)
humi_avg = round(data['humi'].mean(),2)
humi_min = round(data['humi'].min(), 2)
humi_max = round(data['humi'].max(), 2)

app.layout = html.Div(children=[
    html.H1(children='Temperature and Humidity Dashboard'),
    
    html.Div(children=[
        dcc.Graph(
            id='temperature-gauge',
            figure={
                'data':[
                    go.Indicator(
                        mode='gauge+number',
                        value=data['temp'].iloc[-1],
                        title={'text':'Temperature'},
                        domain={'x':[0,1],'y':[0,1]}
                    )
                ],
                'layout':{
                    'width':300,
                    'height':300,
                    'margin':{'t':0,'b':0,'l':0,'r':0}
                }
            }
        ),
        dcc.Graph(
            id='humidity-gauge',
            figure={
                'data':[
                    go.Indicator(
                        mode='gauge+number',
                        value=data['humi'].iloc[-1],
                        title={'text':'Humidity'},
                        domain={'x':[0,1],'y':[0,1]}
                    )
                ],
                'layout':{
                    'width':300,
                    'height':300,
                    'margin':{'t':0,'b':0,'l':0,'r':0}
                }
            }
        ),
        dcc.Graph(
            id='temp-stats',
            figure={
                'data': [
                    go.Indicator(
                        mode='number',
                        value=temp_avg,
                        title={'text': 'Average Temperature'},
                        number={'suffix': '°C'}
                    ),
                    go.Indicator(
                        mode='number',
                        value=temp_min,
                        title={'text': 'Minimum Temperature'},
                        number={'suffix': '°C'}
                    ),
                    go.Indicator(
                        mode='number',
                        value=temp_max,
                        title={'text': 'Maximum Temperature'},
                        number={'suffix': '°C'}
                    )
                ],
                'layout':{
                    'width':300,
                    'height':100,
                    'margin':{'t':0,'b':0,'l':0,'r':0}
                }
            }
        ),
        dcc.Graph(
            id='humi-stats',
            figure={
                'data': [
                    go.Indicator(
                        mode='number',
                        value=humi_avg,
                        title={'text': 'Average Humidity'},
                        number={'suffix': '%'}
                    ),
                    go.Indicator(
                        mode='number',
                        value=humi_min,
                        title={'text': 'Minimum Humidity'},
                        number={'suffix': '%'}
                    ),
                                    
                    go.Indicator(
                        mode='number',
                        value=humi_max,
                        title={'text': 'Maximum Humidity'},
                        number={'suffix': '%'}
                    )
                ],
                'layout':{
                    'width':300,
                    'height':100,
                    'margin':{'t':0,'b':0,'l':0,'r':0}
                }
            }
        ),
    ])
], style={'display': 'flex'}),

html.Div(children=[    html.Label('Select a parameter to display:'),    dcc.Dropdown(        id='parameter-dropdown',        options=dropdown_options,        value='temp'    ),    dcc.Graph(id='parameter-graph')])
@app.callback(
    dash.dependencies.Output('parameter-graph', 'figure'),
    [dash.dependencies.Input('parameter-dropdown', 'value')]
)
def update_graph(selected_value):
    if selected_value == 'temp':
        y_data = data['temp']
        y_label = 'Temperature (°C)'
    else:
        y_data = data['humi']
        y_label = 'Humidity (%)'
    return {
        'data': [go.Scatter(x=data.index, y=y_data)],
        'layout': go.Layout(
            title=f'{y_label} over time',
            xaxis={'title': 'Time'},
            yaxis={'title': y_label},
            height=500,
            margin={'l': 40, 'b': 40, 't': 40, 'r': 40},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)
