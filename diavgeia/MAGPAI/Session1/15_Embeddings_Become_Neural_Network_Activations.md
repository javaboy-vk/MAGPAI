---
title: Slide 15 - Embeddings Become Neural-Network Activations
tags:
  - magpai
  - session1
  - teleprompter
slide: 15
---

# Slide 15 - Embeddings Become Neural-Network Activations

## Slide Intent

Clarify that embeddings are not handed to a separate AI system. They become the live numeric input flowing into the neural network.

## Say This

This is the key connection point.

After tokenization and embedding lookup, the model has vectors:

```text
are      -> [0.12, -0.44, ...]
sales    -> [0.91,  0.08, ...]
chicago  -> [-0.33, 0.77, ...]
```

Those vectors are not a report that gets passed to some separate AI engine.

They become the **input activations** of the neural network.

In other words, the live data flowing through the model starts as the embedding vectors for this prompt.

For the MAGPAI mental model:

```text
Text -> Tokenizer -> Token IDs -> Embeddings -> Neural Network -> Output
```

The words are gone by this point. The model is operating on numeric geometry.

## Key Points

- Embeddings are vectors.
- The vectors become input activations.
- The neural network starts from those activation values.
- There is not usually a separate ANN that hands data to the LLM.

## Transition

Now we can name the kind of neural network used inside modern LLMs.

