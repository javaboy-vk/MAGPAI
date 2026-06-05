---
title: Talking Point 16.A - Why LLMs Are Called Language Models
tags:
  - magpai
  - session1
  - teleprompter
  - talking-point
slide: "16.A"
---

# Talking Point 16.A - Why LLMs Are Called Language Models

## Talking Point Intent

Explain why modern LLMs are called **language models** even though they are implemented as very large artificial neural networks.

## Opening Question

As an LLM is a large ANN, why do we call them language models and not large artificial neural networks?

Technically, modern LLMs **are** very large artificial neural networks.

The reason we call them **Language Models** instead of **Large Artificial Neural Networks** 
is that the name emphasizes their **purpose**, not their implementation.

## Purpose Versus Implementation

Think of it this way:

| Term | Focus |
|---|---|
| Artificial Neural Network (ANN) | The architecture |
| Language Model (LM) | The function |
| Large Language Model (LLM) | A very large ANN trained to model language |

## Useful Analogy

```text
Engine = ANN
Car    = Language Model
```

You do not usually say:

```text
I am driving a V8 engine.
```

You say:

```text
I am driving a car.
```

The engine is what powers it.

The car is what it does.



## Language Models Also Have A Long History

Language Models existed independently of modern deep-learning systems.

Examples include:

- Statistical language models

These systems attempted to predict the next word in a sequence.

They were Language Models even though they were not neural networks.

## The Convergence

For many years, ANNs and Language Models were separate research areas.

Eventually researchers combined them:

```text
Language Modeling
        +
Artificial Neural Networks
        =
Neural Language Models
```

Then, with larger datasets and more compute:

```text
Neural Language Models
        +
Transformers
        +
Billions of Parameters
        =
Large Language Models (LLMs)
```

## The Convergence Of Two Fields

```text
Field 1:
Artificial Neural Networks
(1950s -> Present)

Field 2:
Language Models
(1980s/1990s -> Present)

            |
            v

Neural Language Models
            |
            v

Transformers
            |
            v

Large Language Models
```

## Key Insight

LLMs did not evolve solely from ANNs, nor solely from Language Models.

They emerged when the ANN field and the Language Modeling field converged into a single architecture.


## What Is a Language Model?

A language model tries to learn:

> "Given some text, what text is most likely to come next?"

For example:

```text
The capital of France is ...
```

The model predicts:

```text
Paris
```

Mathematically, it learns probabilities

This objective defines a language model.

The ANN is simply the machinery used to learn that probability distribution.


## Why "Large"?

When researchers began using enormous neural networks with billions of parameters, the term became:

```text
Large Language Model
```

because it is:

- Large
- A language model
- Implemented using neural networks

## From ANN To LLM

A modern LLM is essentially:

```text
Tokens   are the small pieces of text that an AI model actually reads.
   |
   v
Embeddings  are numerical vectors that represent the meaning of tokens.
   |
   v
Transformer Layers  are the main processing layers of a modern language model.
   |
   v
Attention  Attention is the mechanism that lets the model decide which tokens should pay attention to which other tokens.
   |
   v
Feed Forward Networks are NN blocks inside each transformer layer that further process and transform the token vectors.
   |
   v
Output Probabilities are the model’s final prediction scores for possible next tokens or answers.
```

Notice something important:
The transformer itself is composed of neural network layers.
So inside an LLM there are actually many ANNs.
Everything inside is neural-network mathematics.

## Transformer
Each transformer layer takes the embedding vectors and repeatedly refines them.
At the beginning, the vector for sales mostly represents the token itself.
After passing through transformer layers, the vector for sales becomes context-aware.

For example, in: Are MAG sales up in Chicago?
the model learns that sales is related to:

MAG
up
Chicago
business performance
a question being asked

So transformer layers turn isolated token vectors into contextual meaning.

## Attention

Attention helps the model understand relationships between words.

In the sentence:

Are MAG sales up in Chicago?

the token sales should strongly pay attention to:

MAG
up
Chicago
?

because those tokens help define what kind of sales, what direction, what location, and whether this is a question.

## Feed Forward Networks
After attention finds relationships between tokens, the feed forward network applies learned patterns to each token representation.

It helps the model recognize things like:

This is a sales question.
This involves a location.
This asks about trend direction.
This may require data lookup or analysis.

For MAGPAI, this is where the model starts moving from raw text meaning toward useful interpretation.


## Output probabilities
The model does not directly “choose a word” the way a human does.

Instead, it calculates probabilities.

For example, after reading:

MAG sales are

the model may assign probabilities like:

up      62%
down    21%
flat    12%
unknown  5%

The model then selects an output based on those probabilities.

For MAGPAI, output probabilities can represent possible answers, actions, or next steps.

In **MAGPAI**, text becomes tokens, tokens become vectors, vectors move through transformer layers, attention finds relationships, feed forward networks transform meaning, and the model produces probabilities for what to answer or do next.


## Is The ANN The "Brain"?

For modern LLMs:

```text
Yes.
```

More precisely:

- The ANN stores the learned knowledge in its weights.
- The Transformer architecture organizes how information flows.
- The Language Model objective determines what it learns.

You can think of an LLM as:

```text
LLM
=
Transformer ANN
+
Language Training
+
Huge Dataset
+
Billions of Parameters
```

or:

```text
LLM = ANN specialized for language
```


> "The LLM is the application. The ANN is the engine inside it."

That distinction is why the industry settled on **LLM** rather than **Large ANN**, even though 
under the hood a modern LLM is fundamentally a very large neural network.

