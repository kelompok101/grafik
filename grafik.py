import streamlit as st
import plotly.graph_objects as go

# Data
x_values = [1, 2, 3, 4, 5]
y_values = [10, 20, 15, 25, 30]

# Create a Plotly figure
fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='lines'))

# Add title and axis labels
fig.update_layout(title='Contoh Grafik Plotly', xaxis_title='X-axis', yaxis_title='Y-axis')

# Display the Plotly figure using st.plotly_chart
st.plotly_chart(fig)