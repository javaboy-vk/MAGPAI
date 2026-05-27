---
title: Slide 17 - Prompt Stored as an Input Tensor
tags:
  - magpai
  - session1
  - teleprompter
slide: 17
---

# Slide 17 - Prompt Stored as an Input Tensor

## Slide Intent

Show how the original prompt is stored as a token-vector tensor before neural-network layers run.

## Say This

Now connect the original prompt to the actual neural-network input.

The input text was:

```text
are MAG sales up in chicago?
```

After tokenization, ID lookup, and embedding lookup, the framework stores one vector row per token position.

Visually, that looks like a grid:

```text
token      v1      v2      v3      v4
are        0.21   -0.44    0.78    0.12
MAG        0.03    0.91   -0.14    0.36
sales     -0.62    0.18    0.45   -0.09
up        -0.31    0.67    0.11    0.28
in         0.08   -0.15    0.22    0.64
chicago    0.41    0.12   -0.33    0.57
?         -0.07    0.04    0.19   -0.22
```

This is the activation tensor for the prompt:

```text
shape = [7 token positions, 4 vector dimensions]
```

The neural network layers start from this tensor. They do not receive the raw sentence, and they do not receive the token IDs as the main representation. They receive the vector grid.

This is the clean starting point for Session 2: how a neural-network layer transforms that tensor.

## Key Points

- The original prompt becomes a grid of numbers.
- Each row is one token position.
- Each column is one vector dimension.
- The NN starts from this activation tensor.
- Session 2 begins with layer computation over this tensor.

## Transition

Now we will look at the full question-to-insight flow as one dashboard view.





