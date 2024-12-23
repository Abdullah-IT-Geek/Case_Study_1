import streamlit as st

st.title("🖥️ Management")
st.write("Manage all Device Ownership here.")

# Add widgets for device management (example)
device_id = st.text_input("Enter device ID")
user_id = st.text_input("Enter user ID")
if st.button("Assign User"):
    st.success(f"Device {user_id} assigned to {device_id}")
