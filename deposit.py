import streamlit as st
from sql import create_db,insert_data,check_user

query_params = st.experimental_get_query_params()
if query_params.get("deposit") == "deposit":
    st.title("DEPOSIT YOUR MONEY")

    amount = st.number_input("Enter the amount to be deposited ")

    if st.button("DEPOSIT"):
        st.success("DEPOSITED SUCESSFULLY")  

# st.title("DEPOSIT YOUR MONEY")

# amount = st.number_input("Enter the amount to be deposited ")

# if st.button("DEPOSIT"):
#         st.success("DEPOSITED SUCESSFULLY")        
        
        