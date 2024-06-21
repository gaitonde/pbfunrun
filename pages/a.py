# app.py

import streamlit as st
import pandas as pd
import pandasql as psql

st.title("Pandasql in Streamlit")

# Sample DataFrame
df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [4, 5, 6]
})

# Sample SQL query
query = "SELECT * FROM df WHERE a > 1"

# Use pandasql to query the DataFrame
result = psql.sqldf(query, locals())

# Display the result
st.write(result)
