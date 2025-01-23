import streamlit as st
from datetime import date
from maintanence_service import MaintanenceService
from devices import Device

rates = {
        "EUR": 1.0,      # Basis
        "USD": 1.1,      # Beispielkurs: 1 EUR = 1.1 USD
        "GBP": 0.85      # Beispielkurs: 1 EUR = 0.85 GBP
    }

def convert_price(amount, currency, direction="to_currency"):
    """
    Convert a price between currencies.

    Args:
        amount (float): The amount to convert.
        currency (str): The target currency.
        direction (str): Conversion direction, either "to_currency" (default) or "from_currency".

    Returns:
        float: Converted amount.
    """
    if direction == "to_currency":
        return amount * rates[currency]
    elif direction == "from_currency":
        return amount / rates[currency]
    else:
        raise ValueError("Invalid direction. Use 'to_currency' or 'from_currency'.")


st.title("🔧 Maintenance")
st.write("Schedule maintenance tasks here.")

tab1, tab2 = st.tabs(["Upcoming Maintance", "Maintance cost"])

with tab1:
    selected_currency = st.selectbox("Choose Currency", options=rates.keys(), key="upcoming")
    for maintanence in MaintanenceService().find_all_maintanence():
        container = st.container(border=True)
        container.write(f"Maintanence for {maintanence.device_id}")
        container.write(f"Costs {convert_price(maintanence.price, selected_currency, "from_currency")}")
        container.write(f"From {maintanence.start_date}")
        container.write(f"Until {maintanence.end_date}")
with tab2:
    
    selected_device_id = st.selectbox(label='Choose Device', options=Device.find_all(), format_func=lambda x: x.get_ID())
    selected_currency = st.selectbox("Choose Currency", options=rates.keys(), key="cost")
    price = st.number_input(f"Price in {selected_currency}", value=0.0)
    price = convert_price(price, selected_currency)
    selected_date_start = st.date_input("Select a start date", value=date.today())
    selected_date_end = st.date_input("Select a end date", value=date.today())
    
    if st.button("Enter cost"):
        maintanence_service = MaintanenceService()
        maintanence_service.create_maintanence(selected_device_id.get_ID(), price, selected_date_start, selected_date_end)
        st.rerun()
        st.success(f"Reservation from {selected_date_start} until {selected_date_end} for {selected_device_id} costs {price}")