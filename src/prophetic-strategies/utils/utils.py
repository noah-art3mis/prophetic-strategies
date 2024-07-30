import time
from typing import Generator


def fake_stream(sentence: str) -> Generator[str, None, None]:
    for word in sentence.split(" "):
        yield word + " "
        time.sleep(0.05)


# def get_random_sentence_from_db(db: Path) -> dict:
#     # requires table to have same name as db file
#     table = os.path.basename(db).replace(".db", "")
#     with sqlite3.connect(db) as conn:
#         cur = conn.cursor()
#         cur.execute(
#             f"""SELECT * FROM {table} ORDER BY RANDOM() LIMIT 1"""
#         )  # sql injection?
#         row = cur.fetchone()
#         cur.close()

#         sentence = {
#             "book": row[0],
#             "sentence": row[1],
#             "chapter": row[2],
#             "sentence_chapter": row[3],
#             "content": row[4],
#             "embedding": row[5],
#         }

#         return sentence
