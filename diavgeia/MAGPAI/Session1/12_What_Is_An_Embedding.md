---
title: Slide 12 - What Is an Embedding?
tags:
  - magpai
  - session1
  - teleprompter
slide: 12
---

# Slide 12 - What Is an Embedding?



## Say This

Now we can name the structure behind that vector lookup.

An **embedding** is a learned numeric representation of a token.

The model stores these representations in an **embedding table**. You can think of that table as a matrix where each row belongs to one token ID.

A tiny table can look like this:

```text
ID   token      vector row
1    are        [ 0.21, -0.44,  0.78,  0.12]
2    MAG        [ 0.03,  0.91, -0.14,  0.36]
3    sales      [-0.62,  0.18,  0.45, -0.09]
```

Those vector rows are not calculated from the spelling of the word during the demo. They are rows in the embedding table.

In real models, the values are learned during training so that useful relationships become easier for the neural network to process.

**Why Floating Point Numbers?**

- Integers cannot express semantic distance well.
- Floating point numbers allow:
smooth learning
partial similarity
geometric relationships

- Neural networks operate using:
matrix multiplication
linear algebra
gradients
optimization


**How can tokens become floating points parts of a vector?**
- No magic conversion exists.
- They are learned parameters.

The vector is simiply:
- initialized randomly
- adjusted during training millions or billions of times

A token vector is not stored as plain text. It becomes a list of numbers. In real AI systems, these numbers are floating-point values. They may look like they have many decimals, but internally the system usually stores them in formats like 32-bit (7 decimals), or 16-bit (3 decimals). The exact number of decimals is less important than the fact that the model learns by changing these numbers.

We see that AI is powered by floating-point math.
CPUs can do that math, but GPUs can do it massively in parallel.
And modern NVIDIA GPUs go even further with specialized hardware called Tensor Cores, designed to accelerate the mixed-precision matrix operations used in AI.

This is one of the main reasons NVIDIA became so central to the AI revolution.



## Key Points

- An embedding is a learned numeric representation.
- The embedding table stores one vector row per token ID.
- Token ID 3 selects the row for `sales`.
- The table is learned during training, then used by lookup during inference.

## Transition

Now we can explain how training makes those rows become geometric coordinates of meaning.




