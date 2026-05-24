---
title: Live Demo 04 - Chart-Backed Answer
tags:
  - magpai
  - session1
  - teleprompter
  - live-demo
---

# Live Demo 04 - Chart-Backed Answer

## Slide Intent

Cue the end-to-end business assistant demo.

## Shared Screen

VS Code terminal at the repository root.

## Command

```powershell
$env:PYTHONPATH="src"
python -m magpai.tools.chart_answer_demo
```

## Say This Before Running

Now I am connecting the language pipeline to a tiny enterprise-style data flow.

The question is:

```text
Are MAG sales up in Chicago?
```

I do not want to say the model magically knows the answer. The honest architecture is that MAGPAI converts the question into a structured data request, reads a tiny CSV, calculates the trend, and asks a chart tool to create the answer artifact.

## Point At These Output Blocks

- `Question`: the natural language input.
- `Structured request`: intent, company, metric, market, comparison, output.
- `Data source`: the CSV used as source of truth.
- `Generated chart`: the small chart created from the data.
- `MAGPAI answer`: the text answer backed by the calculation.
- `Chart artifact`: the generated SVG chart path.

## Say This After Running

This is the enterprise point:

```text
LLM-style layer: understands and structures the question.
Data tool: reads the source of truth.
Analysis tool: calculates the trend.
Chart tool: creates the artifact.
```

The model does not hallucinate the chart. The chart is generated from data.

## Transition

Now I will close with the bigger mental model for the team.
