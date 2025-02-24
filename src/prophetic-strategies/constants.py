STRATEGIES = [
    {
        "name": "Oracular",
        "description": "Semantic search (SS) using `text-embedding-3-small`",
    },
    {
        "name": "Ficticious",
        "description": "SS + `gpt4o-mini` finetuned with `3171` sentences",
    },
    {
        "name": "Fallacious",
        "description": "SS + `gpt4o` finetuned with `3171` sentences",
    },
    # {"name": "Erratic", "description": "Mystery sampling"},
    {"name": "Mercurial", "description": "Mystery strategy"},
]


ALLOWED_BASE_MODELS = [
    {
        "model": "gpt-4o-2024-08-06",
        "input_cost": 2.5 / 1_000_000,
        "output_cost": 10.0 / 1_000_000,
    },
    {
        "model": "gpt-4o-mini-2024-07-18",
        "input_cost": 0.15 / 1_000_000,
        "output_cost": 0.60 / 1_000_000,
    },
    {
        "model": "claude-3-haiku-20240307",
        "input_cost": 0.25 / 1_000_000,
        "output_cost": 1.25 / 1_000_000,
    },
    {"model": "llama3", "input_cost": 0.0, "output_cost": 0.0},
    # case minilm
    # case embedding openai
    # case generative local
    # cae reranker
]

REFERENCE_PROMPT = """Come up with a title for a book or article this text might belong to. Don't be too obvious; use a mysterious name like those below. The title should have a similar style to the examples. 

###

Text:

{{SNIPPET}}

###

Examples:

- On My Antecedents
- Beyond the _Reality Principle_
- The Mirror Stage as Formative of the _I_ Function as Revealed in Psychoanalytic Experience
- Aggressiveness in Psychoanalysis
- A Theoretical Introduction to the Functions of Psychoanalysis in Criminology
- Presentation on Psychical Causality
- Logical Time and the Assertion of Anticipated Certainty
- Presentation on Transference
- On the Subject Who Is Finally in Question
- The Function and Field of Speech and Language in Psychoanalysis
- Variations on the Standard Treatment
- On a Purpose
- Introduction to Jean Hyppolite's Commentary on Freud's _Verneinung_
- Response to Jean Hyppolite's Commentary on Freud's _Verneinung_
- The Freudian Thing, or the Meaning of the Return to Freud in Psychoanalysis
- Psychoanalysis and Its Teaching
- The Situation of Psychoanalysis and the Training of Psychoanalysts in 1956
- The Instance of the Letter in the Unconscious, or Reason Since Freud
- On a Question Prior to Any Possible Treatment of Psychosis
- The Direction of the Treatment and the Principles of Its Power
- Remarks on Daniel Lagache's Presentation: _Psychoanalysis and Personality_
- The Signification of the Phallus
- In Memory of Ernest Jones: On His Theory of Symbolism
- On an Ex Post Facto Syllabary
- Guiding Remarks for a Convention on Female Sexuality
- The Youth of Gide, or the Letter and Desire
- Kant with Sade
- The Subversion of the Subject and the Dialectic of Desire in the Freudian Unconscious
- Position of the Unconscious
- On Freud's _Trieb_ and the Psychoanalyst's Desire
- Science and Truth
- Freud's Papers on Technique
- The Ego in Freud's Theory and in the Technique of Psychoanalysis
- The Psychoses
- The Object Relation
- The Formations of the Unconscious 
- Desire and Its Interpretation
- The Ethics of Psychoanalysis
- Transference
- Identification
- Anxiety 
- The Names of the Father
- The Four Fundamental Concepts of Psychoanalysis
- Problèmes cruciaux pour la psychanalyse
- L'objet de la psychanalyse
- La logique du fantasme
- L'acte psychanalytique
- From an Other to the other
- The Other Side of Psychoanalysis 
- On a Discourse that Might Not be a Semblance
- ...or Worse
- Encore, On Feminine Sexuality: The Limits of Love and Knowledge
- Les non-dupes errent
- The Sinthome
- L'insu que sait de l'une-bévue s'aile à mourre
- Le moment de conclure
- La topologie et le temps
- Dissolution

###

Respond exclusively with the title and nothing else."""