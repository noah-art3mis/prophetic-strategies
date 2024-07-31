import os
import sqlite3
from pathlib import Path

import pandas as pd
import numpy as np
import streamlit as st
from openai import OpenAI

TOKEN_MULTIPLIER = 1


@st.cache_data
def get_data(db: Path) -> pd.DataFrame:
    # requires table to have same name as db file
    table = os.path.basename(db).replace(".db", "")
    return pd.read_sql(f"""SELECT * FROM {table}""", con=sqlite3.connect(db))


def get_embedding(text: str) -> list[float]:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    response = client.embeddings.create(input=text, model="text-embedding-3-small")
    completion = response.data[0].embedding

    _update_tokens(response.usage.total_tokens)
    return completion


def _update_tokens(n_tokens: int):
    value = (st.session_state.tokens_used + n_tokens) * TOKEN_MULTIPLIER
    result = min(100, value)
    st.session_state.tokens_used = int(result)


def cosine_similarity(a, b: list):
    a = _decode_binary_data(a)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def _decode_binary_data(data):
    # Convert binary data to a numpy array of floats
    num_elements = len(data) // 8  # Each float64 is 8 bytes
    decoded_array = np.frombuffer(data, dtype=np.float64, count=num_elements)
    return decoded_array
