# =============================================================================
# Module Name: tokenizer
# Author: javaboy-vk
# Date: 2026-05-23
# Version: 0.1
# Description:
#     Tiny tokenizer for the MAGPAI opening chatbot demo.
# =============================================================================

from dataclasses import dataclass
import string


@dataclass(frozen=True)
class TokenizedText:
    original_text: str
    normalized_text: str
    tokens: list[str]


class TinyTokenizer:
    """Small visible tokenizer for a live teaching demo."""

    def normalize(self, text: str) -> str:
        return text.lower().strip()

    def tokenize(self, text: str) -> TokenizedText:
        normalized_text = self.normalize(text)
        punctuation_table = str.maketrans("", "", string.punctuation)
        tokens = normalized_text.translate(punctuation_table).split()

        return TokenizedText(
            original_text=text,
            normalized_text=normalized_text,
            tokens=tokens,
        )

