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
))
fig.add_trace(go.Indicator(
    mode="number",
    value=min_temp,
    title={"text": "Minimum Temperature"},
))
fig.add_trace(go.Indicator(
    mode="number",
    value=max_temp,
    title={"text": "Maximum Temperature"},
))
fig.add_trace(go.Indicator(
    mode="number",
    value=avg_humidity,
    title={"text": "Average Humidity"},
))
fig.add_trace(go.Indicator(
    mode="number",
    value=min_humidity,
    title={"text": "Minimum Humidity"},
))
fig.add_trace(go.Indicator(
    mode="number",
    value=max_humidity,
    title={"text": "Maximum Humidity"},
))

# Add a layout to the figure to set the title and axis labels
fig.update_layout(
    title="Temperature and Humidity Summary",
    xaxis_title="Category",
    yaxis_title="Value",
    template='simple_white',
    margin=dict(l=50, r=50, t=100, b=50),
    **{
        "annotations": [
            {
                "text": "Temperature",
                "x": 0.16,
                "y": 1.05,
                "showarrow": False,
                "font": {"size": 16}
            },
            {
                "text": "Humidity",
                "x": 0.54,
                "y": 1.05,
                "showarrow": False,
                "font": {"size": 16}
            }
        ],
        "xaxis1": {"anchor": "y2", "domain": [0.0, 0.29]},
        "xaxis2": {"anchor": "y2", "domain": [0.33, 0.62]},
        "xaxis3": {"anchor": "y2", "domain": [0.67, 0.96]},
        "yaxis1": {"anchor": "x1", "domain": [0.55, 1.0]},
        "yaxis2": {"anchor": "x2", "domain": [0.55, 1.0]},
        "yaxis3": {"anchor": "x3", "domain": [0.55, 1.0]},
        "yaxis4": {"anchor": "x1", "domain": [0.0, 0.45]}
    }
)
fig.show()