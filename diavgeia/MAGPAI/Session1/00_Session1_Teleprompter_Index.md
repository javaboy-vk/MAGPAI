---
title: MAGPAI Session 1 - Teleprompter Index
tags:
  - magpai
  - session1
  - teleprompter
---

# MAGPAI Session 1 - Teleprompter Index

Use this folder as the Diavgeia teleprompter for the 45 minute demo.

Each page maps to one presentation slide or live-demo cue. Keep Diavgeia open on the presenter screen and use the PPTX, terminal, VS Code, and Streamlit on the shared screen.

## Developer Setup

| Page | Purpose |
|---|---|
| [[Environment_Setup]] | Clean project-local Python environment setup for running the chatbot, demos, and tests. |

## Slide Pages

| Order | Page | Purpose |
|---:|---|---|
| 01 | [[01_MAGPAI]] | Open the demo series and frame the promise. |
| 02 | [[02_MAGPAI_Session_1]] | Introduce Session 1 and the core idea. |
| 03 | [[03_Full_Stack_AI_ML_Mental_Model]] | Position MAGPAI Session 1 at level 6 of the AI/ML stack. |
| 04 | [[04_The_Big_Idea]] | Explain human view vs model view. |
| 05 | [[05_Starting_Sentence]] | Anchor the demo on one business sentence. |
| 06 | [[06_Tokenizer_Step_1_Tokens]] | Explain simple tokenization. |
| 07 | [[07_What_Are_Tokens_And_Tokenizers]] | Define token and tokenizer before token IDs. |
| 08 | [[08_Tokenizer_Step_2_Token_IDs]] | Explain vocabulary lookup. |
| 09 | [[09_What_Is_An_Embedding]] | Define embeddings and show a tiny embedding table. |
| 10 | [[10_Embedding_Lookup]] | Explain token IDs becoming vectors. |
| 11 | [[11_What_Is_A_Vector]] | Define vector and the sales vector lookup path. |
| 12 | [[12_How_Token_ID_3_Becomes_A_Vector]] | Explain row lookup. |
| 13 | [[13_Linear_Algebra_View]] | Explain one-hot multiplication equivalence. |
| 14 | [[14_What_Is_A_Tensor]] | Define tensor and activation tensor. |
| 15 | [[15_Prompt_Stored_As_An_Input_Tensor]] | Show the original prompt stored as a token-vector tensor. |
| 16 | [[16_From_Question_To_Insight]] | Show the full question-to-insight dashboard image. |
| 17 | [[17_Live_Demo_Path]] | Introduce the live demo path. |
| 18 | [[18_Audience_Takeaway]] | Close with the durable enterprise mental model. |

## Live Demo Support Pages

| Page | Purpose |
|---|---|
| [[Live_Demo_01_Token_Pipeline]] | Run the terminal token pipeline demo. |
| [[Live_Demo_02_Streamlit_Visualizer]] | Run the Streamlit visual demo. |
| [[Live_Demo_03_Embedding_Linear_Algebra]] | Run the embedding lookup demo. |
| [[Live_Demo_04_Chart_Backed_Answer]] | Run the end-to-end question-to-chart demo. |

## Preparation Loop

1. Update the slide page script in this folder.
2. Update the corresponding PPTX slide.
3. Update code only when the live demo needs clearer behavior.
4. Export to DiavgeiaVault.
5. Rehearse from these pages.

## Export Command

From the repository root:

```powershell
.\scripts\export-diavgeia-vault.ps1
```

Default vault target:

```text
D:\DiavgeiaVault\Engineering\MAGPAI\Session1
```
