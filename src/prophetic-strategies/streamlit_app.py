import streamlit as st
from pathlib import Path
from utils import fake_stream
from semantic_search import search, get_data

STRATEGIES = {
    "Oracle": Path("db/book5.db"),
    # "Navigator": Path("db/oblique.db"),
}

# with st.sidebar:
#     st.header("Parameters")
#     strategy_name = st.selectbox("Strategy", list(STRATEGIES.keys()))
#     db = STRATEGIES[strategy_name]  # type: ignore

db = Path("db/book5.db")

st.title("Prophetic Strategies")
# st.caption("[Source](https://github.com/noah-art3mis/prophetic-strategies)")
st.write("")
question = st.text_input("What is it that you desire (not) to know?")
st.write("")
st.write("")
st.write("")
st.write("")

if question != "":
    df = get_data(db)
    result = search(question, df)
    st.write_stream(fake_stream(result["content"]))
    st.write("")

    reference_book = result["book"]
    st.caption(
        f'<div style="text-align: right;">{reference_book}</div>',
        unsafe_allow_html=True,
    )

    sentence_number = "Sentence " + str(result["sentence"])
    st.caption(
        f'<div style="text-align: right;">{sentence_number}</div>',
        unsafe_allow_html=True,
    )

    # st.feedback()
