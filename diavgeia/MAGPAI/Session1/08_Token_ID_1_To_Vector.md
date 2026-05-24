---
title: Slide 08 - How Token ID 3 Becomes A Vector
tags:
  - magpai
  - session1
  - teleprompter
slide: 08
---

# Slide 08 - How Token ID 3 Becomes A Vector

## Slide Intent

Make the row lookup concrete.

## Say This

Here is the key lookup idea:

```text
Token ID 3 -> E[3]
```

`E` is the embedding matrix.

When the model sees token ID 3, it retrieves row 3 from that matrix.

That row might look like this in the demo:

```text
[0.21, -0.44, 0.78, 0.12]
```

The integer 3 does not contain the meaning of sales. It points to a learned row in the embedding matrix.

## Key Points

- `E` means embedding matrix.
- `E[3]` means row 3.
- The row is the vector.
- The learned row is the useful representation.

## Transition

There is also a useful linear algebra way to understand this same lookup.
