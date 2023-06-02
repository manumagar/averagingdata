import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html
from datetime import datetime
from dash.dependencies import Input, Output

# Set up Google Sheets API credentials
scope = ['https://www.googleapis.com/auth/spreadsheets']
credentials = Credentials.from_service_account_file('kiasprojects-df5217bf8506.json', scopes=scope)
client = gspread.authorize(credentials)

# Open the spreadsheet
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1roauEENHs2gMrKcAAWqz9GLBDvRUoN9m9b1hVkkUaQc/edit?usp=sharing'
spreadsheet = client.open_by_url(spreadsheet_url)

# Select the worksheet
worksheet = spreadsheet.sheet1

# Get all values from the worksheet
data = worksheet.get_all_values()

# Extract headers from the first row of data
headers = data[0]

# Create a DataFrame with the remaining rows of data and the extracted headers
df = pd.DataFrame(data[1:], columns=headers)

app = dash.Dash(__name__)

# Calculate the average, minimum, and maximum temperature and humidity using Pandas
avg_temp = df["Temp"].astype(float).mean()
min_temp = df["Temp"].astype(float).min()
max_temp = df["Temp"].astype(float).max()
avg_humidity = df["Humi"].astype(float).mean()
min_humidity = df["Humi"].astype(float).min()
max_humidity = df["Humi"].astype(float).max()

# Create a dictionary for the dropdown options
dropdown_options = [{'label': 'Temperature', 'value': 'temp'}, {'label': 'Humidity', 'value': 'humi'}]

app.layout = html.Div(children=[
    html.H1(children='Temperature and Humidity Dashboard'),

    html.Div(children=[
        dcc.Graph(
            id='temperature-gauge',
            figure={
                'data': [
                    go.Indicator(
                        mode='gauge+number',
                        value=df['Temp'].astype(float).iloc[-1],
                        title={'text': 'Temperature'},
                        domain={'x': [0, 1], 'y': [0, 1]}
                    )
                ],
                'layout': {
                    'width': 300,
                    'height': 300,
                    'margin': {'t': 0, 'b': 0, 'l': 0, 'r': 0}
                }
            }
        ),
        dcc.Graph(
            id='humidity-gauge',
            figure={
                'data': [
                    go.Indicator(
                        mode='gauge+number',
                        value=df['Humi'].astype(float).iloc[-1],
                        title={'text': 'Humidity'},
                        domain={'x': [0, 1], 'y': [0, 1]}
                    )
                ],
                'layout': {
                    'width': 300,
                    'height': 300,
                    'margin': {'t': 0, 'b': 0, 'l': 0, 'r': 0}
                }
            }
        )
    ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center'}),

    html.Div([
        dcc.Dropdown(
            id='dropdown',
            options=dropdown_options,
            value='temp'  # Set the default option to temperature
        ),
        dcc.DatePickerSingle(
            id='date-picker',
                        min_date_allowed=datetime(2021, 1, 1),  # Set the minimum allowed date
            max_date_allowed=datetime.today(),  # Set the maximum allowed date to today
            initial_visible_month=datetime.today(),  # Set the initial visible month to today
            date=datetime.today()  # Set the initial selected date to today
        ),
        dcc.Graph(
            id='temperature-humidity-graph',
            figure={
                'data': [
                    go.Scatter(
                        x=df['Time'],
                        y=df['Temp'],
                        mode='lines',
                        name='Temperature'
                    ),
                    go.Scatter(
                        x=df['Time'],
                        y=df['Humi'],
                        mode='lines',
                        name='Humidity'
                    )
                ],
                'layout': go.Layout(
                    title='Temperature and Humidity',
                    xaxis={'title': 'Time'},
                    yaxis={'title': 'Temp/Humi'}
                )
            }
        )
    ], style={'width': '80%', 'display': 'inline-block', 'padding': '10px'}),

    html.Div([
        html.H3("Temperature and Humidity Summary"),
        html.Table([
            html.Tr([html.Th('Metric'), html.Th('Average'), html.Th('Minimum'), html.Th('Maximum')]),
            html.Tr([html.Td('Temperature'), html.Td(f"{round(avg_temp, 2)}"), html.Td(min_temp), html.Td(max_temp)]),
            html.Tr([html.Td('Humidity'), html.Td(f"{round(avg_humidity, 2)}"), html.Td(min_humidity), html.Td(max_humidity)])
        ])
    ], style={'width': '50%', 'margin': 'auto', 'padding': '10px'})
])

# Callback to update the temperature-humidity graph based on the dropdown value and selected date
@app.callback(
    Output('temperature-humidity-graph', 'figure'),
    [Input('dropdown', 'value'), Input('date-picker', 'date')]
)
def update_graph(selected_value, selected_date):
    selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()  # Convert the selected date string to a datetime.date object

    # Filter the DataFrame based on the selected date
    filtered_df = df[df['Time'].dt.date == selected_date]

    if selected_value == 'temp':
        y_value = 'Temp'
        y_title = 'Temperature'
    else:
        y_value = 'Humi'
        y_title = 'Humidity'

    return {
        'data': [
            go.Scatter(
                x=filtered_df['Time'],
                y=filtered_df[y_value],
                mode='lines',
                name=y_title
            )
        ],
        'layout': go.Layout(
            title='Temperature and Humidity',
            xaxis={'title': 'Time'},
            yaxis={'title': y_title}
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)

