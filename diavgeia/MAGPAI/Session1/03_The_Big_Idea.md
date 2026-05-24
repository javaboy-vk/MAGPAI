---
title: Slide 03 - The Big Idea
tags:
  - magpai
  - session1
  - teleprompter
slide: 03
---

# Slide 03 - The Big Idea

## Slide Intent

Contrast how people read text with how models receive input.

## Say This

People read words.

We see grammar, context, and meaning. We can look at a sentence and immediately infer what it is probably saying.

When I say **model** here, I mean a **machine-learning model**. More specifically for this session, think of a neural-network language model component.

Easy definition:

```text
A machine-learning model is a learned mathematical function.
It takes numbers as input, computes over them, and produces an output.
```

So the model starts from a different place than we do. It needs a numeric representation before it can compute anything.

That is why this pipeline matters:

```text
Question -> Tokens -> Token IDs -> Vectors -> Neural Network -> Structured Request -> Data Tool -> Chart
```

Each step moves the question away from human-readable text and closer to something the system can execute against trusted data.

## Key Points

- Human view: words, grammar, context, meaning.
- Model view: a learned mathematical function that needs numeric input.
- Tokenization and embeddings bridge language and computation.
- The chart comes from a data tool, not from model memory.

## Transition

Now I will use one simple sentence and carry it through the whole pipeline.

