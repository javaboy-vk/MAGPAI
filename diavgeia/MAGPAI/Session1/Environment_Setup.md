---
title: Environment Setup
tags:
  - magpai
  - session1
  - environment
  - python
  - vscode
---

# Environment Setup

This page explains how to set up a clean, project-local Python environment for MAGPAI.

The goal is:

```text
Install Python packages inside D:\GitHub\MAGPAI\.venv
Do not install MAGPAI dependencies into the global Python installation
Run the chatbot, token demos, Streamlit app, and tests from the workspace
```

## Expected Repository Location

```powershell
cd D:\GitHub\MAGPAI
```

All commands below assume the terminal is opened at the repository root.

## Python Interpreter

Use the clean machine Python only to create the project virtual environment.

Example base interpreter:

```text
P:\Python\Python313\python.exe
```

After setup, day-to-day MAGPAI work should use:

```text
D:\GitHub\MAGPAI\.venv\Scripts\python.exe
```

## Create The Project Virtual Environment

From the MAGPAI repository root:

```powershell
P:\Python\Python313\python.exe -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Verify that the active interpreter is inside the repository:

```powershell
where python
python -c "import sys; print(sys.executable)"
```

Expected result:

```text
D:\GitHub\MAGPAI\.venv\Scripts\python.exe
```

## Install Dependencies

Install dependencies into `.venv`, not into the global Python installation.

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For the smaller Session 1-only dependency set:

```powershell
python -m pip install -r requirements\session_01_tokens.txt
```

Use the full `requirements.txt` when preparing the whole MAGPAI workspace.

## VS Code Interpreter Setup

The workspace is configured to use:

```text
${workspaceFolder}\.venv\Scripts\python.exe
```

VS Code settings:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
  "python.terminal.activateEnvironment": true
}
```

If VS Code does not pick it up automatically:

1. Open Command Palette.
2. Run `Python: Select Interpreter`.
3. Choose `D:\GitHub\MAGPAI\.venv\Scripts\python.exe`.
4. Open a new terminal.

## Required Runtime Environment Variable

When running package modules from the repo root, set:

```powershell
$env:PYTHONPATH="src"
```

This allows commands like:

```powershell
python -m magpai.chatbot
```

to resolve the local `src/magpai` package.

## Run The MAGPAI Chatbot

Interactive:

```powershell
$env:PYTHONPATH="src"
python -m magpai.chatbot
```

Non-interactive:

```powershell
$env:PYTHONPATH="src"
python -m magpai.chatbot --question "are MAG sales up in Chicago?"
```

Trace mode:

```powershell
$env:PYTHONPATH="src"
python -m magpai.chatbot --trace --question "are MAG sales up in Chicago?"
```

Generated chart:

```text
output\magpai_chicago_sales_chart_v0_1.png
```

The `output/` folder is ignored by Git.

## Run Session 1 Token Demos

Tokenization pipeline:

```powershell
$env:PYTHONPATH="src"
python -m magpai.tokenization.token_demo
```

Embedding lookup and linear algebra:

```powershell
$env:PYTHONPATH="src"
python -m magpai.embeddings.embedding_lookup_linear_algebra_demo
```

Streamlit visual demo:

```powershell
$env:PYTHONPATH="src"
streamlit run src\magpai\tokenization\token_streamlit_app.py
```

## Run Tests

```powershell
$env:PYTHONPATH="src"
python -m pytest
```

Run only the chatbot test:

```powershell
$env:PYTHONPATH="src"
python -m pytest tests\test_magpai_chatbot.py -q
```

## VS Code Debugging

Use the launch configuration:

```text
MAGPAI - Chatbot
```

This runs:

```text
module: magpai.chatbot
PYTHONPATH: ${workspaceFolder}/src
```

It starts interactively and waits at:

```text
MAGPAI>
```

For trace output in the debugger, use:

```text
MAGPAI - Chatbot Trace
```

Set breakpoints in:

```text
src\magpai\chatbot.py
src\magpai\nlp\tokenizer.py
src\magpai\nlp\vectorizer.py
src\magpai\nn\tiny_classifier.py
src\magpai\data\sales_data.py
src\magpai\charts\sales_chart.py
```

Then start the `MAGPAI - Chatbot` debugger.

## Git Hygiene

The following runtime folders are ignored and should not be committed:

```text
.venv/
__pycache__/
.pytest_cache/
build/
dist/
output/
runs/
site/
```

Source files, docs, tests, and requirements files should be committed.

## Troubleshooting

### `ModuleNotFoundError: No module named 'magpai'`

Set `PYTHONPATH` from the repo root:

```powershell
$env:PYTHONPATH="src"
```

### `python` points to `P:\Python\Python313`

Activate the local environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then verify:

```powershell
python -c "import sys; print(sys.executable)"
```

### PowerShell blocks script activation

Run this for the current user if execution policy blocks `.venv` activation:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then open a new PowerShell terminal and activate again.

### Chart generation fails

Make sure dependencies are installed in `.venv`:

```powershell
python -m pip install -r requirements.txt
```

The chatbot chart uses `matplotlib`, which is listed in the root `requirements.txt`.
