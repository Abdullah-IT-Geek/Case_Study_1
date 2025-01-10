import streamlit as st
from devices import Device

st.title("🖥️ Management")
st.write("Manage all Device Ownership here.")

tab1, tab2 = st.tabs(["Create new Device", "Change Device"])

with tab1:
    # Add widgets for device management (example)
    device_id = st.text_input("Enter device ID")
    managed_by_user_id = st.text_input("Enter user ID")
    if st.button("Assign User"):
        if (device_id == "" or managed_by_user_id == ""):
            st.error("ERROR: All inputs must contain data", icon="🚨")
        else:
            new_device = Device(device_id, managed_by_user_id)
            new_device.store_data()
            st.success(f"Device {managed_by_user_id} assigned to {device_id}")
with tab2:
    current_device = st.selectbox(label='Choose Device', options=Device.find_all())
    user_id_change = st.text_input("Change user ID")
    if st.button("Change"):
        if (user_id_change == ""):
            st.error("ERROR: Input does not contain data", icon="🚨")
        elif (user_id_change == current_device.managed_by_user_id):
            st.error("ERROR: Input cannot contain the same data", icon="🚨") 
        else:    
            if user_id_change == "":
                device_id_change = current_device.managed_by_user_id
            else:
                st.success(f"Device {current_device.managed_by_user_id} changed to {user_id_change}")
            current_device = Device(device_id_change,user_id_change)
            current_device.store_data()
            st.rerun()
    if st.button("Remove", icon="🗑️"):
        current_device.delete()
        st.rerun()