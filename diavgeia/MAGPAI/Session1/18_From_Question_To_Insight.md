---
title: Slide 18 - From Question to Insight
tags:
  - magpai
  - session1
  - teleprompter
slide: 18
---

# Slide 18 - From Question to Insight

## Slide Intent

Show the full MAGPAI flow as one end-to-end visual before switching to live demos.

## Visual

![[magpai_from_question_to_insight.png]]

## Say This

This view puts the whole session together.

The original question moves through the same sequence we have been building:

```text
Input -> Tokens -> Token IDs -> Embedding Vectors -> Tiny Neural Network -> Output
```

For the teaching example, the important corrected values are:

```text
Token IDs: [1, 2, 3, 4, 5, 6, 7]
Embedding shape: 7 tokens x 4 dimensions
Neural-network input: 7 x 4
Sales trend: 25.0%
```

The point of the slide is not that this tiny neural network is production-grade. The point is that each step is inspectable.

## Key Points

- The prompt becomes tokens and token IDs.
- Token IDs select embedding rows.
- The embedding rows form the input tensor.
- The tiny NN consumes the tensor and produces an output path.
- The final answer is backed by data and a chart.

## Transition

Now I will switch from the walkthrough to code and show the pipeline running.




