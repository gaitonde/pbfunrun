import streamlit as st
from streamlit_gsheets import GSheetsConnection
import datetime
import pandas as pd
from io import StringIO

if "go_next" not in st.session_state:
    st.session_state.go_next = False

if "st.session_state.participant_name" not in st.session_state:
    st.session_state.participant_name = None

if st.session_state.go_next:
    del st.session_state.go_next
    st.switch_page("pages/participants.py")

def next():
    # st.print("in here")
    name = st.session_state.participant_name
    st.write(f"name: {name}")
    st.session_state.p1_name = name

    now = datetime.datetime.now()
    TESTDATA = f"""\
        id, name, email, registered
        1, {st.session_state.participant_name},  john@acme.com,  {now}
    """
    df = pd.read_csv(StringIO(TESTDATA), index_col=0, sep=r",\s*", engine='python')

    # Create GSheets connection
    conn = st.connection("gsheets", type=GSheetsConnection)

    df = conn.update(
        worksheet="Example 1",
        data=df,
    )
    st.cache_data.clear()
    # st.experimental_rerun()

    # st.session_state.go_next = True



# click button to update worksheet
# This is behind a button to avoid exceeding Google API Quota
# if st.button("Update worksheet"):
#     df = conn.update(
#         worksheet="Example 1",
#         data=df,
#     )
#     st.cache_data.clear()
#     st.experimental_rerun()

    # Display our Spreadsheet as st.dataframe
    # st.dataframe(df.head(10))


with st.form("form_1"):
    text_input = st.text_input(
        "Name 👇",
        key="participant_name",
    )

    st.form_submit_button("🚀 Off to the races", on_click=next)
