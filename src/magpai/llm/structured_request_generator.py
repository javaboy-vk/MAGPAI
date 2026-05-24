"""
Deterministic structured request generator for the MAGPAI teaching demo.

This is not a real LLM. It models the orchestration shape we want to teach:
language becomes a structured request that downstream tools can execute.
"""

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class StructuredDataRequest:
    intent: str
    company: str
    metric: str
    market: str
    comparison: str
    output: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


def generate_structured_request(question: str) -> StructuredDataRequest:
    normalized = question.lower()

    if "mag" not in normalized:
        raise ValueError("This demo only supports MAG questions.")
    if "sales" not in normalized:
        raise ValueError("This demo only supports sales metric questions.")
    if "chicago" not in normalized:
        raise ValueError("This demo only supports the Chicago market for Session 1.")

    return StructuredDataRequest(
        intent="metric_trend_question",
        company="MAG",
        metric="sales",
        market="Chicago",
        comparison="over_time",
        output="chart",
    )
