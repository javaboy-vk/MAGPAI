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
| 01 | [[01_Title_AI_Under_The_Covers]] | Open the demo series and frame the promise. |
| 02 | [[02_Session_Title_Text_To_Vectors]] | Introduce Session 1 and the core idea. |
| 03 | [[03_Big_Idea_Text_To_Numbers]] | Explain human view vs model view. |
| 04 | [[04_Starting_Sentence]] | Anchor the demo on one business sentence. |
| 05 | [[05_Tokenizer_Step_1_Tokens]] | Explain simple tokenization. |
| 06 | [[06_Tokenizer_Step_2_Token_IDs]] | Explain vocabulary lookup. |
| 07 | [[07_Embedding_Lookup]] | Explain token IDs becoming vectors. |
| 08 | [[08_Token_ID_1_To_Vector]] | Explain row lookup. |
| 09 | [[09_Linear_Algebra_View]] | Explain one-hot multiplication equivalence. |
| 10 | [[10_Demo_Cue_Token_Demo]] | Run the terminal token pipeline demo. |
| 11 | [[11_Demo_Cue_Streamlit_Visualizer]] | Run the Streamlit visual demo. |
| 12 | [[12_Demo_Cue_Embedding_Linear_Algebra]] | Run the embedding lookup demo. |
| 13 | [[13_Demo_Cue_Chart_Backed_Answer]] | Run the end-to-end question-to-chart demo. |
| 14 | [[14_Audience_Takeaway]] | Close with the durable enterprise mental model. |

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
