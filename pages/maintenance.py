import streamlit as st
def update_price_from_euro():
    st.session_state.price_dollar = st.session_state.price_euro * 1.1
def update_price_from_dollar():
    st.session_state.price_euro = st.session_state.price_dollar * 0.9


st.title("🔧 Maintenance")
st.write("Shedule maintenance tasks here.")

tab1, tab2 = st.tabs(["Upcoming Maintance", "Miantain cost"])

with tab1:
    # Add widgets for device management (example)
    device_id = st.text_input("Enter device ID")
    selected_date = st.date_input("Select a date", value=None)
   
    if st.button("Register Maintance"):
        st.success(f"Device {device_id} sheduled for maintenance on {selected_date}!")

    container = st.container(border=True)
    container.write("Device ID: Gerät1")
    container.write(f"Gerät1 will be maintained in 10.09.2025")
with tab2:
    
    current_device = st.selectbox(label='Choose Device', options=["Geräte1"," Gerät2"])
    
    cost_eur = st.number_input(label="maintaincost in €", 
                                key = "price_euro",
                                on_change=update_price_from_euro)
    
    cost_usd = st.number_input(label="maintaincost in USD", 
                                key = "price_dollar",
                                on_change=update_price_from_dollar)
    
    if st.button("Enter cost"):
        st.success(f"the maintance for the {current_device} will cost {cost_eur} € ")