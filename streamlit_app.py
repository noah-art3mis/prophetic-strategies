import time
import random
import streamlit as st
from openai import OpenAI
from strategies import strategies_oblique, strategies_alchemist, strategies_prophet

STRATEGIES = {
    "Oblique Strategies": strategies_oblique,
    "Alchemist Strategies": strategies_alchemist,
    "Prophet Strategies": strategies_prophet,
}


with st.sidebar:
    st.header("Parameters")
    strategy_name = st.selectbox("Strategy", list(STRATEGIES.keys()))
    strategy = STRATEGIES[strategy_name] # type: ignore

st.title("Prophetic Strategies")
st.write("")
question = st.text_input("Ask and you shall receive")
st.write("")

st.header("Answer")
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


def stream_data(data):
    for word in data.split(" "):
        yield word + " "
        time.sleep(0.12)

if question != "":
    sample = random.sample(strategy, 1)  # type: ignore
    st.write_stream(stream_data(sample[0]))
