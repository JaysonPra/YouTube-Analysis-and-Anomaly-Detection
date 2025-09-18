import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from preprocessing.preprocess_core import preprocessor

st.set_page_config(
    layout="wide"
)

with st.spinner("Loading the YouTube dataset and preparing dashboard..."):
    df = preprocessor()

pg = st.navigation([
    st.Page("pages/home.py", title="Home", default=True),
    st.Page("pages/youtube_anomaly.py", title="YouTube Anomaly Detection"),
    st.Page("pages/trend.py", title="Trend Analysis")
], position="top")

pg.run()