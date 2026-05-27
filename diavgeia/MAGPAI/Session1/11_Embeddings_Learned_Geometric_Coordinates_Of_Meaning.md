---
title: Slide 11 - Embeddings: Learned Geometric Coordinates of Meaning
tags:
  - magpai
  - session1
  - teleprompter
slide: 11
---

# Slide 11 - Embeddings: Learned Geometric Coordinates of Meaning

## Slide Intent

Explain that embeddings do not start meaningful. They become meaningful because training moves vectors into useful geometric positions.

## Say This

Initially, the embedding rows are just random numbers.

```text
MAG     = [random garbage]
sales   = [random garbage]
Chicago = [random garbage]
```

At that stage, the geometry does not mean anything yet.

During training, the model repeatedly sees language patterns like:

```text
sales up
sales increased
revenue growth
Chicago region
```

Backpropagation gradually adjusts the vector values. Words that appear in related contexts are moved closer together. Words that do not belong together are pushed farther apart.

Eventually:

- similar words move closer together
- unrelated words move apart
- the geometry itself starts to store meaning

## Visual Intuition

Imagine a tiny 3D world:

| Word | Coordinates |
|---|---:|
| king | (2, 9, 4) |
| queen | (2, 9, 5) |
| man | (1, 4, 3) |
| woman | (1, 4, 4) |

The distances encode relationships.

This is why famous analogies can work:

```text
king - man + woman ~= queen
```

The vectors capture semantic structure.

## Sentence Embeddings

Individual token vectors are then combined.

Methods include:

- averaging
- attention
- transformers
- pooling

So:

```text
"MAG sales are up in Chicago"
```

can become one giant vector:

```text
[0.192, -0.551, 0.882, ... 1536 dimensions ...]
```

That vector captures business context, upward trend, location, and organizational semantics.

## Why This Works

Language has statistical structure.

Words appearing in similar contexts tend to have related meanings.

The embedding algorithm learns:

```text
context patterns -> geometric relationships
```

This is one of the foundational ideas behind Word2Vec, GloVe, BERT, GPT, and modern LLMs.

## Key Points

- Embeddings start as random parameters.
- Training moves vectors based on repeated context patterns.
- Semantic relationships become geometric relationships.
- Sentence embeddings combine token vectors into one larger representation.

## Transition

Now that the geometry has meaning, we can return to the lookup operation and show how token IDs retrieve those learned rows.
