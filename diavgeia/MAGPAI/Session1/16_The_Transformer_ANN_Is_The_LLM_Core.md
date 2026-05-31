---
title: Slide 16 - The Transformer ANN Is the LLM Core
tags:
  - magpai
  - session1
  - teleprompter
slide: 16
---

# Slide 16 - The Transformer ANN Is the LLM Core

## Slide Intent

Explain that a modern LLM is a very large neural network, usually built with the Transformer architecture.

## Say This

In modern LLMs, the ANN and the LLM are not two separate systems.

The LLM **is** an enormous artificial neural network.

More specifically, most modern language models use a neural-network architecture called a **Transformer**.

Inside that Transformer are neural-network components:

```text
attention layers
feed-forward neural networks
residual connections
normalization layers
massive learned weight matrices
```

The embedding layer and the Transformer layers are part of one giant model.

The embedding vectors flow into the Transformer. The Transformer mixes information between token positions, computes relationships, builds contextual meaning, and predicts likely next tokens.

The model learns these relationships statistically from large amounts of training data.

No human explicitly programs these relationships.

The network discovers them during training.


A useful distinction is:

```text
Learned knowledge      -> weights
Current conversation   -> context window
External documents     -> RAG / vector database
Agent state            -> working memory
```

The short version is: embeddings convert language into geometry. The Transformer neural network manipulates that geometry to infer meaning and predict the next token.

## Key Points

- A modern LLM is a very large neural network.
- The Transformer is the neural-network architecture inside the LLM.
- Long-term learned knowledge lives in weights.
- The current prompt lives in the context window.
- Embeddings are the geometry the Transformer starts from.

## Transition

Before we move to tensors, there is one useful linear algebra view of the embedding lookup.

