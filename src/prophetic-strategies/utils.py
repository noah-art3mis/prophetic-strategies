import time
from typing import Generator
from Prophet import (
    Prophet,
    ProphetRandom,
    ProphetSemanticSearch,
    ProphetSemanticWithRerank,
)


def fake_stream(sentence: str) -> Generator[str, None, None]:
    for word in sentence.split(" "):
        yield word + " "
        time.sleep(0.05)


def find_prophet(strategy: str) -> Prophet:
    match strategy:
        case "Dancer":
            return ProphetRandom()
        case "Oracle":
            return ProphetSemanticSearch()
        case "Navigator":
            return ProphetSemanticWithRerank()
        case _:
            raise ValueError(f"Invalid strategy: {strategy}")
