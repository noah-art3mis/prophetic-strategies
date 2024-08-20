from sentence_transformers import CrossEncoder
import pandas as pd
import torch


def rerank(
    query: str, documents: pd.DataFrame, top_k: int | None = None
) -> pd.DataFrame:

    # MODEL = "jinaai/jina-reranker-v1-tiny-en"
    # MODEL = "cross-encoder/stsb-distilroberta-base"
    MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

    model = CrossEncoder(
        MODEL,
        default_activation_function=torch.nn.Sigmoid(),
    )

    result = model.rank(
        query=query,
        documents=documents["content"].tolist(),
        top_k=top_k if top_k else len(documents),
    )

    documents.reset_index(inplace=True)
    for item in result:
        index = item["corpus_id"]
        documents.at[index, "score"] = item["score"]

    documents = documents.sort_values("score", ascending=False)
    return documents
