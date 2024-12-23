import streamlit as st

st.title("👤 User Management")
st.write("Manage all the users here.")

# Add widgets for user management (example)
user_name = st.text_input("Enter user name")
if st.button("Add User"):
    st.success(f"User {user_name} added successfully!")
