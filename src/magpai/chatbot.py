# =============================================================================
# Module Name: chatbot
# Author: javaboy-vk
# Date: 2026-05-23
# Version: 0.1
# Description:
#     CLI-first MAGPAI chatbot for question-to-chart AI learning.
# =============================================================================

from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path
import json

from magpai.charts.sales_chart import SalesChartGenerator
from magpai.data.sales_data import SalesDataPoint, TinySalesDataset
from magpai.nlp.tokenizer import TinyTokenizer
from magpai.nlp.vectorizer import TinyVectorizer, VectorizedTokens
from magpai.nn.tiny_classifier import TinyModelDecision, TinyNeuralNetworkClassifier


DEFAULT_CHART_PATH = Path("output") / "magpai_chicago_sales_chart_v0_1.png"


@dataclass(frozen=True)
class ChatbotResult:
    question: str
    tokens: list[str]
    vectorized_tokens: VectorizedTokens
    decision: TinyModelDecision
    sales_data: SalesDataPoint | None
    chart_path: Path | None


def _format_vector(vector: list[float]) -> str:
    return "[" + ", ".join(f"{value:.2f}" for value in vector) + "]"


def _format_money(value: int) -> str:
    return f"${value / 1_000_000:.1f}M"


def process_question(
    question: str,
    chart_path: Path = DEFAULT_CHART_PATH,
    generate_chart: bool = True,
) -> ChatbotResult:
    # Stage 1: natural-language text enters the chatbot pipeline.
    tokenizer = TinyTokenizer()

    # Stage 2: tokens become tiny fixed vectors from a visible embedding table.
    vectorizer = TinyVectorizer()

    # Stage 3: vectors enter a neural-network-like classifier.
    classifier = TinyNeuralNetworkClassifier()

    # Stage 4: detected intent and entities drive trusted data lookup.
    sales_dataset = TinySalesDataset()

    tokenized_text = tokenizer.tokenize(question)
    vectorized_tokens = vectorizer.vectorize(tokenized_text.tokens)
    decision = classifier.classify(vectorized_tokens)

    sales_data = None
    generated_chart_path = None

    if decision.supported and decision.location and decision.metric:
        sales_data = sales_dataset.get_metric(decision.location, decision.metric)

        # Stage 5: the chart tool creates an artifact from data, not memory.
        if generate_chart:
            generated_chart_path = SalesChartGenerator().create_chart(sales_data, chart_path)

    return ChatbotResult(
        question=question,
        tokens=tokenized_text.tokens,
        vectorized_tokens=vectorized_tokens,
        decision=decision,
        sales_data=sales_data,
        chart_path=generated_chart_path,
    )


def print_banner() -> None:
    print("=" * 50)
    print("MAGPAI – Tiny AI Business Assistant – v0.1")
    print("Fictitious MAG Company AI Learning Demo")
    print("=" * 50)


def print_thinking_trace(result: ChatbotResult) -> None:
    print("\nMAGPAI THINKING TRACE")
    print("1. Text received")
    print("2. Text tokenized")
    print("3. Tokens converted to vectors")
    print("4. Vectors entered tiny neural network")
    print(f"5. Intent detected: {result.decision.intent}")
    print(f"6. Location detected: {result.decision.location or 'not detected'}")
    print(f"7. Metric detected: {result.decision.metric or 'not detected'}")
    print("8. Sales data retrieved" if result.sales_data else "8. Sales data not retrieved")
    print("9. Chart generated" if result.chart_path else "9. Chart not generated")
    print("10. Response composed")

    print("\nMAGPAI-TRACE> received text:")
    print(f"  {result.question}")

    print("\nMAGPAI-TRACE> tokens:")
    print(f"  {json.dumps(result.tokens)}")

    print("\nMAGPAI-TRACE> vectors:")
    for token, vector in zip(result.vectorized_tokens.tokens, result.vectorized_tokens.vectors):
        print(f"  {token:<8} -> {_format_vector(vector)}")

    token_count, dimension_count = result.vectorized_tokens.shape
    print("\nMAGPAI-TRACE> tiny neural network input:")
    print(f"  matrix shape: {token_count} tokens x {dimension_count} dimensions")

    print("\nMAGPAI-TRACE> tiny neural network output:")
    print(f"  intent = {result.decision.intent}")
    print(f"  confidence = {result.decision.confidence:.2f}")

    print("\nMAGPAI-TRACE> extracted entities:")
    print(f"  metric = {result.decision.metric or 'not detected'}")
    print(f"  location = {result.decision.location or 'not detected'}")

    if result.sales_data:
        print("\nMAGPAI-TRACE> retrieved data:")
        print(f"  last_month = {result.sales_data.last_month}")
        print(f"  this_month = {result.sales_data.this_month}")
        print(f"  change_percent = {result.sales_data.change_percent:.1f}")

    if result.chart_path:
        print("\nMAGPAI-TRACE> chart saved:")
        print(f"  {result.chart_path.as_posix()}")


def print_response(result: ChatbotResult) -> None:
    print("\nMAGPAI RESPONSE\n")

    if not result.decision.supported or not result.sales_data:
        print("This v0.1 chatbot currently supports the Chicago MAG sales question.")
        print('Try: "are mag sales up in Chicago?"')
        return

    sales_data = result.sales_data
    print("Yes. MAG sales are up in Chicago.\n")
    print(
        f"Chicago sales increased from {_format_money(sales_data.last_month)} last month "
        f"to {_format_money(sales_data.this_month)} this month,"
    )
    print(f"which is a {sales_data.change_percent:.0f}% increase month over month.\n")
    print("MAGPAI generated the chart below from the sales data.")


def run_chatbot(question: str, trace: bool = False) -> ChatbotResult:
    result = process_question(question)
    if trace:
        print_thinking_trace(result)
    print_response(result)
    return result


def main() -> None:
    parser = ArgumentParser(description="MAGPAI Chatbot - v0.1")
    parser.add_argument("--question", help="Run the chatbot without interactive input.")
    parser.add_argument(
        "--trace",
        action="store_true",
        help="Show the under-the-covers MAGPAI thinking trace.",
    )
    args = parser.parse_args()

    print_banner()

    if args.question:
        print(f"\nMAGPAI> {args.question}")
        run_chatbot(args.question, trace=args.trace)
        return

    question = input("\nMAGPAI> ")
    run_chatbot(question, trace=args.trace)


if __name__ == "__main__":
    main()
