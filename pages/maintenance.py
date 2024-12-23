import streamlit as st

st.title("🔧 Maintenance")
st.write("Shedule maintenance tasks here.")

# Add widgets for device management (example)
device_id = st.text_input("Enter device ID")
selected_date = st.date_input("Select a date", value=None)
if st.button("Register Device"):
    st.success(f"Device {device_id} sheduled for maintenance on {selected_date}!")
