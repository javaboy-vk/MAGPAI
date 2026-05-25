---
title: Slide 10 - What Is an Embedding?
tags:
  - magpai
  - session1
  - teleprompter
slide: 10
---

# Slide 10 - What Is an Embedding?

## Slide Intent

Introduce the embedding table before using embedding lookup as an operation.

## Say This

An **embedding** is a learned numeric representation of a token.

The model stores these representations in an **embedding table**. You can think of that table as a matrix where each row belongs to one token ID.

A tiny teaching table can look like this:

```text
ID   token      vector row
1    are        [ 0.21, -0.44,  0.78,  0.12]
2    MAG        [ 0.03,  0.91, -0.14,  0.36]
3    sales      [-0.62,  0.18,  0.45, -0.09]
```

Those vector rows are not calculated from the spelling of the word during the demo. They are rows in the embedding table.

In real models, the values are learned during training so that useful relationships become easier for the neural network to process.

## Key Points

- An embedding is a learned numeric representation.
- The embedding table stores one vector row per token ID.
- Token ID 3 selects the row for `sales`.
- The table is learned during training, then used by lookup during inference.

## Transition

Now we can explain embedding lookup as selecting a row from this table.




