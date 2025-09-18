import streamlit as st
import joblib
import os
from config.config import page_spacing
from preprocessing.preprocess_core import preprocessor

def get_model_path():
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', '..', 'model', 'saves', 'isolation_pipeline.pkl')
    )

def model_predict():
    df = preprocessor()

    pipeline = joblib.load(get_model_path())

    features = ["views", "likes", "comments", "duration"]
    X = df[features].copy()
    predictions = pipeline.predict(X)

    df["is_anomaly"] = (predictions == -1).astype(int)

    return df

df = model_predict()
cols = page_spacing()

# Filter only anomalies
anomalies = df[df["is_anomaly"] == 1].reset_index(drop=True)

# Pagination setup
items_per_page = 10
total_pages = (len(anomalies) - 1) // items_per_page + 1
page = st.number_input("Page", min_value=1, max_value=total_pages, value=1, step=1)

start_idx = (page - 1) * items_per_page
end_idx = start_idx + items_per_page
page_data = anomalies.iloc[start_idx:end_idx]

with cols["content"]:
    st.markdown("# YouTube Anomaly Detection")
    for _, row in page_data.iterrows():
        with st.container():
            st.markdown(f"#### [{row['title']}]({row['url']})")
            st.markdown(
                f"**Views**: {row['views']:,}  |  "
                f"**Likes**: {row['likes']:,}  |  "
                f"**Comments**: {row['comments']:,}"
            )
            st.divider()
