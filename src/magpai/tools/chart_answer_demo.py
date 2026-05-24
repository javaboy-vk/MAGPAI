"""
End-to-end chart-backed answer demo for MAGPAI Session 1.
"""

from pathlib import Path
import json

from magpai.llm.structured_request_generator import generate_structured_request
from magpai.tools.chart_generator import render_ascii_bar_chart, write_svg_bar_chart
from magpai.tools.data_reader import load_sales_rows
from magpai.tools.trend_analyzer import analyze_trend


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = REPO_ROOT / "data" / "mag_sales_demo.csv"
CHART_PATH = REPO_ROOT / "dist" / "charts" / "mag_sales_chicago.svg"


def main() -> None:
    question = "Are MAG sales up in Chicago?"

    print("Question:")
    print(question)

    print("\nStructured request:")
    structured_request = generate_structured_request(question)
    print(json.dumps(structured_request.to_dict(), indent=2))

    print("\nData source:")
    print(DATA_PATH)

    rows = load_sales_rows(DATA_PATH)
    analysis = analyze_trend(rows, structured_request)

    print("\nGenerated chart:")
    print(render_ascii_bar_chart(analysis))

    write_svg_bar_chart(analysis, CHART_PATH)

    answer_word = "up" if analysis.is_up else "not up"
    print("\nMAGPAI answer:")
    print(
        f"Yes. MAG sales in Chicago are {answer_word}. "
        f"They increased from {analysis.start_value} in {analysis.start_period} "
        f"to {analysis.end_value} in {analysis.end_period}, "
        f"a gain of {analysis.point_change} points, "
        f"or {analysis.percent_change:.1f}%."
    )

    print("\nChart artifact:")
    print(CHART_PATH)


if __name__ == "__main__":
    main()
