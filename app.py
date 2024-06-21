import streamlit as st
from streamlit_gsheets import GSheetsConnection

if "go_next" not in st.session_state:
    st.session_state.go_next = False

if st.session_state.go_next:
    del st.session_state.go_next
    st.switch_page("pages/participants.py")

def next():
    # st.print("in here")
    name = st.session_state.participant_name
    st.write(f"name: {name}")
    st.session_state.p1_name = name
    st.session_state.go_next = True


conn = st.connection("gsheets", type=GSheetsConnection)
url = "https://docs.google.com/spreadsheets/d/1fQz2Ix6heBb8ORtGFsNqcPodfM79a-29_9WMWHcEJR0/edit#gid=1446078968"
df = conn.read(spreadsheet=url, ttl="1m")
prompts = df.set_index("name").to_dict()["prompt"]

# st.write(prompts["present_levels_feedback"])

st.header("Prompts from Google Spreadsheet")

for i, row in enumerate(df.itertuples(), 1):
    st.divider()
    st.markdown(f"{i}: {row.name}")
    st.markdown(f"{row.prompt}")

with st.form("select_llm"):
    text_input = st.text_input(
        "Name 👇",
        key="participant_name",
        # label_visibility=st.session_state.visibility,
        # disabled=st.session_state.disabled,
        # placeholder=st.session_state.placeholder,
    )

    st.form_submit_button("🚀 Start writing IEP Goals", on_click=next)
