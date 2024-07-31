import pandas as pd
from abc import ABC, abstractmethod
from semantic_search import get_embedding, cosine_similarity


class Prophet(ABC):

    @abstractmethod
    def search(self, question: str, df: pd.DataFrame) -> pd.Series:
        pass


class ProphetRandom(Prophet):

    def search(self, question: str, df: pd.DataFrame) -> pd.Series:
        return df.sample(1).iloc[0]


class ProphetSemanticSearch(Prophet):

    def search(self, question: str, df: pd.DataFrame) -> pd.Series:
        qv = get_embedding(question)
        df["similarity"] = df["embedding"].apply(lambda x: cosine_similarity(x, qv))
        return df.sort_values("similarity", ascending=False).head(1).iloc[0]
