# to create the dropdown and the combined temperature and humidity import pandas as pd
import plotly.graph_objs as go
import dash
from dash import dcc 
from dash import html 

data = pd.read_csv("data.csv")

app = dash.Dash(__name__)

# to create a dictionary for the dropdown options
# dropdown_options = [{'label': 'Temperature', 'value': 'temp'}, {'label': 'Humidity', 'value': 'humi'}]
dropdown_options = [    {'label': 'Temperature', 'value': 'temp'},    {'label': 'Humidity', 'value': 'humi'},    {'label': 'Temperature Average', 'value': 'temp_avg'},    {'label': 'Humidity Average', 'value': 'humi_avg'},    {'label': 'Temperature Maximum', 'value': 'temp_max'},    {'label': 'Humidity Maximum', 'value': 'humi_max'},    {'label': 'Temperature Minimum', 'value': 'temp_min'},    {'label': 'Humidity Minimum', 'value': 'humi_min'}]


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
        )
    ], style={'display':'flex','flex-wrap':'wrap','justify-content':'center'}),

    # to create the dropdown and the combined temperature and humidity graph
    html.Div([
        dcc.Dropdown(
            id='dropdown',
            options=dropdown_options,
            value='temp' # it is to set the default option to temperature
        ),
        dcc.Graph(
            id='temperature-humidity-graph',
            figure={
                'data': [
                    go.Scatter(
                        x=data['time'],
                        y=data['temp'],
                        mode='lines',
                        name='Temperature'
                    ),
                    go.Scatter(
                        x=data['time'],
                        y=data['humi'],
                        mode='lines',
                        name='Humidity'
                    )
                ],
                'layout': go.Layout(
                    title='Temperature and Humidity',
                    xaxis={'title': 'time'},
                    yaxis={'title': 'temp/humi'}
                )
            }
        )
    ], style={'width': '80%', 'display': 'inline-block', 'padding': '10px'})
])

# it is to add a callback function to update the graph based on the dropdown value

@app.callback(
    dash.dependencies.Output('temperature-humidity-graph', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')])
def update_graph(selected_value):
    if selected_value == 'temp':
        y_value = 'temp'
        y_title = 'Temperature'
    elif selected_value == 'humi':
        y_value = 'humi'
        y_title = 'Humidity'
    elif selected_value == 'temp_avg':
        y_value = 'temp_avg'
        y_title = 'Temperature Average'
    elif selected_value == 'humi_avg':
        y_value = 'humi_avg'
        y_title = 'Humidity Average'
    elif selected_value == 'temp_max':
        y_value = 'temp_max'
        y_title = 'Temperature Maximum'
    elif selected_value == 'humi_max':
        y_value = 'humi_max'
        y_title = 'Humidity Maximum'
    elif selected_value == 'temp_min':
        y_value = 'temp_min'
        y_title = 'Temperature Minimum'
    elif selected_value == 'humi_min':
        y_value = 'humi_min'
        y_title = 'Humidity Minimum'
    return {
        'data': [
            go.Indicator(
                mode='gauge+number',
                value=data[y_value],
                title={'text': y_title},
                gauge={
                    'axis': {'range': [None, None]},
                    'bar': {'color': '#2F4F4F'},
                    'steps': [
                        {'range': [0, 25], 'color': '#6495ED'},
                        {'range': [25, 50], 'color': '#4169E1'},
                        {'range': [50, 75], 'color': '#1E90FF'},
                        {'range': [75, 100], 'color': '#000080'}
                    ],
                    'threshold': {
                        'line': {'color': 'red', 'width': 4},
                        'thickness': 0.75,
                        'value': threshold_value
                    }
                }
            )
        ],
        'layout': go.Layout(
            title='{} Gauge'.format(y_title)
        )
    }

def update_graph(selected_value):
    if selected_value == 'temp':
        y_value = 'temp'
        y_title = 'Temperature'
    else:
        y_value = 'humi'
        y_title = 'Humidity'
    return {
        'data': [
            go.Scatter(
                x=data['time'],
                y=data[y_value],
                mode='lines',
                name=y_title
            )
        ],
        'layout': go.Layout(
            title='Temperature and Humidity',
            xaxis={'title': 'time'},
            yaxis={'title': y_title}
        )
    }
    
   

if __name__ == '__main__':
    app.run_server(debug=True)



