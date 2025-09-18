import streamlit as st

def page_spacing():
    left_margin, left_sidebar, content, right_margin = st.columns(
        [0.25, 0.25, 3, 0.5],
    )
    return {
        "left_margin": left_margin,
        "left_sidebar": left_sidebar,
        "content": content,
        "right_margin": right_margin
    }