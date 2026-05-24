---
title: Slide 05 - Tokenizer Step 1 - Tokens
tags:
  - magpai
  - session1
  - teleprompter
slide: 05
---

# Slide 05 - Tokenizer Step 1 - Tokens

## Slide Intent

Explain tokenization as breaking text into known pieces.

## Say This

The first tokenizer step is to break the sentence into tokens.

In our teaching demo, the tokenizer is deliberately simple. It lowercases the sentence and splits on spaces.

So this:

```text
Are MAG sales up in Chicago?
```

becomes this:

```text
["are", "mag", "sales", "up", "in", "chicago", "?"]
```

This is not how every production tokenizer works. Real LLM tokenizers may split text into subwords, punctuation, spaces, and special tokens.

But for learning, word-level tokens make the concept visible.

## Key Points

- Tokenization breaks text into pieces.
- Our demo uses word-level tokens.
- Real tokenizers are more complex.
- The question mark is also a token in this teaching demo.
- The simplified version teaches the boundary clearly.

## Transition

Once we have tokens, the next step is to map them to token IDs.
