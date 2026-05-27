---
title: Slide 15 - Linear Algebra View
tags:
  - magpai
  - session1
  - teleprompter
slide: 15
---

# Slide 15 - Linear Algebra View

## Slide Intent

Connect embedding lookup to one-hot matrix multiplication.

## Say This

Embedding lookup can also be explained as a linear algebra operation.

Token ID 3 can be represented as a one-hot vector:

```text
[0, 0, 0, 1, 0, 0, 0, 0]
```

If we multiply that one-hot vector by the embedding matrix `E`, it selects row 3:

```text
[0, 0, 0, 1, 0, 0, 0, 0] x E = [-0.62, 0.18, 0.45, -0.09]
```

In real code, frameworks usually skip the one-hot vector because it is inefficient. They directly retrieve the row.

But conceptually, this view helps us connect the lookup to matrix multiplication.

## Key Points

- One-hot vector has one active position.
- Multiplying by `E` selects the matching row.
- Direct lookup is faster in real code.
- The result is the same vector.

## Transition

Now we can explain what reaches the neural network before switching to code.





