---
title: Slide 12 - Demo Cue - Embedding Linear Algebra
tags:
  - magpai
  - session1
  - teleprompter
  - live-demo
slide: 12
---

# Slide 12 - Demo Cue - Embedding Linear Algebra

## Slide Intent

Cue the command-line demo that proves lookup and one-hot multiplication return the same vector.

## Shared Screen

VS Code terminal at the repository root.

## Command

```powershell
$env:PYTHONPATH="src"
python -m magpai.embeddings.embedding_lookup_linear_algebra_demo
```

## Say This Before Running

This demo focuses on one token ID and one embedding matrix.

It shows the same vector produced two ways: direct lookup and one-hot matrix multiplication.

## Point At These Output Blocks

- `Embedding table shape`: vocabulary size by embedding dimension.
- `Token ID`: the row we are selecting.
- `Lookup form`: direct row retrieval.
- `One-hot form`: one active position.
- `One-hot vector x embedding matrix`: matrix multiplication version.
- `Are both methods equal?`: confirms both methods return the same result.

## Say This After Running

This is why I can describe embedding lookup in two ways.

Operationally, the framework performs an efficient lookup.

Conceptually, the lookup is equivalent to selecting a row through matrix multiplication.

## Transition

Now I will show the end-to-end business question becoming a chart-backed answer.
