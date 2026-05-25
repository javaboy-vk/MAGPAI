---
title: Slide 07 - Tokenizer Step 1 - Tokens
tags:
  - magpai
  - session1
  - teleprompter
slide: 07
---

# Slide 07 - Tokenizer Step 1 - Tokens

## Slide Intent

Explain tokenization as breaking text into known pieces.

## Say This

The first tokenizer step is to break the sentence into tokens.

In our teaching demo, the tokenizer is deliberately simple. It lowercases the sentence and splits on spaces.

So this input question:

```text
Are MAG sales up in Chicago?
```

becomes this:

```text
["are", "MAG", "sales", "up", "in", "chicago", "?"]
```

In the PPTX we keep `MAG` capitalized because it is the company name in the input text. The demo still treats it as one token.

This is not how every production tokenizer works. Real LLM tokenizers may split text into subwords, punctuation, spaces, casing variants, and special tokens.

But for learning, word-level tokens make the concept visible.

## Key Points

- Tokenization breaks text into pieces.
- Our demo uses word-level tokens.
- Real tokenizers are more complex.
- The question mark is also a token in this teaching demo.
- The simplified version teaches the boundary clearly.

## Transition

Before we map tokens to IDs, we will define the words token and tokenizer.




