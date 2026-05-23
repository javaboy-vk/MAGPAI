# MAGPAI Session 1 - Speaking Script - v1.2

## Opening

Today we start at the beginning of a language model. Before transformers, attention, training, or inference, the first thing we need to understand is how text becomes numbers.

## Slide Story

The sentence is:

```text
Sales are up in Chicago
```

To us, this is a business statement. We understand that sales increased, and we understand the location is Chicago.

But the model cannot process this sentence directly. A neural network needs numeric input.

So the tokenizer starts by preparing the text.

In our demo, we normalize the text to lowercase:

```text
sales are up in chicago
```

Then the tokenizer splits the text into tokens:

```text
["sales", "are", "up", "in", "chicago"]
```

Each token is then looked up in a vocabulary:

```text
sales becomes 1
are becomes 2
up becomes 3
in becomes 4
chicago becomes 5
```

Now the sentence is no longer text. It is a sequence of token IDs:

```text
[1, 2, 3, 4, 5]
```

But these IDs are still only indexes. Token ID 1 does not contain the meaning of sales by itself. It points to row 1 in an embedding table.

That row is a vector:

```text
[0.21, -0.44, 0.78, 0.12]
```

The vector is the numeric representation that enters the neural network.

## Linear Algebra Explanation

At a high level, the embedding table is a matrix. Token ID 1 selects row 1 from that matrix.

Mathematically, we can think of token ID 1 as this one-hot vector:

```text
[0, 1, 0, 0, 0, 0]
```

When this one-hot vector is multiplied by the embedding matrix, it selects row 1.

So embedding lookup is both a simple table lookup and a linear algebra operation.

## Closing

The first MAGPAI mental model is:

```text
Text becomes tokens.
Tokens become IDs.
IDs become vectors.
Vectors become model input.
```

A model never sees `sales` as a word. It sees a numeric pattern.
