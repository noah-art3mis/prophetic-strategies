import streamlit as st
from pathlib import Path
from utils import fake_stream, find_prophet
from semantic_search import get_data

db = Path("db/book5.db")

if "feedback" not in st.session_state:
    st.session_state.feedback = None

if "tokens_used" not in st.session_state:
    st.session_state.tokens_used = 0

if "answer" not in st.session_state:
    st.session_state.answer = None


st.title("Prophetic Strategies")
st.write("")

ith st.sidebar:
    st.header("Parameters")
    strategy = st.selectbox("Strategy", ["Navigator", "Oracle"])

    st.markdown("---")
    st.write("Made by Gustavo Costa.")
    st.write(
        "[Source code](https://github.com/noah-art3mis/prophetic-strategies) / [Blog](https://gustavocosta.psc.br/) / [Instagram](https://www.instagram.com/simulacro.psi/) / [Twitter](https://x.com/simulacrum_ai) / [LinkedIn](https://www.linkedin.com/in/gustavoarcos/)"
    )
   st.write("")
    st.write("")

if st.session_state.tokens_used >= 50:
    p1, p2 = st.columns(2)
    progress_bar = p1.progress(
        st.session_state.tokens_used, text="Prophet's lack of patience"
    )

if st.session_state.tokens_used >= 100:
    st.write("The oracle tires of your antics. Please come another time.")
else:
    with st.form("my_form", border=False):
        st.write("")
        question = st.text_input("What is it that you desire (not) to know?")
        submit = st.form_submit_button("O, Prophet...")

    if submit:
        df = get_data(db)
        prophet = find_prophet(strategy)  # type: ignore
        answer = prophet.search(question, df)
        st.session_state.answer = answer
        st.session_state.feedback = None

    result = st.session_state.answer

    if result is not None:
        if submit:
            st.write_stream(fake_stream(result["content"]))
        else:
            st.write(result["content"])

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

        # def thanks():
    #     st.toast("The prophet thanks you for the feedback.")

    # if st.session_state.feedback is None:
    #     feedback = st.feedback(on_change=thanks)