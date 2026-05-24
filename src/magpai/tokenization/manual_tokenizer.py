"""
============================================================
Module Name : manual_tokenizer.py
Author      : javaboy-vk
Date        : 2026-05-22
Version     : 1.0
Description : Provides a tiny manual tokenizer for MAGPAI Session 1.
============================================================
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TokenizationResult:
    """
    Holds the result of converting text into tokens and token IDs.
    """

    original_text: str
    normalized_text: str
    tokens: list[str]
    token_ids: list[int]


class ManualTokenizer:
    """
    A deliberately simple tokenizer for teaching the concept:

        text -> tokens -> token IDs

    This tokenizer uses lowercase normalization and whitespace splitting.
    It is not intended to behave like a production LLM tokenizer.
    """

    def __init__(self, vocab: dict[str, int]):
        self.vocab = vocab

    def normalize(self, text: str) -> str:
        """
        Normalizes input text for the teaching demo.
        """

        return text.lower().replace("?", " ?").strip()

    def tokenize(self, text: str) -> list[str]:
        """
        Splits normalized text into word-level tokens.
        """

        return self.normalize(text).split()

    def encode(self, text: str) -> TokenizationResult:
        """
        Converts text into tokens and token IDs.
        """

        normalized_text = self.normalize(text)
        tokens = normalized_text.split()

        unknown_tokens = [token for token in tokens if token not in self.vocab]

        if unknown_tokens:
            raise ValueError(
                f"Unknown token(s): {unknown_tokens}. "
                f"Allowed vocabulary: {list(self.vocab.keys())}"
            )

        token_ids = [self.vocab[token] for token in tokens]

        return TokenizationResult(
            original_text=text,
            normalized_text=normalized_text,
            tokens=tokens,
            token_ids=token_ids,
        )


def build_demo_vocab() -> dict[str, int]:
    """
    Builds the tiny MAGPAI Session 1 demonstration vocabulary.
    """

    return {
        "<PAD>": 0,
        "are": 1,
        "mag": 2,
        "sales": 3,
        "up": 4,
        "in": 5,
        "chicago": 6,
        "?": 7,
    }
