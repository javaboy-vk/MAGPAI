"""
============================================================
Module Name : embedding_lookup_linear_algebra_demo.py
Author      : javaboy-vk
Date        : 2026-05-22
Version     : 1.1
Description : Demonstrates how a token ID selects a row from an
              embedding matrix and explains the one-hot equivalent.
============================================================
"""

import torch


# ------------------------------------------------------------
# 1. Embedding table setup
# ------------------------------------------------------------

vocab_size = 6
embedding_dimension = 4

torch.manual_seed(7)

embedding = torch.nn.Embedding(
    num_embeddings=vocab_size,
    embedding_dim=embedding_dimension,
)


# ------------------------------------------------------------
# 2. Token ID lookup
# ------------------------------------------------------------

token_id = 1
lookup_vector = embedding(torch.tensor(token_id))


# ------------------------------------------------------------
# 3. One-hot matrix multiplication equivalent
# ------------------------------------------------------------

one_hot = torch.zeros(vocab_size)
one_hot[token_id] = 1.0

matrix_multiply_vector = one_hot @ embedding.weight


# ------------------------------------------------------------
# 4. Output
# ------------------------------------------------------------

print("Embedding table shape:")
print(tuple(embedding.weight.shape))

print("\nToken ID:")
print(token_id)

print("\nLookup form:")
print("embedding_table[1]")
print(lookup_vector)

print("\nOne-hot form:")
print(one_hot)

print("\nOne-hot vector × embedding matrix:")
print(matrix_multiply_vector)

print("\nAre both methods equal?")
print(torch.allclose(lookup_vector, matrix_multiply_vector))
