---
title: Slide 11 - What Is a Vector?
tags:
  - magpai
  - session1
  - teleprompter
slide: 11
---

# Slide 11 - What Is a Vector?

## Slide Intent

Define vector before relying on vector language in the row lookup explanation.

## Say This

A **vector** is a list of numbers.

For this session, think of a vector as the numeric form of a token that the neural network can compute with.

For the word `sales`, the demo uses this lookup path:

```text
1. Token: "sales"
2. Vocabulary lookup: "sales" -> 3
3. Embedding lookup: E[3]
4. Output vector: [-0.62, 0.18, 0.45, -0.09]
```

The important point is that the vector is not the token ID. The token ID is only the row number. The vector is the row content.

## Key Points

- A vector is a list of numbers.
- A token ID is an index.
- The embedding table row is the vector.
- The vector is what moves forward into the neural network.

## Transition

Now we can zoom into Token ID 3 and show exactly how it becomes the `sales` vector.


