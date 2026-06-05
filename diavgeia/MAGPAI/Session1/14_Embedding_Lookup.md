---
title: Slide 14 - Embedding Lookup
tags:
  - magpai
  - session1
  - teleprompter
slide: 14
---

# Slide 14 - Embedding Lookup

## Slide Intent

Introduce the embedding table as the place where IDs become vectors.

## Say This

Now we can put the pieces together: token IDs retrieve vectors from the embedding table.

An embedding table is like a lookup table where each row contains a vector.

For example:

```text
1 -> vector for "are"
2 -> vector for "MAG"
3 -> vector for "sales"
```

The token ID selects the row. The selected row is the token vector.

Now that we know what Vectors and Embeddings are we can understand the first of the two trainings
of a foundational model: training the vocabulary.
We briefly mentioned earlier about creating vocabularies of tokens.


## Transition

Now that token IDs retrieve embedding vectors, we can explain what the neural network 
actually receives.

That vector is what moves forward into the neural network and are learned during the second kind
of training: NN training.

## Key Points

- Embeddings convert IDs into vectors.
- The token ID selects a row.
- The vector is the numeric representation.
- In real models, vectors are learned during training.







