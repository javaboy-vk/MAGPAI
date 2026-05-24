# =============================================================================
# Module Name: test_magpai_chatbot
# Author: javaboy-vk
# Date: 2026-05-23
# Version: 0.1
# Description:
#     Tests for the MAGPAI chatbot pipeline.
# =============================================================================

from magpai.chatbot import process_question


def test_expected_question_returns_sales_question_result(tmp_path):
    chart_path = tmp_path / "magpai_chicago_sales_chart_v0_1.png"

    result = process_question(
        "are mag sales up in Chicago?",
        chart_path=chart_path,
        generate_chart=False,
    )

    assert result.decision.intent == "sales_question"
    assert result.decision.location == "Chicago"
    assert result.decision.metric == "sales"
    assert result.sales_data is not None
    assert result.sales_data.last_month == 1_200_000
    assert result.sales_data.this_month == 1_500_000
    assert result.sales_data.change_percent == 25.0
    assert result.chart_path is None

