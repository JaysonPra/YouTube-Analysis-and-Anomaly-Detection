import streamlit as st
from config.config import page_spacing
from preprocessing.preprocess_core import preprocessor
import altair as alt
import pandas as pd
from collections import Counter

df = preprocessor()

cols = page_spacing()

with cols["content"]:
    st.write("YouTube Trend Analysis")
    tab1, tab2, tab3 = st.tabs(["📊 Category Trend", "⏱️ Duration vs Engagement", "🏷️ Top Tags"])

    with tab1:
        category_counts = df["category"].value_counts().reset_index()
        category_counts.columns = ["category", "count"]

        chart1 = alt.Chart(category_counts).mark_bar().encode(
            x=alt.X("category:N", sort="-y", title="Category"),
            y=alt.Y("count:Q", title="Number of Videos"),
            color="category:N",
            tooltip=["category", "count"]
        ).properties(
            title="📈 Category Distribution",
            width=600,
            height=400
        )

        st.altair_chart(chart1, use_container_width=True)

    with tab2:
        engagement_df = df.copy()

        # Filter out top 1% outliers
        duration_q = engagement_df["duration"].quantile(0.99)
        engagement_q = engagement_df["engagement_score"].quantile(0.99)

        filtered_df = engagement_df[
            (engagement_df["duration"] <= duration_q) &
            (engagement_df["engagement_score"] <= engagement_q)
        ]

        chart2 = alt.Chart(filtered_df).mark_circle(size=60).encode(
            x=alt.X("duration:Q", title="Duration (seconds)"),
            y=alt.Y("engagement_score:Q", title="Total Engagement"),
            color="category:N",
            tooltip=["title", "duration", "views", "likes", "comments", "engagement_score"]
        ).properties(
            title="⏱️ Duration vs Engagement (Filtered)",
            width=600,
            height=400
        )

        st.altair_chart(chart2, use_container_width=True)


    with tab3:
        tag_series = df["hashtags"].dropna()
        flat_tags = [tag.strip() for sublist in tag_series for tag in sublist]

        # Count tag frequency
        tag_counts = Counter(flat_tags)
        tag_df = (
            pd.DataFrame(tag_counts.items(), columns=["tag", "count"])
            .sort_values("count", ascending=False)
            .head(20)
        )

        chart = alt.Chart(tag_df).mark_bar().encode(
            x=alt.X("tag:N", sort="-y", title="Tag"),
            y=alt.Y("count:Q", title="Frequency"),
            color="tag:N",
            tooltip=["tag", "count"]
        ).properties(
            title="🏷️ Top Tags",
            width=600,
            height=400
        )

        st.altair_chart(chart, use_container_width=True)