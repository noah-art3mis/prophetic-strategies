import os
import sqlite3
from pathlib import Path

import pandas as pd
import numpy as np
import streamlit as st
from openai import OpenAI


def search(question: str, db: Path) -> pd.Series:
    qv = _get_embedding(question)

    # requires table to have same name as db file
    table = os.path.basename(db).replace(".db", "")
    df = pd.read_sql(f"""SELECT * FROM {table}""", con=sqlite3.connect(db))

    df["similarity"] = df["embedding"].apply(lambda x: _cosine_similarity(x, qv))

    return df.sort_values("similarity", ascending=False).head(1).iloc[0]


def _get_embedding(text: str) -> list[float]:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    response = client.embeddings.create(input=text, model="text-embedding-3-small")
    return response.data[0].embedding


def _cosine_similarity(a, b: list):
    a = _decode_binary_data(a)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def _decode_binary_data(data):
    # Convert binary data to a numpy array of floats
    num_elements = len(data) // 8  # Each float64 is 8 bytes
    decoded_array = np.frombuffer(data, dtype=np.float64, count=num_elements)
    return decoded_array
