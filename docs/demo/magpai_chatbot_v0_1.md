# MAGPAI Chatbot - v0.1

## Purpose

The MAGPAI chatbot starts with a business outcome instead of theory. It answers a tiny business question, generates a chart, and exposes the internal pipeline that produced the answer.

This is not a production chatbot. MAGPAI v0.1 is intentionally tiny, visible, and explainable.

## Demo Command

Interactive:

```powershell
python -m magpai.chatbot
```

Non-interactive:

```powershell
python -m magpai.chatbot --question "are mag sales up in Chicago?"
```

Trace mode:

```powershell
python -m magpai.chatbot --trace --question "are mag sales up in Chicago?"
```

## VS Code Debugging

Use the VS Code launch configuration:

```text
MAGPAI - Chatbot
```

Set breakpoints anywhere in the chatbot pipeline and start that configuration. VS Code launches the module through the Python debugger and waits at `MAGPAI>`.

For trace mode, use:

```text
MAGPAI - Chatbot Trace
```

## Expected Output

By default, the chatbot prints:

- startup banner
- `MAGPAI>` prompt
- final response

With `--trace`, the chatbot also prints:

- thinking trace
- token list
- vector representation
- tiny neural network input shape
- detected intent and entities
- retrieved sales data
- chart path

## Pipeline Diagram

```text
User Question
   ->
Tokenizer
   ->
Vectorizer / Embedding Table
   ->
Tiny Neural Network Classifier
   ->
Intent + Entities
   ->
Tiny Sales Dataset
   ->
Response Generator
   ->
Chart Generator
```

## Why Start With The Chatbot Experience

The audience first sees the business result:

```text
Yes. MAG sales are up in Chicago.
```

Then the demo rewinds and reveals how the answer was produced. This creates a stronger learning moment because the audience sees both the useful assistant behavior and the internal mechanics.

## Why MAGPAI v0.1 Is Tiny

The small implementation makes each step inspectable:

- hard-coded tokenizer
- hard-coded embedding table
- tiny neural-network-like classifier
- tiny sales dataset
- simple chart generator

The goal is understanding, not production completeness.

## Generated Chart

Default output:

```text
output/magpai_chicago_sales_chart_v0_1.png
```
