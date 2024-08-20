from sentence_transformers import SentenceTransformer
import sqlite3
from pathlib import Path
import pandas as pd
import numpy as np


def similarity_minilm(question):
    DATABASE = Path("../../db/book5.db")
    TABLE_NAME = "book5"
    model = SentenceTransformer("all-MiniLM-L6-v2")

    qv = model.encode(question)
    df = get_wv(DATABASE, TABLE_NAME)
    similarities = model.wv.similarity([qv], df["embedding_minilm"].tolist())
    df["similarity"] = similarities


def get_wv(db: Path, table_name: str) -> pd.DataFrame:
    with sqlite3.connect(db) as conn:
        rows = pd.read_sql(f"""SELECT * FROM {table_name}""", conn)
        return rows
