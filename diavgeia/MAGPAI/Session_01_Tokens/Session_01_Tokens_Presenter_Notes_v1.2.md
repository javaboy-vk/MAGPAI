---
title: MAGPAI Session 1 - Tokens - v1.2
aliases:
  - From Sentence to Tokens to Vectors
tags:
  - magpai
  - ai-demos
  - tokenization
  - embeddings
---

# MAGPAI Session 1
## From Sentence to Tokens to Vectors
### How Text Becomes Numbers

---

# Stack Orientation

MAGPAI starts in the AI/ML language layer.

That layer is based on computing, mathematics, data, machine learning, deep learning, linguistics, information theory, and software systems.

Session 1 zooms into the first transformation: text becoming numeric model input.

---

# Big Idea

People read words.

AI models process numbers.

```text
Text → Tokens → IDs → Vectors → Model
```

---

# Starting Sentence

```text
Are MAG sales up in Chicago?
```

This is meaningful to a human as a business question.

It is not yet model input.

---

# Tokenization

```text
"are mag sales up in chicago ?"
        ↓
["are", "mag", "sales", "up", "in", "chicago", "?"]
```

The tokenizer breaks text into known pieces.

---

# Vocabulary Lookup

```text
"are"     → 1
"mag"     → 2
"sales"   → 3
"up"      → 4
"in"      → 5
"chicago" → 6
"?"       → 7
```

Tokens become token IDs.

---

# Embedding Lookup

```text
1 → embedding_table[1]
```

The token ID selects a row in the embedding matrix.

---

# Vector Representation

```text
1 → [0.21, -0.44, 0.78, 0.12]
```

The vector is a numeric pattern.

---

# Linear Algebra View

```text
[0, 1, 0, 0, 0, 0] × E = row 1 of E
```

Embedding lookup is equivalent to one-hot vector times embedding matrix.

---

# Live Demo

```powershell
python -m magpai.tokenization.token_demo
python -m magpai.embeddings.embedding_lookup_linear_algebra_demo
streamlit run src\magpai\tokenization\token_streamlit_app.py
```

---

# Takeaway

A model never sees `sales` as a word.

It sees a numeric pattern represented by a vector.
