
import pandas as pd
import plotly.graph_objects as go

# Load the data from the CSV file into a Pandas DataFrame
data = pd.read_csv("data.csv")

# Calculate the average, minimum and maximum temperature and humidity using Pandas
avg_temp = data["Temperature"].mean()
min_temp = data["Temperature"].min()
max_temp = data["Temperature"].max()
avg_humidity = data["Humidity"].mean()
min_humidity = data["Humidity"].min()
max_humidity = data["Humidity"].max()

# Create a Plotly figure using the calculated values
fig = go.Figure(
    layout=dict(height=600, width=800, margin=dict(l=50, r=50, t=50, b=50, pad=4))  # Set the figure size and margins
)
fig.add_trace(go.Indicator(
    mode="number",
    value=avg_temp,
    title={"text": "Average Temperature"},
    domain={'row': 0, 'column': 0}
))
fig.add_trace(go.Indicator(
    mode="number",
    value=min_temp,
    title={"text": "Minimum Temperature"},
    domain={'row': 0, 'column': 1}
))
fig.add_trace(go.Indicator(
    mode="number",
    value=max_temp,
    title={"text": "Maximum Temperature"},
    domain={'row': 0, 'column': 2}
))
fig.add_trace(go.Indicator(
    mode="number",
    value=avg_humidity,
    title={"text": "Average Humidity"},
    domain={'row': 1, 'column': 0}
))
fig.add_trace(go.Indicator(
    mode="number",
    value=min_humidity,
    title={"text": "Minimum Humidity"},
    domain={'row': 1, 'column': 1}
))
fig.add_trace(go.Indicator(
    mode="number",
    value=max_humidity,
    title={"text": "Maximum Humidity"},
    domain={'row': 1, 'column': 2}
))

# Add a layout to the figure to set the title and axis labels
fig.update_layout(
    title="Temperature and Humidity Summary",
    xaxis_title="",
    yaxis_title="",
    template='simple_white',
    margin=dict(l=50, r=50, t=100, b=50),
    grid={'rows': 2, 'columns': 3, 'pattern': "independent"},
)

# Add titles to the columns
fig.add_annotation(x=0.16, y=1.1, text="Temperature", font=dict(size=16), showarrow=False, xref="paper", yref="paper", align='center')
fig.add_annotation(x=0.54, y=1.1, text="Humidity", font=dict(size=16), showarrow=False, xref="paper", yref="paper", align='center')

# Show the figure
fig.show()
