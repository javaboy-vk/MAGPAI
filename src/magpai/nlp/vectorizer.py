# =============================================================================
# Module Name: vectorizer
# Author: javaboy-vk
# Date: 2026-05-23
# Version: 0.1
# Description:
#     Tiny embedding table that converts demo tokens into visible vectors.
# =============================================================================

from dataclasses import dataclass


@dataclass(frozen=True)
class VectorizedTokens:
    tokens: list[str]
    vectors: list[list[float]]

    @property
    def shape(self) -> tuple[int, int]:
        if not self.vectors:
            return (0, 0)
        return (len(self.vectors), len(self.vectors[0]))


class TinyVectorizer:
    """Hard-coded embedding table for explainable token-to-vector mapping."""

    def __init__(self) -> None:
        self.embedding_table: dict[str, list[float]] = {
            "are": [0.10, 0.00, 0.00],
            "mag": [0.90, 0.10, 0.10],
            "sales": [0.20, 0.90, 0.10],
            "up": [0.10, 0.80, 0.20],
            "in": [0.00, 0.10, 0.00],
            "chicago": [0.10, 0.20, 0.90],
        }

    def vectorize(self, tokens: list[str]) -> VectorizedTokens:
        vectors = [self.embedding_table.get(token, [0.00, 0.00, 0.00]) for token in tokens]
        return VectorizedTokens(tokens=tokens, vectors=vectors)

