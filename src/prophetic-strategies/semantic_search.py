import pandas as pd
import numpy as np
import streamlit as st
from openai import OpenAI

from utils import update_tokens


def semantic_search(question: str, df: pd.DataFrame) -> pd.Series:
    qv = _get_embedding(question)
    df["similarity"] = df["embedding"].apply(lambda x: _cosine_similarity(x, qv))
    df = df.sort_values("similarity", ascending=False)
    top_result = df.iloc[0]
    return top_result


def _get_embedding(text: str) -> list[float]:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    response = client.embeddings.create(input=text, model="text-embedding-3-small")
    completion = response.data[0].embedding

    update_tokens(response.usage.total_tokens, "embedding")
    return completion


def _cosine_similarity(a, b: list):
    a = _decode_binary_data(a)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def _decode_binary_data(data):
    # Convert binary data to a numpy array of floats
    num_elements = len(data) // 8  # Each float64 is 8 bytes
    decoded_array = np.frombuffer(data, dtype=np.float64, count=num_elements)
    return decoded_array
