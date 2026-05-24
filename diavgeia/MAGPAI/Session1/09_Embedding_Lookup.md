---
title: Slide 09 - Embedding Lookup
tags:
  - magpai
  - session1
  - teleprompter
slide: 09
---

# Slide 09 - Embedding Lookup

## Slide Intent

Introduce the embedding table as the place where IDs become vectors.

## Say This

Now the token IDs become vectors.

An embedding table is like a lookup table where each row contains a vector.

For example:

```text
1 -> vector for "are"
2 -> vector for "MAG"
3 -> vector for "sales"
```

The token ID selects the row. The selected row is the token vector.

That vector is what moves forward into the neural network.

## Key Points

- Embeddings convert IDs into vectors.
- The token ID selects a row.
- The vector is the numeric representation.
- In real models, vectors are learned during training.

## Transition

Before we zoom into the row lookup, we will define what a vector is.

