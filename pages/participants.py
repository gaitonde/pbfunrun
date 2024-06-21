# example/st_app_gsheets_using_service_account.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read Google Sheet as DataFrame")

# st.write(st.session_state.p1_name)

st.write("name? ^")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Output")

st.dataframe(df)
