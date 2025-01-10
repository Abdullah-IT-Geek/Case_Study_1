import streamlit as st

st.title("📱 Reservation")
st.write("Reserve a device")

# Add widgets for device management (example)

tab1, tab2 = st.tabs(["Upcoming Reservation", "Create Reservation"])

with tab1:
     container = st.container(border=True)
     container.write("Device ID: Gerät1")
     container.write("Reservation from 10.10.2025 until 15.10.2025")
with tab2:
    device_id = st.text_input("Enter device ID")
    selected_date_start = st.date_input("Select a start date", value=None)
    selected_date_end = st.date_input("Select a end date", value=None)
    if st.button("Register Device"):
        st.success(f"Device {device_id} is resevited from {selected_date_start} until {selected_date_end}!")
    




