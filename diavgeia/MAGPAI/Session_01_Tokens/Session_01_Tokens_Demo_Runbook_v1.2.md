# MAGPAI Session 1 - Demo Runbook - v1.2

## Purpose

Run the Session 1 demos from the existing MAGPAI package structure.

## Setup

From the repository root:

```powershell
pip install -r requirements\session_01_tokens.txt
$env:PYTHONPATH="src"
```

## Demo 1 - Tokenization Pipeline

```powershell
python -m magpai.tokenization.token_demo
```

Show:

1. Original sentence
2. Normalized sentence
3. Tokens
4. Token IDs
5. Embedding vectors

## Demo 2 - Embedding Lookup and Linear Algebra

```powershell
python -m magpai.embeddings.embedding_lookup_linear_algebra_demo
```

Show:

1. Embedding table shape
2. Token ID lookup
3. One-hot vector
4. One-hot vector times embedding matrix
5. Equivalence between lookup and matrix multiplication

## Demo 3 - Streamlit Visualization

```powershell
streamlit run src\magpai\tokenization\token_streamlit_app.py
```

Show:

1. Text input
2. Transformation pipeline
3. Word → Token ID → Vector table
4. Audience takeaway
