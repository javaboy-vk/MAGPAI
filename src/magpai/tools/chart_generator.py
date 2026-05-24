"""
Chart generator for the MAGPAI chart-backed answer demo.
"""

from pathlib import Path

from magpai.tools.trend_analyzer import TrendAnalysis


def render_ascii_bar_chart(analysis: TrendAnalysis) -> str:
    max_value = max(row.value for row in analysis.rows)
    lines = [f"{analysis.company} {analysis.metric.title()} - {analysis.market}"]

    for row in analysis.rows:
        label = row.period
        bar_length = round((row.value / max_value) * 24)
        bar = "#" * bar_length
        lines.append(f"{label} | {bar:<24} {row.value}")

    return "\n".join(lines)


def write_svg_bar_chart(analysis: TrendAnalysis, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    width = 720
    height = 360
    left = 120
    top = 70
    bar_height = 34
    gap = 24
    max_bar_width = 480
    max_value = max(row.value for row in analysis.rows)

    bars = []
    for index, row in enumerate(analysis.rows):
        y = top + index * (bar_height + gap)
        bar_width = round((row.value / max_value) * max_bar_width)
        bars.append(
            f'<text x="36" y="{y + 23}" font-size="18" fill="#243042">{row.period}</text>'
            f'<rect x="{left}" y="{y}" width="{bar_width}" height="{bar_height}" '
            f'rx="4" fill="#2563eb" />'
            f'<text x="{left + bar_width + 16}" y="{y + 23}" font-size="18" '
            f'fill="#243042">{row.value}</text>'
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="#ffffff" />
  <text x="36" y="38" font-size="26" font-family="Arial, sans-serif" font-weight="700" fill="#111827">{analysis.company} {analysis.metric.title()} - {analysis.market}</text>
  <g font-family="Arial, sans-serif">
    {''.join(bars)}
  </g>
</svg>
"""

    output_path.write_text(svg, encoding="utf-8")
    return output_path
