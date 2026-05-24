# MAGPAI – Mark Anthony Group Prototype AI – v1.0

**Pronounced:** magpie  
**Lifecycle:** Training / internal demo / educational prototype  
**Created:** 2026-05-22

MAGPAI is a tiny, transparent educational AI model and demo lab designed to explain how modern AI systems work under the covers.

MAGPAI is not intended to be a production model. It is a teaching platform for understanding, inspecting, running, visualizing, and explaining AI concepts through slides, diagrams, Python code, notebooks, and local runtime demos.

## Purpose

MAGPAI helps engineers understand:

- tokenization
- embeddings
- next-token prediction
- training loops
- loss and backpropagation
- attention
- tiny Transformers
- local inference
- observability
- enterprise AI safety

## Demo Series

| Session | Title | Main Demo |
|---:|---|---|
| 01 | Text to Tokens to Vectors | Tokenizer + embedding visualizer |
| 02 | Next Token Prediction | Probability distribution demo |
| 03 | Training Loop | Loss curve + weight update demo |
| 04 | Attention | Attention heatmap demo |
| 05 | Tiny Transformer | Mini GPT-style model |
| 06 | Local Inference | Hercules local inference gateway |
| 07 | Observability | Runtime metrics dashboard |
| 08 | Enterprise Safety | Prompt policy boundary demo |

## Repository Layout

```text
docs/       Documentation, session outlines, ADRs, glossary
slides/     PowerPoint source and exports
diagrams/   draw.io, Mermaid, SVG, PNG, PDF diagrams
notebooks/  Jupyter notebooks for teaching demos
src/        Reusable Python source code
apps/       Streamlit and FastAPI visual demo apps
tests/      Pytest test cases
data/       Small sample data and generated data
models/     Local checkpoints and model exports
runs/       TensorBoard / PyTorch runtime output
reports/    Generated coverage, profiling, and documentation reports
scripts/    Developer automation scripts
diavgeia/   Diavgeia-ready documentation entry points
```

## Quick Start

```powershell
git clone <your-repository-url>
cd MAGPAI

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

pytest
```

## Run the First Demo

```powershell
streamlit run apps/streamlit/token_visualizer_app.py
```

## Run the Chart-Backed Answer Demo

```powershell
$env:PYTHONPATH="src"
python -m magpai.tools.chart_answer_demo
```

## Run the MAGPAI Chatbot

```powershell
$env:PYTHONPATH="src"
python -m magpai.chatbot --question "are mag sales up in Chicago?"
```

Show the under-the-covers trace:

```powershell
$env:PYTHONPATH="src"
python -m magpai.chatbot --trace --question "are mag sales up in Chicago?"
```

## Documentation

Build local documentation with MkDocs:

```powershell
mkdocs serve
```

## Diavgeia Vault Export

Export the Diavgeia-ready presenter material to the local vault:

```powershell
.\scripts\export-diavgeia-vault.ps1
```

Default target:

```text
D:\DiavgeiaVault\Engineering\MAGPAI\Session1
```

## Artifact Naming Standard

Use versioned names:

```text
MAGPAI – Session 01 – Tokens to Vectors – v1.0
MAGPAI – Runtime Architecture – v1.0
MAGPAI – Tiny Transformer Model – v1.0
```

## Status

Version: 1.0  
Owner: Vasilis Katsoulis  
Scope: Educational AI demo and internal engineering learning lab
