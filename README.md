# Prophetic Strategies

Semantic search through Lacan's Seminar Book 5. Access [here](https://prophetic.streamlit.app/).

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
```

## Findings

-   sentence-transformers interacts unfavourably with streamlit.
-   Anecdotally, more examples make the model respond in more diverse ways.
