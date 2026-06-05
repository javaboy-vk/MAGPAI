---
title: Slide 18 - What Is a Tensor?
tags:
  - magpai
  - session1
  - teleprompter
slide: 18
---

# Slide 18 - What Is a Tensor?


## Say This

A **tensor** is the framework's in-memory numeric container, is a multi-dimensional array of numbers.

The simple way to build the idea is:

```text
vector = 1-D list of numbers
matrix = 2-D table of numbers
tensor = 3D+ tensor = stacked matrices / higher-dimensional arrays
```

For our prompt, each token has one vector. If the prompt has 7 tokens and each token vector has 4 numbers, the input can be stored with this shape:

```text
[7 token positions, 4 vector dimensions]
```

That stored object is an **activation tensor** because it is not model weights. 
It is the live numeric data flowing through the neural network for this specific input.

For a batch of many prompts, the shape adds a batch dimension:

```text
[batch size, number of tokens, vector size]
```

The important mental model is: **the words are gone by this point**. 
The neural network starts from numbers stored in a tensor.

## Transition

Now we will show the original prompt visually as the tensor the NN receives.


## Key Points

- A tensor is a numeric container with shape.
- A vector is a simple 1-D tensor.
- A prompt becomes a 2-D token-vector tensor.
- An activation tensor stores the live input data before a layer processes it.




