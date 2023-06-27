import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_echarts import st_echarts
import json

data = pd.read_csv("models.csv")
# Convert DataFrame to JSON
j = data.to_json(orient="records")
# Convert JSON string to a list of dictionaries
json_data = json.loads(j)

time = [d["time"] for d in json_data if "time" in d]
parameter = [d["parameter"] for d in json_data if d is not None]
print(time, "json")


def main():
    st.title("Simulation Dashboard")
    # Display the data
    st.subheader("Generated Data")
    st.write(data)
    # Plot the data
    st.subheader("Line Chart")
    options = {
        "title": {"text": "Chart for the model"},
        "tooltip": {
            "dataZoom": {"yAxisIndex": "true"},
            "trigger": "axis",
            "axisPointer": {"type": "shadow"},
        },
        "legend": {"top": "7%", "left": "center"},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": "true"},
        "yAxis": {"type": "value"},
        "xAxis": {"type": "category", "data": time},
        "series": [
            {
                "name": "parameter",
                "type": "line",
                "stack": "total",
                "label": {"show": "true"},
                "emphasis": {"focus": "series"},
                "data": parameter,
            },
        ],
    }
    st_echarts(options=options)


if __name__ == "__main__":
    main()
