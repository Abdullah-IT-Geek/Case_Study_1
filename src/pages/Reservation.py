import streamlit as st
from datetime import date
from reservation_service import ReservationService
from users import User
from devices import Device

st.title("📱 Reservation")
st.write("Reserve a device")

# Add widgets for device management (example)

tab1, tab2 = st.tabs(["Upcoming Reservation", "Create Reservation"])

with tab1:
    for reservation in ReservationService().find_all_reservations():
        container = st.container(border=True)
        container.write(f"Reservation for {reservation.device_id}")
        container.write(f"Created by {reservation.user_id}")
        container.write(f"From {reservation.start_date}")
        container.write(f"Until {reservation.end_date}")

with tab2:
    selected_user_id = st.selectbox(label='Choose User', options=User.find_all(), format_func=lambda x: x.get_ID())
    selected_device_id = st.selectbox(label='Choose Device', options=Device.find_all(), format_func=lambda x: x.get_ID())
    selected_date_start = st.date_input("Select a start date", value=date.today())
    selected_date_end = st.date_input("Select a end date", value=date.today())
    if st.button("Register Device"):
        reservation_service = ReservationService()
        reservation_service.create_reservation(selected_user_id.get_ID(), selected_device_id.get_ID(), selected_date_start, selected_date_end)
        st.rerun()
        st.success(f"Reservation from {selected_date_start} until {selected_date_end} for {selected_device_id} created by {selected_user_id}")
    