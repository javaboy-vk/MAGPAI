---
title: Live Demo 01 - Token Pipeline
tags:
  - magpai
  - session1
  - teleprompter
  - live-demo
---

# Live Demo 01 - Token Pipeline

## Slide Intent

Cue the first live demo from the command line.

## Shared Screen

VS Code terminal at the repository root.

## Command

```powershell
$env:PYTHONPATH="src"
python -m magpai.tokenization.token_demo
```

## Say This Before Running

Now I am going to run the same pipeline from the command line.

This is not a black box. The script prints each transformation step so we can see the question moving from text to vectors.

## Point At These Output Blocks

- `Sentence`: original input text.
- `Normalized sentence`: lowercase form.
- `Tokens`: the word-level token list.
- `Token IDs`: vocabulary indexes.
- `Embedding vectors`: numeric rows returned by the embedding layer; this printed table is the token-vector grid we just described as the input tensor.

## Say This After Running

This output is the whole first mental model in one place:

```text
Question text becomes tokens.
Tokens become IDs.
IDs become vectors.
Vectors are stored as an activation tensor.
```

The command line version is useful because it removes visual distractions and shows the data directly.

## Transition

Next I will show the same idea in a more visual form.
