import streamlit as st
from func import is_valid_pin, generate_unique_id
from sql import create_db, insert_data, check_user, update_balance,withdraw_balance,update_pin,check_balance

st.set_page_config(
    page_title="ATM APP"
)

st.title("ATM APP USING PYTHON AND SQL")
if 'flag' not in st.session_state:
    st.session_state.flag = False

new, existing = st.columns(2)

with new:
    st.header("NEW USER REGISTRATION")
    name = st.text_input("NAME", "")
    pin = st.text_input("Enter a 4-digit PIN:")
    balance = 0
    if st.button("GENERATE MY UNIQUE ID"):
        if is_valid_pin(pin):
            unique_id = generate_unique_id()
            st.success(f"Your unique ID is: {unique_id}")
            st.success("Your registration is successful")

            create_db()
            insert_data(name, pin, unique_id, balance)

with existing:
    st.header("EXISTING USER LOGIN PORTAL")
    unique_id = st.text_input("Enter your unique id ")
    pin = st.text_input("Enter your pin ")
    if st.button("Login"):
        user_data = check_user(unique_id, pin)
        if user_data:
            st.success(f"Welcome, {user_data[0]}! Login successful.")
            st.session_state.flag = True
        else :
            st.error("Check your unique id or pin ")
st.write("------------------------------------------------------------------------------------------------------------------------------------------------")
if st.session_state.flag:
    deposit, withdraw, change_pin, balance_check = st.columns(4)
    with deposit:
        st.subheader("DEPOSIT")
        unique_id = unique_id
        deposit_amount = st.number_input("Enter the amount to deposit")
        if st.button("DEPOSIT"):
            update_balance(unique_id, deposit_amount)
            st.write(f"💸₹{deposit_amount} Deposited")
            st.success("SUCCESS")
    
    with withdraw:
        st.subheader("WITHDRAW")
        unique_id = unique_id
        withdraw_amount = st.number_input("Enter the amount to withdraw")
        if st.button("WITHDRAW"):
            withdraw_balance(unique_id, withdraw_amount)
            st.write(f"💸₹{withdraw_amount} Withdrawn")
            st.success("SUCCESS")
    
    with change_pin:
        st.subheader("CHANGE PIN")
        unique_id=unique_id
        new_pin = st.text_input("Enter the new pin ")
        if st.button("CHANGE PIN"):
            if is_valid_pin(new_pin):
                update_pin(unique_id, new_pin)
                st.success("PIN changed successfully.")
            else:
                st.error("Please enter a valid 4-digit PIN.")
    
    with balance_check:
        st.subheader("CHECK BALANCE")
        unique_id=unique_id
        if st.button("CHECK BALANCE"):
            current_balance = check_balance(unique_id)
            st.write("Your current balance is : ")
            st.success(f"💸₹{current_balance}")




