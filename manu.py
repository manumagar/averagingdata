import pandas as pd  
import plotly.graph_objects as go

# Load the data from the CSV file into a Pandas DataFrame
df = pd.read_csv("data.csv")




filename = 'data.csv'   
date_column_name = 'date'   
value_column_name = 'temp'
value_column_name2 = 'humi'  
target_date = '3/11/2023'   

df = pd.read_csv(filename)
filtered_df = df[df[date_column_name] == target_date]

avg_temp = filtered_df[value_column_name].mean()
max_temp = filtered_df[value_column_name].max()
min_temp= filtered_df[value_column_name].min()

avg_humidity = filtered_df[value_column_name2].mean()
max_humidity= filtered_df[value_column_name2].max()
min_humidity= filtered_df[value_column_name2].min()

print(avg_temp)
print(avg_humidity)


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
