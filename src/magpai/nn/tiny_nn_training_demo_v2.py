# =============================================================================
# Module Name: tiny_nn_training_demo_v2.py
# Author: javaboy-vk
# Date: 2026-06-01
# Version: 2.0
# Description:
#   Console companion for the MAGPAI Tiny ANN Trainer browser demo.
#   It demonstrates the same concept:
#   - The question stays fixed: "Are MAG sales up in Chicago?"
#   - Six different training sentences update weights and bias.
#   - After each update, MAGPAI re-answers the same fixed question.
# =============================================================================

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class TrainingExample:
    """One MAGPAI training experience."""

    sentence: str
    target: int
    vector: List[float]


def sigmoid(value: float) -> float:
    """Convert a raw ANN score into a probability-like value between 0 and 1."""
    return 1.0 / (1.0 + math.exp(-value))


def dot(left: List[float], right: List[float]) -> float:
    """Calculate the dot product between two vectors."""
    return sum(a * b for a, b in zip(left, right))


class MAGPAITinyANN:
    """
    A tiny educational ANN with one linear neuron.

    Conceptually:
        z = w·x + b
        prediction = sigmoid(z)

    During training:
        error = target - prediction
        weight = weight + learning_rate * error * input
        bias = bias + learning_rate * error
    """

    def __init__(self, weights: List[float], bias: float, learning_rate: float) -> None:
        self.weights = weights
        self.bias = bias
        self.learning_rate = learning_rate

    def predict(self, vector: List[float]) -> float:
        """Run inference using the current weights and bias."""
        raw_score = dot(self.weights, vector) + self.bias
        return sigmoid(raw_score)

    def train_one(self, example: TrainingExample) -> float:
        """Train on one example and return the prediction before the update."""
        prediction = self.predict(example.vector)
        error = example.target - prediction

        for index, input_value in enumerate(example.vector):
            self.weights[index] += self.learning_rate * error * input_value

        self.bias += self.learning_rate * error
        return prediction


def main() -> None:
    fixed_question = "Are MAG sales up in Chicago?"

    feature_names = [
        "Sales Change",
        "Location Chicago",
        "Trend Up/Down",
        "Question Type",
        "Time Context",
        "Overall Sentiment",
    ]

    fixed_question_vector = [0.81, 1.00, 1.00, 1.00, 0.60, 0.85]

    examples = [
        TrainingExample("Chicago sales increased by 15%", 1, [0.65, 1.00, 0.78, 1.00, 0.40, 0.70]),
        TrainingExample("Chicago sales increased by 22%", 1, [0.78, 1.00, 0.88, 1.00, 0.45, 0.78]),
        TrainingExample("Chicago sales decreased by 8%", 0, [0.28, 1.00, 0.18, 1.00, 0.35, 0.20]),
        TrainingExample("Chicago sales increased by 18%", 1, [0.70, 1.00, 0.82, 1.00, 0.50, 0.74]),
        TrainingExample("Chicago sales increased by 30%", 1, [0.92, 1.00, 1.00, 1.00, 0.55, 0.90]),
        TrainingExample("Chicago sales increased by 27%", 1, [0.81, 1.00, 1.00, 1.00, 0.60, 0.85]),
    ]

    model = MAGPAITinyANN(
        weights=[0.150, 0.200, 0.200, 0.200, 0.200, 0.150],
        bias=-1.100,
        learning_rate=0.70,
    )

    print("MAGPAI Tiny ANN Training Demo v2.0")
    print("==================================")
    print(f'Fixed question: "{fixed_question}"')
    print("The question never changes. Training changes weights and bias.\n")

    initial_prediction = model.predict(fixed_question_vector)
    print(f"Step 0 prediction for fixed question: {initial_prediction:.3f}\n")

    for step, example in enumerate(examples, start=1):
        print("=" * 72)
        print(f"Training Step {step}")
        print(f"Training sentence: {example.sentence}")
        print(f"Target label: {example.target} ({'YES' if example.target == 1 else 'NO'})")
        print("\nTensor / graphics vector:")
        for name, value in zip(feature_names, example.vector):
            print(f"  {name:<18}: {value:.2f}")

        prediction_before = model.train_one(example)
        prediction_after = model.predict(fixed_question_vector)

        print(f"\nPrediction on training example before update: {prediction_before:.3f}")
        print(f"Re-answer fixed question after update:        {prediction_after:.3f}")
        print(f"Current bias: {model.bias:.3f}")
        print("Current weights:")
        for name, weight in zip(feature_names, model.weights):
            print(f"  {name:<18}: {weight:.3f}")

        input("\nPress Enter for next training sentence...")

    final_prediction = model.predict(fixed_question_vector)
    print("\n" + "=" * 72)
    print("Training complete.")
    print(f'Final answer to "{fixed_question}": {"YES" if final_prediction >= 0.5 else "NO"}')
    print(f"Final confidence: {final_prediction:.3f}")


if __name__ == "__main__":
    main()
