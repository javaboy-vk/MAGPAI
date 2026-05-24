---
title: Slide 08 - Tokenizer Step 2 - Token IDs
tags:
  - magpai
  - session1
  - teleprompter
slide: 08
---

# Slide 08 - Tokenizer Step 2 - Token IDs

## Slide Intent

Explain vocabulary lookup and make clear that token IDs are labels.

## Say This

After tokenization, each token is looked up in a vocabulary.

In this demo vocabulary:

```text
"<PAD>"   -> 0
"are"     -> 1
"MAG"     -> 2
"sales"   -> 3
"up"      -> 4
"in"      -> 5
"chicago" -> 6
"?"       -> 7
```

So the token list:

```text
["are", "MAG", "sales", "up", "in", "chicago", "?"]
```

becomes:

```text
[1, 2, 3, 4, 5, 6, 7]
```

Important point: the integer ID is not the meaning. It is an index.

Token ID 3 does not mathematically mean sales. It points to where the model can find the representation for sales.

## Key Points

- Tokens become token IDs through vocabulary lookup.
- IDs are stable labels.
- IDs are not meaningful quantities by themselves.

## Transition

Before using vectors, we need to define the embedding table that stores them.


