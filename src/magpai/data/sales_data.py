# =============================================================================
# Module Name: sales_data
# Author: javaboy-vk
# Date: 2026-05-23
# Version: 0.1
# Description:
#     Tiny hard-coded MAG sales dataset for the opening chatbot demo.
# =============================================================================

from dataclasses import dataclass


@dataclass(frozen=True)
class SalesDataPoint:
    location: str
    metric: str
    last_month: int
    this_month: int

    @property
    def change_percent(self) -> float:
        return ((self.this_month - self.last_month) / self.last_month) * 100


class TinySalesDataset:
    """Small source-of-truth dataset used by the demo."""

    def __init__(self) -> None:
        self._data: dict[tuple[str, str], SalesDataPoint] = {
            ("Chicago", "sales"): SalesDataPoint(
                location="Chicago",
                metric="sales",
                last_month=1_200_000,
                this_month=1_500_000,
            )
        }

    def get_metric(self, location: str, metric: str) -> SalesDataPoint:
        return self._data[(location, metric)]

