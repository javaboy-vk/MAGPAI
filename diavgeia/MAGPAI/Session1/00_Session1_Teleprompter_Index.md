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
| 02 | [[02_Full_Stack_AI_ML_Mental_Model]] | Position MAGPAI Session 1 at level 6 of the AI/ML stack. |
| 03 | [[03_Math_Sciences_Of_AI_ML_Layers]] | Show the math and sciences behind the AI/ML layers. |
| 04 | [[04_MAGPAI_Session_1]] | Introduce Session 1 and the core idea. |
| 05 | [[05_The_Big_Idea]] | Explain human view vs model view. |
| 06 | [[06_Starting_Sentence]] | Anchor the demo on one business sentence. |
| 07 | [[07_Tokenizer_Step_1_Tokens]] | Explain simple tokenization. |
| 08 | [[08_What_Are_Tokens_And_Tokenizers]] | Define token and tokenizer before token IDs. |
| 8.A | [[8.A_Tokenizer Lab Demo]] | Run the Tokenizer Lab demo from the site. |
| 09 | [[09_Tokenizer_Step_2_Token_IDs]] | Explain vocabulary lookup. |
| 10 | [[10_What_Is_A_Vector]] | Define vector and the sales vector lookup path. |
| 10.A | [[10.A_Embedding-Lab-Demo]] | Show how selected vector dimensions appear as arrows on a 2D Cartesian diagram. |
| 11 | [[11_How_Token_ID_3_Becomes_A_Vector]] | Explain row lookup. |
| 12 | [[12_What_Is_An_Embedding]] | Define embeddings and show a tiny embedding table. |
| 13 | [[13_Embeddings_Learned_Geometric_Coordinates_Of_Meaning]] | Explain training, vector geometry, analogies, and sentence embeddings. |
| 14 | [[14_Embedding_Lookup]] | Explain token IDs retrieving learned vectors. |
| 14.A | [[14.A_Vocabulary_training_demo]] | Run the text vocabulary training demo from the site. |
| 14.B | [[14.B_Visual_Vocabulary_training_demo]] | Run the visual vocabulary training demo from the site. |
| 15 | [[15_Embeddings_Become_Neural_Network_Activations]] | Explain embeddings becoming live neural-network activations. |
| 16 | [[16_The_Transformer_ANN_Is_The_LLM_Core]] | Explain that the Transformer ANN is the LLM computational core. |
| 16.A | [[16A_Neural_Language_Models_Transformers_Parameters]] | Summarize LLMs as neural language models plus Transformers plus billions of parameters. |
| 18 | [[18_What_Is_A_Tensor]] | Define tensor and activation tensor. |
| 19 | [[19_Prompt_Stored_As_An_Input_Tensor]] | Show the original prompt stored as a token-vector tensor. |
| 20 | [[20_From_Question_To_Insight]] | Show the full question-to-insight dashboard image. |
| 20.A | [[20.A_Neural Network Training v1]] | Run the first neural-network training demo. |
| 20.B | [[20.B_Neural Network Training v2]] | Run the second neural-network training demo. |
| 20.C | [[20.C_Vision Neural Network Training]] | Run the vision neural-network training demo. |
| 20.D | [[20.D_Chatbot Demo]] | Run the chatbot demo. |
| 20.E | [[20.E_Agent Demo]] | Run the agent demo. |

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
