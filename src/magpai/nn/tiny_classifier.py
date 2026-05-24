# =============================================================================
# Module Name: tiny_classifier
# Author: javaboy-vk
# Date: 2026-05-23
# Version: 0.1
# Description:
#     Tiny neural-network-like classifier for the opening chatbot demo.
# =============================================================================

from dataclasses import dataclass

from magpai.nlp.vectorizer import VectorizedTokens


@dataclass(frozen=True)
class TinyModelDecision:
    intent: str
    confidence: float
    metric: str | None
    location: str | None
    supported: bool


class TinyNeuralNetworkClassifier:
    """
    Explainable stand-in for a trained neural network.

    The demo exposes the idea that token vectors enter a model. The decision
    logic is intentionally simple and visible for a first live walkthrough.
    """

    def classify(self, vectorized_tokens: VectorizedTokens) -> TinyModelDecision:
        tokens = set(vectorized_tokens.tokens)
        has_sales_question = {"are", "mag", "sales", "up", "in", "chicago"}.issubset(tokens)

        if not has_sales_question:
            return TinyModelDecision(
                intent="unsupported_question",
                confidence=0.12,
                metric=None,
                location=None,
                supported=False,
            )

        return TinyModelDecision(
            intent="sales_question",
            confidence=0.97,
            metric="sales",
            location="Chicago",
            supported=True,
        )

