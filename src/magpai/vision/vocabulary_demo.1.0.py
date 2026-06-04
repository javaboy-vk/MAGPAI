# =============================================================================
# Module Name : vocabulary_demo.1.0.py
# Author      : javaboy-vk
# Date        : 2026-06-03
# Version     : 1.0
# Description : Terminal-based MAGPAI Vision Vocabulary demo.
#               This program demonstrates how a bird image can be represented
#               as visual tokens, converted into embeddings, passed through a
#               tiny neural network, and classified as MAGPIE.
# =============================================================================

"""
MAGPAI Vision Vocabulary Demo - v1.0

This is a teaching program, not a production computer-vision model.
It intentionally uses fixed, readable numbers so the learning flow is clear:

    image idea -> visual vocabulary -> token IDs -> embedding tensor
    -> tiny neural network -> prediction

Run:
    python src/magpai/vision/vocabulary_demo.1.0.py

Press ENTER to advance through each step.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from math import exp
from typing import Dict, List, Sequence, Tuple

Vector = List[float]
Matrix = List[Vector]


# -----------------------------------------------------------------------------
# 1. Demo Data Structures
# -----------------------------------------------------------------------------

@dataclass(frozen=True)
class VisualToken:
    """Represents one learned visual concept in the MAGPAI visual vocabulary."""

    token_id: int
    name: str
    explanation: str


@dataclass(frozen=True)
class Prediction:
    """Represents one output class and its probability."""

    label: str
    probability: float


# -----------------------------------------------------------------------------
# 2. Utility Functions
# -----------------------------------------------------------------------------

def clear_screen() -> None:
    """Clear the terminal so each teaching step appears as a clean slide."""
    os.system("cls" if os.name == "nt" else "clear")


def wait_for_enter() -> None:
    """Pause until the user presses ENTER."""
    input("\nPress ENTER to advance...")


def print_header(title: str, step: int, total_steps: int) -> None:
    """Print a consistent MAGPAI header for every terminal screen."""
    print("=" * 78)
    print(f"MAGPAI VISION VOCABULARY DEMO v1.0 | Step {step} of {total_steps}")
    print(title)
    print("=" * 78)


def print_matrix(matrix: Sequence[Sequence[float]], row_labels: List[str]) -> None:
    """Print an embedding matrix with labels on the left."""
    for label, row in zip(row_labels, matrix):
        values = "  ".join(f"{value:>6.2f}" for value in row)
        print(f"{label:<18} [ {values} ]")


def softmax(logits: Sequence[float]) -> Vector:
    """
    Convert raw neural-network scores into probabilities.

    The neural network produces raw numbers called logits.
    Softmax turns those numbers into values that add up to 1.0.
    """
    max_logit = max(logits)
    exp_values = [exp(value - max_logit) for value in logits]
    total = sum(exp_values)
    return [value / total for value in exp_values]


def mean_rows(matrix: Sequence[Sequence[float]]) -> Vector:
    """Average rows into one summary vector."""
    row_count = len(matrix)
    return [sum(row[column] for row in matrix) / row_count for column in range(len(matrix[0]))]


def vector_matrix_multiply(vector: Sequence[float], matrix: Sequence[Sequence[float]]) -> Vector:
    """Multiply a row vector by a matrix stored as rows."""
    column_count = len(matrix[0])
    return [
        sum(vector[row_index] * matrix[row_index][column_index] for row_index in range(len(vector)))
        for column_index in range(column_count)
    ]


def add_vectors(left: Sequence[float], right: Sequence[float]) -> Vector:
    """Add two equal-length vectors."""
    return [left_value + right_value for left_value, right_value in zip(left, right)]


# -----------------------------------------------------------------------------
# 3. Visual Vocabulary
# -----------------------------------------------------------------------------

VISUAL_VOCABULARY: Dict[int, VisualToken] = {
    1: VisualToken(1, "Black Feather", "Dark feather texture common in magpies."),
    2: VisualToken(2, "White Feather", "White feather patch, especially on the belly or wing."),
    3: VisualToken(3, "Beak", "Bird beak shape near the head."),
    4: VisualToken(4, "Eye", "Small dark eye feature."),
    5: VisualToken(5, "Wing", "Wing contour and feather grouping."),
    6: VisualToken(6, "Tail", "Long tail shape, a strong magpie clue."),
    7: VisualToken(7, "Branch", "Perch or branch context."),
    8: VisualToken(8, "Sky / Background", "Background context around the bird."),
}

# This is the simplified result of the vision tokenizer.
# A real model would compute these from image patches.
DETECTED_TOKEN_IDS: List[int] = [3, 4, 1, 2, 2, 6, 7, 8]

# -----------------------------------------------------------------------------
# 4. Embedding Table
# -----------------------------------------------------------------------------

# Each token ID maps to a dense vector.
# This is the image equivalent of word embeddings in text models.
# The demo uses 8 dimensions for readability.
EMBEDDING_TABLE: Dict[int, Vector] = {
    1: [0.82, -0.14, 0.71, 0.23, -0.31, 0.65, -0.12, 0.45],
    2: [0.73, -0.32, 0.61, 0.18, -0.07, 0.44, 0.21, -0.19],
    3: [0.91, -0.21, 0.84, 0.12, -0.05, 0.77, -0.33, 0.16],
    4: [0.15, 0.77, 0.09, 0.52, -0.22, 0.18, 0.66, -0.41],
    5: [0.55, 0.43, 0.19, 0.66, -0.22, 0.30, 0.28, -0.15],
    6: [0.68, 0.24, 0.33, 0.74, -0.13, 0.35, 0.08, -0.28],
    7: [0.46, 0.12, 0.58, -0.21, 0.09, 0.11, -0.41, 0.83],
    8: [0.22, 0.60, -0.14, 0.18, 0.71, -0.08, 0.12, 0.64],
}

# -----------------------------------------------------------------------------
# 5. Tiny Neural Network
# -----------------------------------------------------------------------------

class TinyMagpaiVisionNetwork:
    """
    A tiny neural network used only for explaining MAGPAI Vision.

    Network shape:

        Input embedding summary: 8 numbers
            v fully connected weights
        Hidden Layer 1: 6 neurons
            v fully connected weights
        Hidden Layer 2: 3 neurons
            v fully connected weights
        Output Layer: 4 class scores

    Important teaching point:
    -------------------------
    A neuron is a small mathematical unit. It receives numbers from the
    previous layer, multiplies each input by a learned weight, adds a bias,
    and applies an activation function.

        activation = ReLU((input_1 * weight_1) + ... + bias)

    A connection is not a wire carrying words like "beak" or "tail".
    It carries a numeric signal. The weight on that connection determines
    how strongly that signal affects the next neuron.

    In a real trained model, all these weights are learned from data.
    In this teaching demo, the weights are manually chosen so the flow is
    stable, readable, and clearly favors MAGPIE for the provided tokens.
    """

    def __init__(self) -> None:
        # Hidden Layer 1 weights.
        # Shape: 8 input dimensions -> 6 hidden neurons.
        # Each column represents one neuron in Hidden Layer 1.
        # Example:
        #   W1[:, 0] are all weights feeding Hidden Neuron 1.
        #   Hidden Neuron 1 acts like a bird-head feature detector.
        self.w1 = [
            [0.80, 0.55, 0.40, 0.20, 0.10, 0.05],
            [-0.10, 0.20, 0.30, 0.45, 0.15, 0.10],
            [0.75, 0.65, 0.30, 0.25, 0.20, 0.10],
            [0.20, 0.30, 0.70, 0.60, 0.15, 0.10],
            [-0.20, -0.10, 0.10, 0.20, 0.60, 0.65],
            [0.70, 0.55, 0.25, 0.20, 0.15, 0.10],
            [-0.30, 0.10, 0.50, 0.20, 0.05, 0.15],
            [0.10, -0.10, -0.20, 0.10, 0.55, 0.70],
        ]
        self.b1 = [0.10, 0.05, 0.05, 0.04, 0.02, 0.01]

        # Hidden Layer 2 weights.
        # Shape: 6 hidden-layer-1 neurons -> 3 hidden-layer-2 neurons.
        # These neurons combine lower-level features into larger concepts:
        #   H2.1 = bird shape evidence
        #   H2.2 = black/white feather pattern evidence
        #   H2.3 = magpie-specific long-tail evidence
        self.w2 = [
            [0.90, 0.20, 0.30],
            [0.75, 0.35, 0.25],
            [0.20, 0.95, 0.45],
            [0.10, 0.85, 0.55],
            [0.25, 0.20, 0.90],
            [0.15, 0.10, 0.55],
        ]
        self.b2 = [0.05, 0.08, 0.10]

        # Output weights.
        # Shape: 3 hidden-layer-2 neurons -> 4 output classes.
        # Output columns represent: Magpie, Crow, Jay, Other Bird.
        # Magpie receives strong positive weights from all three combined features.
        self.w3 = [
            [1.20, 0.45, 0.35, 0.20],
            [1.50, 0.55, 0.20, 0.25],
            [1.65, 0.10, 0.15, 0.45],
        ]
        self.b3 = [0.30, -0.20, -0.35, -0.40]

    @staticmethod
    def relu(values: Sequence[float]) -> Vector:
        """
        ReLU activation function.

        ReLU means Rectified Linear Unit:
            negative values become 0
            positive values pass through unchanged

        This lets neurons behave like feature detectors that "turn on"
        when the incoming evidence is strong enough.
        """
        return [max(value, 0) for value in values]

    def forward(
        self,
        embedding_tensor: Matrix,
    ) -> Tuple[Vector, Vector, Vector, Vector]:
        """
        Run the embedding tensor through the tiny neural network.

        The embedding tensor has one row per visual token.
        To keep the demo simple, we average all token embeddings into one
        8-number image summary vector. A real vision transformer would preserve
        more spatial structure and use attention across image patches.
        """
        image_vector = mean_rows(embedding_tensor)

        # Fully connected layer 1:
        # Every input dimension connects to every neuron in Hidden Layer 1.
        hidden_1_raw = add_vectors(vector_matrix_multiply(image_vector, self.w1), self.b1)
        hidden_1 = self.relu(hidden_1_raw)

        # Fully connected layer 2:
        # Every Hidden Layer 1 neuron connects to every Hidden Layer 2 neuron.
        hidden_2_raw = add_vectors(vector_matrix_multiply(hidden_1, self.w2), self.b2)
        hidden_2 = self.relu(hidden_2_raw)

        # Output layer:
        # Every Hidden Layer 2 neuron connects to every output class neuron.
        logits = add_vectors(vector_matrix_multiply(hidden_2, self.w3), self.b3)
        probabilities = softmax(logits)

        return image_vector, hidden_1, hidden_2, probabilities


# -----------------------------------------------------------------------------
# 6. Demo Step Functions
# -----------------------------------------------------------------------------

def step_1_image() -> None:
    clear_screen()
    print_header("1. INPUT IMAGE", 1, 7)
    print("The input is a picture of a magpie-like bird.")
    print()
    print("Computer vision starts with pixels, not meaning.")
    print("MAGPAI does not initially see 'bird' or 'magpie'.")
    print("It receives numbers representing color and brightness.")
    print()
    print("[ Stylized image: black-and-white bird on a branch ]")
    wait_for_enter()


def step_2_visual_vocabulary() -> None:
    clear_screen()
    print_header("2. LEARNED VISUAL VOCABULARY", 2, 7)
    print("The visual vocabulary is the image equivalent of a text vocabulary.")
    print()
    for token in VISUAL_VOCABULARY.values():
        print(f"{token.token_id:>2}  {token.name:<18} - {token.explanation}")
    wait_for_enter()


def step_3_tokenizer() -> None:
    clear_screen()
    print_header("3. VISION TOKENIZER", 3, 7)
    print("The image is divided into patches.")
    print("Each important patch is matched to a learned visual token.")
    print()
    print("Detected visual tokens:")
    for token_id in DETECTED_TOKEN_IDS:
        token = VISUAL_VOCABULARY[token_id]
        print(f"  {token_id:>2} -> {token.name}")
    print()
    print(f"Visual token ID sequence: {DETECTED_TOKEN_IDS}")
    wait_for_enter()


def build_embedding_tensor() -> Matrix:
    """Convert visual token IDs into the embedding tensor."""
    return [EMBEDDING_TABLE[token_id] for token_id in DETECTED_TOKEN_IDS]


def step_4_embeddings(embedding_tensor: Matrix) -> None:
    clear_screen()
    print_header("4. EMBEDDING TENSOR", 4, 7)
    row_labels = [VISUAL_VOCABULARY[token_id].name for token_id in DETECTED_TOKEN_IDS]
    print("Each token ID is replaced by its embedding vector.")
    print("Each row below is one visual token embedding.")
    print()
    print_matrix(embedding_tensor, row_labels)
    wait_for_enter()


def step_5_network_explanation() -> None:
    clear_screen()
    print_header("5. TINY NEURAL NETWORK", 5, 7)
    print("MAGPAI now sends the embedding tensor into a small neural network.")
    print()
    print("Network architecture:")
    print("  Input summary vector : 8 numbers")
    print("  Hidden Layer 1       : 6 neurons")
    print("  Hidden Layer 2       : 3 neurons")
    print("  Output Layer         : 4 classes")
    print()
    print("Important idea:")
    print("  Every neuron in one layer connects to neurons in the next layer.")
    print("  Each connection has a weight.")
    print("  The weight controls how strongly one signal influences the next neuron.")
    wait_for_enter()


def step_6_forward_pass(
    network: TinyMagpaiVisionNetwork,
    embedding_tensor: Matrix,
) -> Tuple[Vector, Vector, Vector, Vector]:
    clear_screen()
    print_header("6. FORWARD PASS THROUGH THE NETWORK", 6, 7)
    image_vector, hidden_1, hidden_2, probabilities = network.forward(embedding_tensor)
    print("Image summary vector, created by averaging token embeddings:")
    print("[ " + "  ".join(f"{value:>6.2f}" for value in image_vector) + " ]")
    print()
    print("Hidden Layer 1 activations:")
    print("[ " + "  ".join(f"{value:>6.2f}" for value in hidden_1) + " ]")
    print()
    print("Hidden Layer 2 activations:")
    print("[ " + "  ".join(f"{value:>6.2f}" for value in hidden_2) + " ]")
    print()
    print("The activated neurons now carry evidence toward the output classes.")
    wait_for_enter()
    return image_vector, hidden_1, hidden_2, probabilities


def step_7_prediction(probabilities: Sequence[float]) -> None:
    clear_screen()
    print_header("7. PREDICTION OUTPUT", 7, 7)
    labels = ["Magpie", "Crow", "Jay", "Other Bird"]
    predictions = [Prediction(label, float(prob)) for label, prob in zip(labels, probabilities)]
    predictions.sort(key=lambda item: item.probability, reverse=True)

    for item in predictions:
        bar = "#" * int(item.probability * 40)
        print(f"{item.label:<12} {item.probability * 100:>6.2f}%  {bar}")

    print()
    print(f"Final MAGPAI answer: {predictions[0].label.upper()}")
    print()
    print("Teaching conclusion:")
    print("  Text models use token vocabularies.")
    print("  Vision models can use visual tokens or learned visual features.")
    print("  In both cases, tokens become embeddings, and embeddings become neural-network input.")


# -----------------------------------------------------------------------------
# 7. Main Program
# -----------------------------------------------------------------------------

def main() -> None:
    """Run the complete interactive MAGPAI Vision Vocabulary demo."""
    step_1_image()
    step_2_visual_vocabulary()
    step_3_tokenizer()

    embedding_tensor = build_embedding_tensor()
    step_4_embeddings(embedding_tensor)

    network = TinyMagpaiVisionNetwork()
    step_5_network_explanation()
    _, _, _, probabilities = step_6_forward_pass(network, embedding_tensor)
    step_7_prediction(probabilities)


if __name__ == "__main__":
    main()
