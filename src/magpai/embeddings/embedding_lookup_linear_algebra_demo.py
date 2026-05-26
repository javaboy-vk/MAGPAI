"""
============================================================
Module Name : embedding_lookup_linear_algebra_demo.py
Author      : javaboy-vk
Date        : 2026-05-22
Version     : 1.1
Description : Demonstrates how a token ID selects a row from an
              embedding matrix and explains the one-hot equivalent.
#
#     Conceptual explanation of what embedding model PyTorch/Torch uses,
#     intended for the MAGPAI embedding lookup / linear algebra demo.
# =============================================================================
#
# PyTorch / Torch does NOT use one built-in "embedding model" by default.
#
# What PyTorch provides is an embedding layer, most commonly:
#
#     torch.nn.Embedding
#
# This is not a pretrained model by itself.
# It is a trainable lookup table.
#
# Conceptually, the process looks like this:
#
#     token id  --->  row lookup in embedding matrix  --->  dense vector
#
# For example:
#
#     import torch
#     import torch.nn as nn
#
#     embedding = nn.Embedding(
#         num_embeddings=10000,  # vocabulary size
#         embedding_dim=128      # vector size
#     )
#
#     token_ids = torch.tensor([12, 45, 902])
#     vectors = embedding(token_ids)
#
#     print(vectors.shape)
#
# The output shape would be:
#
#     torch.Size([3, 128])
#
# This means:
#
#     3 token ids
#         -> 3 embedding vectors
#         -> each vector has 128 numeric values
#
# Internally, PyTorch stores the embedding table as a trainable parameter matrix:
#
#     Embedding weight matrix shape = [vocabulary_size, embedding_dimension]
#
# For example:
#
#     [10000, 128]
#
# In this example:
#
#     - There are 10,000 possible token ids.
#     - Each token id maps to one row in the embedding matrix.
#     - Each row is a 128-dimensional vector.
#     - The values in the matrix are learned during training unless pretrained
#       weights are loaded manually.
#
# Therefore, the precise answer is:
#
#     PyTorch does not choose an embedding model for you.
#     It gives you torch.nn.Embedding, which is a trainable embedding matrix.
#     The actual embedding model depends on what you build or load.
#
# Common embedding sources:
#
#     - Tiny MAGPAI demo:
#           A custom nn.Embedding layer trained or initialized inside the demo.
#
#     - Word2Vec-style model:
#           Pretrained Word2Vec vectors loaded into a PyTorch embedding layer.
#
#     - BERT-style model:
#           Transformer token embeddings loaded from a pretrained BERT model.
#
#     - OpenAI embedding use:
#           External API embeddings, not native PyTorch embeddings.
#
#     - LLM from scratch:
#           A token embedding layer trained as part of the model.
#
# In MAGPAI terms, the first simple version should likely use:
#
#     nn.Embedding(vocab_size, embedding_dim)
#
# Later, MAGPAI can compare this simple learned embedding table with pretrained
# embeddings or transformer-based embeddings.
#
# Key linear algebra interpretation:
#
#     An embedding lookup is equivalent to selecting one row from a matrix.
#
# If the vocabulary has V tokens and each embedding has D dimensions, then the
# embedding matrix has shape:
#
#     E = [V x D]
#
# A token id selects one row:
#
#     token_id = i
#     embedding_vector = E[i]
#
# For a sequence of token ids:
#
#     [i1, i2, i3, ..., in]
#
# PyTorch returns a matrix of vectors:
#
#     [n x D]
#
# where:
#
#     n = number of tokens in the input sequence
#     D = embedding dimension
#
# This is the first major step where symbolic text is converted into numeric
# tensors that a neural network can process.
# =============================================================================
"""

import torch


# ------------------------------------------------------------
# 1. Embedding table setup
# ------------------------------------------------------------

vocab_size = 8
embedding_dimension = 4

torch.manual_seed(7)

embedding = torch.nn.Embedding(
    num_embeddings=vocab_size,
    embedding_dim=embedding_dimension,
)


# ------------------------------------------------------------
# 2. Token ID lookup
# ------------------------------------------------------------

token_id = 3
lookup_vector = embedding(torch.tensor(token_id))
# lookup_vector = tensor([0.7085, 1.0128, 0.2304, 1.0902],
# grad_fn=<EmbeddingBackward0>),
# embedding = Embedding(8, 4)


# ------------------------------------------------------------
# 3. One-hot matrix multiplication equivalent
# ------------------------------------------------------------

one_hot = torch.zeros(vocab_size)
# one_hot = tensor([0., 0., 0., 1., 0., 0., 0., 0.]),
# vocab_size = 8

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
print("embedding_table[3]")
print(lookup_vector)

print("\nOne-hot form:")
print(one_hot)

print("\nOne-hot vector × embedding matrix:")
print(matrix_multiply_vector)

print("\nAre both methods equal?")
print(torch.allclose(lookup_vector, matrix_multiply_vector))
