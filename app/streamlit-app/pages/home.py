import streamlit as st
import time
from config.config import page_spacing

cols = page_spacing()

intro = (
    "## 👋 Welcome to the **YouTube Anomaly Detection App**\n\n"
    "This tool helps uncover trends and outliers in YouTube data.\n\n"
    "### 🔍 Objectives\n"
    "- Detect **anomalies** in a YouTube dataset\n"
    "- Visualize **trends**, and **patterns**\n\n"
    "_Built by **Jayson Pradhananga**_"
)

def stream_data():
    for letter in intro:
        yield letter
        time.sleep(0.02)

with cols["content"]:
    st.write_stream(stream_data())
    st.divider()
    st.markdown("Click the following buttons to be redirected:\n")
    spacer1, link1, link2, spacer2 = st.columns([1,2,2,1])
    with link1:
        st.page_link("pages/youtube_anomaly.py", label="📊 YouTube Anomaly Detection")
    with link2:
        st.page_link("pages/trend.py", label="📈 YouTube Trend Analysis")