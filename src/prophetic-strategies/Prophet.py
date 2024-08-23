import pandas as pd
from abc import ABC, abstractmethod
from semantic_search import get_embedding, cosine_similarity
from cross_encoding import rerank


class Prophet(ABC):

    @abstractmethod
    def search(
        self, question: str, df: pd.DataFrame, top_k: int | None, iterations: int = 1
    ) -> str:
        pass


class ProphetRandom(Prophet):

    def search(
        self, question: str, df: pd.DataFrame, top_k: int | None, iterations: int = 1
    ) -> str:
        
        results = df.sample(iterations)
        result = " ".join(results["content"])
        return result


class ProphetRandom2(Prophet):

    def search(
        self, question: str, df: pd.DataFrame, top_k: int | None, iterations: int = 1
    ) -> str:

        sample = df.sample(1)
        result = sample["content"]
        sample_index = df["sentence"]

        for i in range(iterations):
            result += df.loc[df["sentence"] == sample_index + i, "content"]

        return result


class ProphetSemanticSearch(Prophet):

    def search(
        self, question: str, df: pd.DataFrame, top_k: int | None, iterations: int = 1
    ) -> pd.DataFrame:
        qv = get_embedding(question)
        df["similarity"] = df["embedding"].apply(lambda x: cosine_similarity(x, qv))
        df = df.drop("embedding", axis=1)
        df = df.sort_values("similarity", ascending=False)
        df = df.head(top_k if top_k is not None else df.shape[0])
        return df


class ProphetSemanticWithRerank(ProphetSemanticSearch):

    def search(
        self, question: str, df: pd.DataFrame, top_k: int | None, iterations: int = 1
    ) -> pd.DataFrame:
        unranked = super().search(question, df, top_k)
        reranked = rerank(question, unranked, top_k)
        return reranked
