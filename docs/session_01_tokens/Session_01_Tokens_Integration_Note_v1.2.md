# MAGPAI Session 1 - Repository Integration Note - v1.2

## Correction

The Session 1 files must not create a parallel `src/session_01_tokens/` structure.
The existing MAGPAI source tree already uses a package-oriented layout:

```text
src/magpai/
  attention/
  common/
  embeddings/
  gateway/
  inference/
  prediction/
  safety/
  tokenization/
  training/
  transformer/
```

Therefore, Session 1 should integrate into the existing package namespace.

## Correct Source Placement

```text
src/magpai/tokenization/manual_tokenizer.py
src/magpai/tokenization/token_demo.py
src/magpai/tokenization/token_streamlit_app.py
src/magpai/embeddings/embedding_lookup_linear_algebra_demo.py
```

## Correct Runtime Commands

From the repository root:

```powershell
pip install -r requirements\session_01_tokens.txt
$env:PYTHONPATH="src"
python -m magpai.tokenization.token_demo
python -m magpai.embeddings.embedding_lookup_linear_algebra_demo
streamlit run src\magpai\tokenization\token_streamlit_app.py
```

## Architecture Principle

For internal learning, Academy, Diavgeia, and MAGPAI engineering demos, use Obsidian slides.

For formal delivery to Mark Anthony leadership or broad corporate audiences, use PowerPoint.

The standardized model is:

```text
Diavgeia hosts the knowledge.
PowerPoint delivers the performance.
GitHub preserves the source.
VS Code runs the demos.
```

## Artifact Placement

```text
pptx/Session_01_Tokens_v1.0.pptx

diavgeia/MAGPAI/Session_01_Tokens/
  Session_01_Tokens_Diavgeia_Page_v1.2.md
  Session_01_Tokens_Obsidian_Slides_v1.2.md
  Session_01_Tokens_Demo_Runbook_v1.2.md
  Session_01_Tokens_Speaking_Script_v1.2.md

docs/session_01_tokens/
  Session_01_Tokens_Integration_Note_v1.2.md
  Session_01_Tokens_Slide_Story_v1.2.md
  Session_01_Tokens_Embedding_Explanation_v1.2.md

diagrams/session_01_tokens/
  sentence_to_tokens_to_vectors_v1.0.svg
```
