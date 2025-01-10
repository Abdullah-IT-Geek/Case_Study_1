import streamlit as st
from users import User

#@st.dialog("User")
#def New_user():
#        st.write("Create a new User:")
#        user_ID = st.text_input("User_ID:")
#        user = st.text_input("Created by (Please, enter your email!!) ")
#        if st.button("Submit"):
#            new_user = User(user_ID,user)
#            new_user.store_data()
#            st.rerun()
                
st.title("👤 User Management")
st.write("Manage all the users here.")

# Add widgets for user management (example)
#user_name = st.text_input("Enter user name")
#if st.button("Add User"):
#    st.success(f"User {user_name} added successfully!")
# Überschrift der ersten Ebene

# Benutzername aus der Selectbox abrufen


# Benutzer löschen

tab1, tab2 = st.tabs(["Create User", "Delete User"])
 
with tab1:
    # Add widgets for device management (example)
    user_name = st.text_input("Enter Username")
    user_email = st.text_input("Enter your email")
    if st.button("Create User"):
        if (user_name== "" or user_email == ""):
            st.error("ERROR: All inputs must contain data", icon="🚨")
        else:
            new_user = User(user_email, user_name)
            new_user.store_data()
            st.success(f"User {user_name} created by {user_email}")
        st.rerun()
with tab2:
    #users = User.find_all()  # Liste aller User-Objekte abrufen
    #print(users)  # Debugging: Alle Benutzer anzeigen
    current_user = st.selectbox(label='Choose User', options=User.find_all())
    #print(selected_user)
    if st.button("Remove", icon="🗑️"):
        current_user.delete()  # Löscht den ausgewählten Benutzer
        st.rerun()

    