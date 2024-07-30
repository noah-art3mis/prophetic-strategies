import streamlit as st
from pathlib import Path

from utils.utils import fake_stream
from utils.utils import rag

STRATEGIES = {
    # "Navigator": Path("db/oblique.db"),
    "Oracle": Path("db/book5.db"),
}

with st.sidebar:
    st.header("Parameters")
    strategy_name = st.selectbox("Strategy", list(STRATEGIES.keys()))
    strategy = STRATEGIES[strategy_name]  # type: ignore

st.title("Prophetic Strategies")
st.write("")
question = st.text_input("What is it that you desire (not) to know?")
st.write("")
st.write("")


if question != "":
    result = rag(question, strategy)
    st.write_stream(fake_stream(result["content"]))
    st.write("")
    st.caption(result["book"])
    st.caption(f"Sentence {result['sentence']}")
