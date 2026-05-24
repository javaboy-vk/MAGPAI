---
title: Slide 11 - Demo Cue - Streamlit Visualizer
tags:
  - magpai
  - session1
  - teleprompter
  - live-demo
slide: 11
---

# Slide 11 - Demo Cue - Streamlit Visualizer

## Slide Intent

Cue the interactive Streamlit demo.

## Shared Screen

Browser window running Streamlit.

## Command

```powershell
streamlit run src\magpai\tokenization\token_streamlit_app.py
```

## Say This Before Running

Now I am switching to the visual version of the same pipeline.

The goal here is to make the mapping easier to scan: token, token ID, and vector side by side.

Use the canonical question:

```text
Are MAG sales up in Chicago?
```

## Point At These UI Areas

- Text input: the sentence being transformed.
- Transformation pipeline: the same sequence from the slides.
- Table: token to token ID to vector.
- Error behavior: if we enter a word outside the small demo vocabulary, the app tells us.

## Say This During The Demo

The vocabulary is intentionally small. That keeps the example controlled.

If this were a production tokenizer, the vocabulary would be much larger and the tokenization rules would be more sophisticated.

But the teaching point is the same: the model does not receive raw text. It receives numeric representations.

## Transition

Now I will show the embedding lookup from the linear algebra angle.
