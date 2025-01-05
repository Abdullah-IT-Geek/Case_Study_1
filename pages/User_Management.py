import streamlit as st

@st.dialog("User")
def New_user():
        st.write("Create a new User:")
        User_ID = st.text_input("User_ID:")
        user = st.text_input("Created by (Please, enter your email!!) ")
        st.session_state.User = {}
        if st.button("Submit"):
            if User_ID not in st.session_state.User:
                st.session_state.User[User_ID] = user
            st.rerun()
                
st.title("👤 User Management")
st.write("Manage all the users here.")

# Add widgets for user management (example)
#user_name = st.text_input("Enter user name")
#if st.button("Add User"):
#    st.success(f"User {user_name} added successfully!")
# Überschrift der ersten Ebene

# Auswahlbox mit Geräten
current_device = st.selectbox(label='Choose Device', options=["Geräte1"," Gerät2"])

# Anzeige des ausgewählten Geräts
st.write(f"the current Device is {current_device}")

# Layout mit 3 Spalten
left, middle, right = st.columns([5, 1, 1])

# Button zum Erstellen eines neuen Geräts
if right.button("Create"):
    New_user()

# Anzeige der bestehenden Geräte
if "User" in st.session_state and len(st.session_state.User) > 0:
    st.write("Existing devices:")
    for user, name in st.session_state.User.items():
        st.write(f"{user} with the name {name}")