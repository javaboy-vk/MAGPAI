# MAGPAI Session 1 - Tokens - v1.2

## Demo Title

From Sentence to Tokens to Vectors - v1.0

## Session Theme

How Text Becomes Numbers

## Guiding Architecture

```text
Diavgeia hosts the knowledge.
PowerPoint delivers the performance.
GitHub preserves the source.
VS Code runs the demos.
```

## Core Concept

AI models do not directly read words the way humans do.

Before a model can process language, text is transformed through this pipeline:

```text
Text → Tokens → Token IDs → Embedding Vectors → Neural Network Input
```

## Demonstratable Artifacts

| Artifact | Purpose |
|---|---|
| `pptx/Session_01_Tokens_v1.0.pptx` | Formal PowerPoint delivery deck |
| `diavgeia/MAGPAI/Session_01_Tokens/Session_01_Tokens_Obsidian_Slides_v1.2.md` | Internal Obsidian slide deck |
| `src/magpai/tokenization/token_demo.py` | Command-line tokenization demo |
| `src/magpai/tokenization/token_streamlit_app.py` | Streamlit visual demo |
| `src/magpai/embeddings/embedding_lookup_linear_algebra_demo.py` | Embedding lookup and linear algebra demo |
| `diagrams/session_01_tokens/sentence_to_tokens_to_vectors_v1.0.svg` | Visual pipeline diagram |

## Run Commands

```powershell
pip install -r requirements\session_01_tokens.txt
$env:PYTHONPATH="src"
python -m magpai.tokenization.token_demo
python -m magpai.embeddings.embedding_lookup_linear_algebra_demo
streamlit run src\magpai\tokenization\token_streamlit_app.py
```

## Audience Takeaway

A model never sees `sales` as a word. It sees a numeric pattern represented by a vector.
