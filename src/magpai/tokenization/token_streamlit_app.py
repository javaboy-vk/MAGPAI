"""
============================================================
Module Name : token_streamlit_app.py
Author      : javaboy-vk
Date        : 2026-05-22
Version     : 1.1
Description : Streamlit visualization showing how text becomes tokens,
              token IDs, and vectors using the MAGPAI package namespace.
============================================================
"""

import pandas as pd
import streamlit as st
import torch

from magpai.tokenization.manual_tokenizer import ManualTokenizer, build_demo_vocab


# ------------------------------------------------------------
# 1. Page setup
# ------------------------------------------------------------

st.set_page_config(
    page_title="MAGPAI Session 1 - Tokens",
    page_icon="🧠",
    layout="wide",
)

st.title("MAGPAI Session 1 — From Sentence to Tokens to Vectors")
st.subheader("How Text Becomes Numbers")

st.markdown(
    """
    This demo shows the first transformation in a language AI system:

    **Text → Tokens → Token IDs → Embedding Vectors → Neural Network Input**
    """
)


# ------------------------------------------------------------
# 2. Vocabulary and tokenizer
# ------------------------------------------------------------

vocab = build_demo_vocab()
tokenizer = ManualTokenizer(vocab)


# ------------------------------------------------------------
# 3. Input
# ------------------------------------------------------------

sentence = st.text_input(
    "Enter a sentence using the demo vocabulary:",
    "Are MAG sales up in Chicago?",
)

try:
    result = tokenizer.encode(sentence)
except ValueError as error:
    st.error(str(error))
    st.info(f"Allowed vocabulary: {list(vocab.keys())}")
    st.stop()


# ------------------------------------------------------------
# 4. Embeddings
# ------------------------------------------------------------

torch.manual_seed(7)

embedding = torch.nn.Embedding(
    num_embeddings=len(vocab),
    embedding_dim=4,
)

vectors = embedding(torch.tensor(result.token_ids))


# ------------------------------------------------------------
# 5. Display transformation pipeline
# ------------------------------------------------------------

st.markdown("## Transformation Pipeline")

st.code(
    f"""
Text:
{result.original_text}

Normalized text:
{result.normalized_text}

Tokens:
{result.tokens}

Token IDs:
{result.token_ids}

Embedding vectors:
Each token ID is used as an index into the embedding table.
""",
    language="text",
)


# ------------------------------------------------------------
# 6. Table view
# ------------------------------------------------------------

rows = []

for token, token_id, vector in zip(result.tokens, result.token_ids, vectors):
    rows.append(
        {
            "Token": token,
            "Token ID": token_id,
            "Vector": [round(value.item(), 4) for value in vector],
        }
    )

df = pd.DataFrame(rows)

st.markdown("## Word → Token ID → Vector")
st.dataframe(df, use_container_width=True)


# ------------------------------------------------------------
# 7. Embedding lookup explanation
# ------------------------------------------------------------

st.markdown("## How Token ID 1 Becomes a Vector")

st.code(
    """
Token:      are
Token ID:   1
Lookup:     embedding_table[1]
Result:     row 1 of the embedding matrix
    """.strip(),
    language="text",
)


# ------------------------------------------------------------
# 8. Conceptual takeaway
# ------------------------------------------------------------

st.markdown("## Audience Takeaway")

st.success(
    "MAGPAI does not answer from memory. It converts language into structure, "
    "then uses data and tools to produce a chart-backed answer."
)
