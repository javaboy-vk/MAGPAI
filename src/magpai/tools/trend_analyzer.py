"""
Trend analyzer for the MAGPAI chart-backed answer demo.
"""

from dataclasses import dataclass

from magpai.llm.structured_request_generator import StructuredDataRequest
from magpai.tools.data_reader import SalesRow


@dataclass(frozen=True)
class TrendAnalysis:
    company: str
    market: str
    metric: str
    start_period: str
    end_period: str
    start_value: int
    end_value: int
    point_change: int
    percent_change: float
    is_up: bool
    rows: list[SalesRow]


def analyze_trend(rows: list[SalesRow], request: StructuredDataRequest) -> TrendAnalysis:
    matching_rows = [
        row
        for row in rows
        if row.company == request.company
        and row.market == request.market
        and row.metric == request.metric
    ]

    if len(matching_rows) < 2:
        raise ValueError(f"Not enough data for request: {request}")

    matching_rows = sorted(matching_rows, key=lambda row: row.period)
    start = matching_rows[0]
    end = matching_rows[-1]
    point_change = end.value - start.value
    percent_change = (point_change / start.value) * 100

    return TrendAnalysis(
        company=request.company,
        market=request.market,
        metric=request.metric,
        start_period=start.period,
        end_period=end.period,
        start_value=start.value,
        end_value=end.value,
        point_change=point_change,
        percent_change=percent_change,
        is_up=point_change > 0,
        rows=matching_rows,
    )
