"""
Data reader for the MAGPAI chart-backed answer demo.
"""

from dataclasses import dataclass
from pathlib import Path
import csv


@dataclass(frozen=True)
class SalesRow:
    period: str
    company: str
    market: str
    metric: str
    value: int


def load_sales_rows(csv_path: Path) -> list[SalesRow]:
    with csv_path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        return [
            SalesRow(
                period=row["period"],
                company=row["company"],
                market=row["market"],
                metric=row["metric"],
                value=int(row["value"]),
            )
            for row in reader
        ]
