# MAGPAI Session 1 - Question to Chart-Backed Answer - v1.2

## Demo Title

From Question to Tokens to Chart-Backed Answer - v1.0

## Session Theme

How a Business Question Becomes a Data-Backed Answer

## Guiding Architecture

```text
Diavgeia hosts the knowledge.
PowerPoint delivers the performance.
GitHub preserves the source.
VS Code runs the demos.
```

## Canonical Question

```text
Are MAG sales up in Chicago?
```

Where:

```text
MAG = Mark Anthony Group
sales = business metric
up = trend question
Chicago = market/location
```

## Core Concept

MAGPAI should not imply that the model magically knows the data.

The honest enterprise flow is:

```text
Question -> Tokens -> Token IDs -> Embedding Vectors -> Structured Request -> Data Tool -> Analysis Tool -> Chart Tool -> Answer
```

## Demonstratable Artifacts

| Artifact | Purpose |
|---|---|
| `diavgeia/MAGPAI/Session1/00_Session1_Teleprompter_Index.md` | Diavgeia teleprompter index with one page per slide/demo cue |
| `pptx/Session_01_Tokens_v1.0.pptx` | Formal PowerPoint delivery deck |
| `src/magpai/tokenization/token_demo.py` | Command-line tokenization demo |
| `src/magpai/tokenization/token_streamlit_app.py` | Streamlit visual demo |
| `src/magpai/embeddings/embedding_lookup_linear_algebra_demo.py` | Embedding lookup and linear algebra demo |
| `src/magpai/tools/chart_answer_demo.py` | End-to-end chart-backed business answer demo |
| `data/mag_sales_demo.csv` | Tiny source-of-truth CSV for the business answer demo |

## Presenter Workflow

Use `diavgeia/MAGPAI/Session1/` as the second-screen Diavgeia teleprompter while PowerPoint, VS Code, terminal output, and Streamlit are shared on the main screen.

Preparation loop:

```text
Update the matching Diavgeia slide page
Update the matching PowerPoint slide
Update source code demos when needed
Export to DiavgeiaVault
Rehearse from Diavgeia as the teleprompter
```

Default export command:

```powershell
.\scripts\export-diavgeia-vault.ps1
```

Default vault target:

```text
D:\DiavgeiaVault\Engineering\MAGPAI\Session1
```

## Run Commands

```powershell
pip install -r requirements\session_01_tokens.txt
$env:PYTHONPATH="src"
python -m magpai.tokenization.token_demo
python -m magpai.embeddings.embedding_lookup_linear_algebra_demo
python -m magpai.tools.chart_answer_demo
streamlit run src\magpai\tokenization\token_streamlit_app.py
```

## Audience Takeaway

MAGPAI does not answer from memory. It converts language into structure, then uses data and tools to produce a chart-backed answer.
