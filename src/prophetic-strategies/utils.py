import time
from typing import Generator
from Prophet import Prophet, ProphetRandom, ProphetSemanticSearch


def fake_stream(sentence: str) -> Generator[str, None, None]:
    for word in sentence.split(" "):
        yield word + " "
        time.sleep(0.05)


def find_prophet(strategy: str) -> Prophet:
    match strategy:
        case "Oracle":
            return ProphetRandom()
        case "Navigator":
            return ProphetSemanticSearch()
        case _:
            raise ValueError(f"Invalid strategy: {strategy}")
