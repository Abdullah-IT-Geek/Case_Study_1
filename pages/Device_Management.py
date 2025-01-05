import streamlit as st

st.title("🖥️ Management")
st.write("Manage all Device Ownership here.")

tab1, tab2 = st.tabs(["Create new Device", "Change Device"])

with tab1:
    # Add widgets for device management (example)
    device_id = st.text_input("Enter device ID")
    user_id = st.text_input("Enter user ID")
    if st.button("Assign User"):
        st.success(f"Device {user_id} assigned to {device_id}")
with tab2:
    current_device = st.selectbox(label='Chose Device', options=["Geräte1"," Gerät2"])
    device_id_change = st.text_input("Change device ID")
    user_id_change = st.text_input("Change user ID")
    if st.button("Change"):
        st.success(f"Device {user_id} changed to {user_id_change}")
        st.success(f"Device {device_id} changed to {device_id_change}")