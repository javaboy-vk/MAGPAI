# MAGPAI Session 1 - Speaking Script - v1.2

## Opening

Today we start by locating MAGPAI in the AI/ML stack.

MAGPAI starts in the language layer, where text becomes tokens, token IDs, vectors, tensors, and eventually model input.

That layer is not floating by itself. It is built on computing, mathematics, data, classical machine learning, deep learning, and a set of sciences that include linear algebra, probability, statistics, optimization, information theory, linguistics, and software systems.

After that orientation, we narrow the scope to Session 1: how a simple business question becomes numbers.

## Slide Story

The question is:

```text
Are MAG sales up in Chicago?
```

To us, this is a business question. We understand the company, metric, direction, and location.

But the model cannot process this sentence directly. A neural network needs numeric input.

So the tokenizer starts by preparing the text.

In our demo, we normalize the text:

```text
are mag sales up in chicago ?
```

Then the tokenizer splits the text into tokens:

```text
["are", "mag", "sales", "up", "in", "chicago", "?"]
```

Each token is then looked up in a vocabulary:

```text
are becomes 1
mag becomes 2
sales becomes 3
up becomes 4
in becomes 5
chicago becomes 6
? becomes 7
```

Now the sentence is no longer text. It is a sequence of token IDs:

```text
[1, 2, 3, 4, 5, 6, 7]
```

But these IDs are still only indexes. Token ID 3 does not contain the meaning of sales by itself. It points to row 3 in an embedding table.

That row is a vector:

```text
[0.21, -0.44, 0.78, 0.12]
```

The vector is the numeric representation that enters the neural network.

## Linear Algebra Explanation

At a high level, the embedding table is a matrix. Token ID 3 selects row 3 from that matrix.

Mathematically, we can think of token ID 3 as a one-hot vector:

```text
[0, 0, 0, 1, 0, 0, 0, 0]
```

When this one-hot vector is multiplied by the embedding matrix, it selects row 3.

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
