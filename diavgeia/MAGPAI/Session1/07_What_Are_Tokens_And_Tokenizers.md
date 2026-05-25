---
title: Slide 07 - What Are Tokens and Tokenizers?
tags:
  - magpai
  - session1
  - teleprompter
slide: 07
---

# Slide 07 - What Are Tokens and Tokenizers?

## Slide Intent

Pause after the first token list and define the two new terms before moving to token IDs.

## Say This

Before we continue, we need two precise words.

A **token** is a known text piece the model system can handle. In this demo, a token is usually a word, plus the question mark as its own token.

A **tokenizer** is the component that converts raw text into those known pieces.

So the input text:

```text
are MAG sales up in chicago?
```

becomes:

```text
["are", "MAG", "sales", "up", "in", "chicago", "?"]
```

The tokenizer is not deciding whether sales are up. It is only preparing the text for lookup.

## For example:
For ChatGPT 4 an average token is approximately ¾ of the length of a word. 
So, 100 tokens are approximately 75 words.
GPT4 vocabulary size is 100,256

There are fewer unique tokens than unique words. 
This reduces the model’s vocabulary which makes the model more efficient.
Token balances having more meaning than words, while retaining more meaning than individual characters.


## Key Points

- A token is a text piece the system can look up.
- A tokenizer converts raw text into tokens.
- In the teaching demo, the tokenization rule is deliberately simple.
- Tokenization is preparation, not understanding.

## Transition

Now that we know what tokens are, we can map each token to a token ID.


