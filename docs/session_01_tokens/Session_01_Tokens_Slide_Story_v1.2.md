# MAGPAI Session 1 - Slide Story - v1.2

## Theme

How Text Becomes Numbers

## Human Statement

```text
Sales are up in Chicago
```

A human immediately sees a business statement. The words suggest a metric, a positive movement, and a location.

A neural network does not start with that meaning. It cannot process raw English words directly. It needs numbers.

## Transformation

```text
"Sales are up in Chicago"
        ↓
Normalize text
        ↓
"sales are up in chicago"
        ↓
Tokenize
        ↓
["sales", "are", "up", "in", "chicago"]
        ↓
Vocabulary lookup
        ↓
[1, 2, 3, 4, 5]
        ↓
Embedding lookup
        ↓
Numeric vectors
        ↓
Neural network input
```

## Tokenizer Boundary

The tokenizer performs this part:

```text
Text → Tokens → Token IDs
```

In the MAGPAI teaching demo, tokenization is deliberately simple:

```python
tokens = sentence.lower().split()
```

This produces word-level tokens:

```text
["sales", "are", "up", "in", "chicago"]
```

A real LLM tokenizer may split text into whole words, subwords, spaces, punctuation, and special tokens. The simplified demo teaches the concept before introducing production tokenizer complexity.

## Vocabulary Lookup

```text
"sales"   → 1
"are"     → 2
"up"      → 3
"in"      → 4
"chicago" → 5
```

The token IDs are arbitrary labels. They are not meaningful mathematical quantities by themselves.

## Embedding Boundary

The embedding layer performs this part:

```text
Token IDs → Vectors
```

For example:

```text
1 → [0.21, -0.44, 0.78, 0.12]
```

Token ID 1 is used as an index into the embedding matrix. It selects row 1.

## Audience Takeaway

A model never sees `sales` as a word. It sees a numeric pattern.
