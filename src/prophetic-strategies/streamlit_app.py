import streamlit as st
from pathlib import Path
from utils.utils import fake_stream
from utils.semantic_search import search

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
    result = search(question, db)
    st.write_stream(fake_stream(result["content"]))
    st.write("")

st.caption(
    f'<div style="text-align: right;">{result["book"]}</div>', unsafe_allow_html=True
)
st.caption(
    f'<div style="text-align: right;">Sentence {result["sentence"]}</div>',
    unsafe_allow_html=True,
)
