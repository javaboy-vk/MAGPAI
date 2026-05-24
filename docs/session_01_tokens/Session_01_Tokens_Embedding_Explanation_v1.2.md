# MAGPAI Session 1 - Embedding Lookup and Linear Algebra - v1.2

## Core Explanation

A token ID does not calculate a vector by itself.

A token ID is an index into an embedding table.

```text
Token ID 3 -> embedding_table[3]
```

If row 3 of the embedding table is:

```text
[0.21, -0.44, 0.78, 0.12]
```

then token ID 3 returns that vector.

## Embedding Matrix

The embedding table is a matrix:

```text
E in R^(V x D)
```

Where:

```text
V = vocabulary size
D = embedding dimension
```

For the demo:

```text
V = 8
D = 4
E in R^(8 x 4)
```

Conceptually:

```text
Token ID     Vector
----------------------------------------
0            [ ... ]
1            [ ... ]
2            [ ... ]
3            [ 0.21, -0.44,  0.78,  0.12]
4            [ ... ]
5            [ ... ]
6            [ ... ]
7            [ ... ]
```

## One-Hot Linear Algebra View

Token ID 3 can also be represented as a one-hot vector:

```text
[0, 0, 0, 1, 0, 0, 0, 0]
```

Then:

```text
[0, 0, 0, 1, 0, 0, 0, 0] x E = row 3 of E
```

That multiplication returns:

```text
[0.21, -0.44, 0.78, 0.12]
```

In real code, frameworks avoid creating the one-hot vector because it is inefficient. They directly index the embedding matrix:

```python
vector = embedding.weight[token_id]
```

## Why Four Numbers?

The demo uses `embedding_dim = 4` so each token is represented by four numeric coordinates.

```text
sales -> [x1, x2, x3, x4]
```

In real models, the embedding dimension may be hundreds or thousands of numbers. The idea is the same: each token becomes a point in a high-dimensional vector space.

## Speaker-Friendly Summary

Token ID 3 points to row 3 in the embedding matrix. The row contains the learned vector for that token. During training, the model adjusts these vector values so they become useful for prediction.
