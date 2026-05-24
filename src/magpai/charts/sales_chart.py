# =============================================================================
# Module Name: sales_chart
# Author: javaboy-vk
# Date: 2026-05-23
# Version: 0.1
# Description:
#     Simple matplotlib chart generator for the opening chatbot demo.
# =============================================================================

from pathlib import Path

from magpai.data.sales_data import SalesDataPoint


def _format_millions(value: int) -> str:
    return f"${value / 1_000_000:.1f}M"


class SalesChartGenerator:
    """Creates a small presentation-readable chart from sales data."""

    def create_chart(self, sales_data: SalesDataPoint, output_path: Path) -> Path:
        import matplotlib.pyplot as plt

        output_path.parent.mkdir(parents=True, exist_ok=True)

        labels = ["Last Month", "This Month"]
        values = [sales_data.last_month, sales_data.this_month]
        display_values = [_format_millions(value) for value in values]

        fig, ax = plt.subplots(figsize=(8, 4.5))
        bars = ax.bar(labels, values, color=["#64748b", "#2563eb"], width=0.55)

        ax.set_title("Chicago MAG Sales", fontsize=18, fontweight="bold", pad=18)
        ax.set_ylabel("Sales", fontsize=12)
        ax.set_ylim(0, 1_700_000)
        ax.grid(axis="y", linestyle="--", alpha=0.25)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        for bar, display_value in zip(bars, display_values):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 45_000,
                display_value,
                ha="center",
                va="bottom",
                fontsize=13,
                fontweight="bold",
            )

        ax.text(
            0.5,
            -0.22,
            "Change: +25% month over month",
            transform=ax.transAxes,
            ha="center",
            fontsize=13,
            color="#166534",
            fontweight="bold",
        )

        fig.tight_layout()
        fig.savefig(output_path, dpi=160, bbox_inches="tight")
        plt.close(fig)

        return output_path

