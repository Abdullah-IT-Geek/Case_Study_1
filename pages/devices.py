import streamlit as st

st.title("📱 Device Management")
st.write("Manage all your devices here.")

# Add widgets for device management (example)
device_id = st.text_input("Enter device ID")
if st.button("Register Device"):
    st.success(f"Device {device_id} registered successfully!")
