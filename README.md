# Prophetic Strategies

Semantic search through Lacan's Seminar Book 5. Access [here](https://prophetic.streamlit.app/).

## Configuration

Strategies:

| Name              | Description                                         |
| ----------------- | --------------------------------------------------- |
| Oracle            | Semantic search (SS) using `text-embedding-3-small` |
| Ficticious        | SS + `gpt4o-mini` finetuned with `50` sentences     |
| Fallacious        | SS + `gpt4o-mini` finetuned with `500` sentences    |
| Quixotic          | SS + `gpt4o-mini` finetuned with `3171` sentences   |
| Spectral          | SS + `gpt4o` finetuned with `50` sentences          |
| Chimerical        | SS + `gpt4o` finetuned with `500` sentences         |
| Apocryphal        | SS + `gpt4o` finetuned with `3171` sentences        |
| Dancer            | Mystery sampling                                    |
| Erratic/Mercurial | Mystery strategy                                    |

models = `Oracle`

captions = [
"Semantic search (SS) using `text-embedding-3-small`.",
]

"ft:gpt-4o-mini-2024-07-18:personal:book5-prev-50:9zNUM8u9"
"ft:gpt-4o-mini-2024-07-18:personal:book5-prev-500:9zNj1EM1"
"ft:gpt-4o-mini-2024-07-18:personal:book5-prev-5000:9zOZlylK"
"ft:gpt-4o-2024-08-06:personal:book5-prev-50:9zNl1D6V"
"ft:gpt-4o-2024-08-06:personal:book5-prev-500:9zNzD7P1"
"ft:gpt-4o-2024-08-06:personal:book5-prev-5000:9zPWBSz9"

## Data model

```yaml
- db: book5
  table: book5
  columns:
      - book: 'Book V - The Formations of the Unconscious (1957–1958)'
      - sentence: 898
      - chapter: 7
      - sentence_chapter: 30
      - content: "We have expressed this by placing a rough breathing in parenthesis in α' φ', namely that the Other homologates it as such, homologates it as message, authenticates it as a joke."
      - embedding: { ... }
      - embedding_minilm: { ... }
```
