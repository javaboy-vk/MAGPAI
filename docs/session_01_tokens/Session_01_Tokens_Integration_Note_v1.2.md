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
src/magpai/llm/structured_request_generator.py
src/magpai/tools/data_reader.py
src/magpai/tools/trend_analyzer.py
src/magpai/tools/chart_generator.py
src/magpai/tools/chart_answer_demo.py
```

## Correct Runtime Commands

From the repository root:

```powershell
pip install -r requirements\session_01_tokens.txt
$env:PYTHONPATH="src"
python -m magpai.tokenization.token_demo
python -m magpai.embeddings.embedding_lookup_linear_algebra_demo
python -m magpai.tools.chart_answer_demo
streamlit run src\magpai\tokenization\token_streamlit_app.py
```

## Architecture Principle

For internal learning, Academy, Diavgeia, and MAGPAI engineering demos, use Diavgeia presenter notes.

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

images/
  full_stack_ai_ml_mental_model_16_layers_magpai_start.png
  full_stack_ai_ml_mental_model_16_layers_science_math.png
  magpai_from_question_to_insight.png

diavgeia/MAGPAI/Session_01_Tokens/
  Session_01_Tokens_Diavgeia_Page_v1.2.md
  Session_01_Tokens_Presenter_Notes_v1.2.md
  Session_01_Tokens_Demo_Runbook_v1.2.md
  Session_01_Tokens_Speaking_Script_v1.2.md

docs/session_01_tokens/
  Session_01_Tokens_Integration_Note_v1.2.md
  Session_01_Tokens_Slide_Story_v1.2.md
  Session_01_Tokens_Embedding_Explanation_v1.2.md

data/
  mag_sales_demo.csv

diagrams/session_01_tokens/
  sentence_to_tokens_to_vectors_v1.0.svg
```

## Current Delivery Sequence

The current PowerPoint and Diavgeia teleprompter use 19 numbered slide pages:

```text
01 MAGPAI
02 Full Stack AI/ML Mental Model
03 Math & Sciences of AI/ML Layers
04 MAGPAI Session 1
05 The Big Idea
06 Starting Sentence
07 Tokenizer Step 1 - Tokens
08 What Are Tokens and Tokenizers?
09 Tokenizer Step 2 - Token IDs
10 What Is an Embedding?
11 Embedding Lookup
12 What Is a Vector?
13 How Token ID 3 Becomes a Vector
14 Linear Algebra View
15 What Is a Tensor?
16 Prompt Stored as an Input Tensor
17 From Question to Insight
18 Live Demo Path
19 Audience Takeaway
```
