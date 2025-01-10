import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="🚀",
    layout="wide",
)

st.title("Welcome to the Dashboard! 🚀")
st.write("Use the sidebar to navigate through different sections of the app.")

# Optionally, add a welcome image or custom content
st.image("src/welcome_image.png", use_container_width=True)
