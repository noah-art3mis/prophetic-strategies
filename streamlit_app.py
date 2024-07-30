import os
from pathlib import Path
import streamlit as st
from openai import OpenAI
from utils.utils import stream_data
import sqlite3

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
question = st.text_input("What is it that you desire to (not) know?")
st.write("")
st.write("")

# if question != "":
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
# st.write_stream(
#     client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": question}],
#         stream=True,
#         temperature=1.0,
#         max_tokens=512,
#     )
# )


def get_sentence_from_db(db: Path) -> dict:
    # requires table to have same name as db file
    table = os.path.basename(db).replace(".db", "")
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()
        cur.execute(
            f"""SELECT * FROM {table} ORDER BY RANDOM() LIMIT 1"""
        )  # sql injection?
        row = cur.fetchone()
        cur.close()

        sentence = {
            "book": row[0],
            "sentence": row[1],
            "chapter": row[2],
            "sentence_chapter": row[3],
            "content": row[4],
            "embedding": row[5],
        }

        return sentence


if question != "":
    result = get_sentence_from_db(strategy)
    st.write_stream(stream_data(result["content"]))
    st.write("")
    st.caption(result["book"])
    st.caption(f"Sentence {result['sentence']}")
    st.write(result["embedding"])
