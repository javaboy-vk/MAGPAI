"""
============================================================
Module Name : token_demo.py
Author      : javaboy-vk
Date        : 2026-05-22
Version     : 1.1
Description : Demonstrates how text becomes tokens, IDs, and embeddings
              using the MAGPAI package namespace.
============================================================
"""

import torch

from magpai.tokenization.manual_tokenizer import ManualTokenizer, build_demo_vocab


# ------------------------------------------------------------
# 1. Input sentence
# ------------------------------------------------------------

sentence = "Are MAG sales up in Chicago?"


# ------------------------------------------------------------
# 2. Tokenization and token ID conversion
# ------------------------------------------------------------

vocab = build_demo_vocab()
tokenizer = ManualTokenizer(vocab)
result = tokenizer.encode(sentence)


# ------------------------------------------------------------
# 3. Embedding vectors
#
# The torch package contains data structures for multi-dimensional tensors 
# and defines mathematical operations over these tensors. Additionally, 
# it provides many utilities for efficient serialization of Tensors 
# and arbitrary types, and other useful utilities.
# ------------------------------------------------------------

torch.manual_seed(7)

embedding = torch.nn.Embedding(
    num_embeddings=len(vocab),
    embedding_dim=4,
)


vectors = embedding(torch.tensor(result.token_ids))


# ------------------------------------------------------------
# 4. Output
# ------------------------------------------------------------

print("Sentence:")
print(result.original_text)

print("\nNormalized sentence:")
print(result.normalized_text)

print("\nTokens:")
print(result.tokens)

print("\nToken IDs:")
print(result.token_ids)

print("\nEmbedding vectors:")
print(vectors)

print("\nTakeway point:")
print("Text becomes tokens. Tokens become IDs. IDs become vectors.")
