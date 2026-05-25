# MAGPAI Session 1 - Slide Story - v1.2

## Theme

How a Business Question Becomes a Data-Backed Answer

## Opening Orientation

MAGPAI Session 1 starts by locating the demo inside the AI/ML stack.

The first stack view shows where MAGPAI starts: the language layer, where text becomes tokens, token IDs, vectors, tensors, and model input.

The second stack view shows what the layers are based on: mathematics, computer science, engineering, linguistics, information theory, statistics, optimization, risk science, and related disciplines.

That orientation prepares the audience for the main Session 1 story: a business question becoming numeric model input and then a chart-backed answer.

## Human Question

```text
Are MAG sales up in Chicago?
```

A human immediately sees a business question. The words suggest a company, metric, trend direction, and location.

A neural network does not start with that meaning. It cannot process raw English words directly. It needs numbers.

## Transformation

```text
"Are MAG sales up in Chicago?"
        ->
Normalize text
        ->
"are mag sales up in chicago ?"
        ->
Tokenize
        ->
["are", "mag", "sales", "up", "in", "chicago", "?"]
        ->
Vocabulary lookup
        ->
[1, 2, 3, 4, 5, 6, 7]
        ->
Embedding lookup
        ->
Numeric vectors
        ->
Structured request
        ->
Data lookup and chart-backed answer
```

## Tokenizer Boundary

The tokenizer performs this part:

```text
Text -> Tokens -> Token IDs
```

In the MAGPAI teaching demo, tokenization is deliberately simple:

```python
tokens = sentence.lower().replace("?", " ?").split()
```

This produces word-level tokens plus a question-mark token:

```text
["are", "mag", "sales", "up", "in", "chicago", "?"]
```

A real LLM tokenizer may split text into whole words, subwords, spaces, punctuation, and special tokens. The simplified demo teaches the concept before introducing production tokenizer complexity.

## Vocabulary Lookup

```text
"are"     -> 1
"mag"     -> 2
"sales"   -> 3
"up"      -> 4
"in"      -> 5
"chicago" -> 6
"?"       -> 7
```

The token IDs are arbitrary labels. They are not meaningful mathematical quantities by themselves.

## Embedding Boundary

The embedding layer performs this part:

```text
Token IDs -> Vectors
```

For example:

```text
3 -> [0.21, -0.44, 0.78, 0.12]
```

Token ID 3 is used as an index into the embedding matrix. It selects row 3.

## Business Answer Boundary

MAGPAI then demonstrates a tiny enterprise-style flow:

```text
Structured request -> CSV data -> trend calculation -> chart -> answer
```

The LLM-style layer does not invent the chart. The chart is generated from data.

## Audience Takeaway

MAGPAI does not answer from memory. It converts language into structure, then uses data and tools to produce a chart-backed answer.
