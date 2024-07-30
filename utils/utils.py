import pandas as pd
import streamlit as st
from openai import OpenAI
import numpy as np
import time
from typing import Generator
import sqlite3
import os
from pathlib import Path


def fake_stream(sentence: str) -> Generator[str, None, None]:
    for word in sentence.split(" "):
        yield word + " "
        time.sleep(0.05)


def decode_binary_data(data):
    # Convert binary data to a numpy array of floats
    num_elements = len(data) // 8  # Each float64 is 8 bytes
    decoded_array = np.frombuffer(data, dtype=np.float64, count=num_elements)
    return decoded_array


def cosine_similarity(a, b: list):
    a = decode_binary_data(a)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def get_embedding(text: str) -> list[float]:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    response = client.embeddings.create(input=text, model="text-embedding-3-small")
    return response.data[0].embedding


def get_random_sentence_from_db(db: Path) -> dict:
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


def rag(question: str, db: Path) -> pd.Series:
    qv = get_embedding(question)

    # requires table to have same name as db file
    table = os.path.basename(db).replace(".db", "")
    df = pd.read_sql(f"""SELECT * FROM {table}""", con=sqlite3.connect(db))

    df["similarity"] = df["embedding"].apply(lambda x: cosine_similarity(x, qv))

    return df.sort_values("similarity", ascending=False).head(1).iloc[0]
