# Sentence Embedding Demo

Type one sentence per line. The demo converts each sentence into a small teaching embedding and compares sentence similarity.

<div class="magpai-demo">
  <label class="magpai-label" for="embedding-input">Input sentences</label>
  <textarea id="embedding-input" class="magpai-textarea" rows="5">the cat sits on a mat
the dog plays on the grass
AI research is super fun</textarea>

  <section class="magpai-panel">
    <h2>Sentence Embeddings</h2>
    <div id="embedding-output"></div>
  </section>

  <section class="magpai-panel">
    <h2>Cosine Similarity in Vector Space</h2>
    <p class="plot-note">
      The graph compares the first two sentences. The original embeddings are 6-dimensional, so this 2D view preserves the angle between them.
    </p>
    <canvas id="cosine-plot" class="embedding-plot" width="1100" height="520"></canvas>
    <div id="cosine-summary" class="cosine-summary"></div>
  </section>

  <section class="magpai-panel">
    <h2>Interpretation</h2>
    <div id="cosine-interpretation"></div>
  </section>

  <section class="magpai-panel">
    <h2>Model Used</h2>
    <p>
      This page does not call a production embedding model. It uses a tiny teaching model implemented directly in browser JavaScript so the mechanics are visible and the demo works inside MkDocs.
    </p>
    <p>
      Each known word maps to a handcrafted 6-dimensional vector:
    </p>
    <ol>
      <li>animal / living</li>
      <li>movement / action</li>
      <li>place / nature</li>
      <li>technology</li>
      <li>research / abstract</li>
      <li>positive tone</li>
    </ol>
    <p>
      A sentence embedding is the average of its non-stopword token vectors, normalized to unit length. That gives a small, inspectable vector that is useful for teaching cosine similarity.
    </p>
    <p>
      Size: 12 known vocabulary entries by 6 dimensions, or 72 stored numeric weights. Real embedding models usually have vocabularies with tens or hundreds of thousands of tokens and embedding dimensions such as 384, 768, 1,536, or larger.
    </p>
  </section>
</div>

<style>
  .magpai-demo {
    display: grid;
    gap: 1rem;
  }

  .magpai-label {
    font-weight: 700;
  }

  .magpai-textarea {
    box-sizing: border-box;
    width: 100%;
    padding: 0.8rem;
    border: 1px solid var(--md-default-fg-color--lighter);
    border-radius: 0.35rem;
    font: inherit;
  }

  .magpai-panel {
    padding: 0.9rem;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.35rem;
    background: var(--md-code-bg-color);
  }

  .magpai-panel h2 {
    margin-top: 0;
    font-size: 0.95rem;
  }

  .embedding-card {
    display: grid;
    gap: 0.5rem;
    padding: 0.75rem 0;
    border-bottom: 1px solid var(--md-default-fg-color--lightest);
  }

  .embedding-card:last-child {
    border-bottom: 0;
  }

  .embedding-sentence {
    font-weight: 700;
  }

  .embedding-vector {
    font-family: var(--md-code-font-family);
    font-size: 0.85rem;
  }

  .plot-note {
    margin-top: -0.25rem;
    color: var(--md-default-fg-color--light);
  }

  .embedding-plot {
    display: block;
    width: 100%;
    max-width: 100%;
    height: auto;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.35rem;
    background: rgba(10, 18, 34, 0.06);
  }

  .cosine-summary {
    margin-top: 0.85rem;
    font-size: 1.05rem;
    font-weight: 700;
  }

  .cosine-summary strong {
    color: #2d9cff;
  }

  .interpretation-list {
    margin: 0.5rem 0 1rem;
  }

  .interpretation-list dt {
    float: left;
    min-width: 3.2rem;
    font-weight: 700;
  }

  .interpretation-list dd {
    margin-left: 3.8rem;
    margin-bottom: 0.25rem;
  }

  .bar-row {
    display: grid;
    grid-template-columns: 7rem 1fr 4rem;
    align-items: center;
    gap: 0.5rem;
  }

  .bar-track {
    height: 0.8rem;
    border-radius: 0.25rem;
    background: rgba(127, 127, 127, 0.18);
    overflow: hidden;
  }

  .bar-fill {
    height: 100%;
    border-radius: 0.25rem;
    background: #2d9cff;
  }

  .sentence-pattern {
    display: inline-block;
    padding: 0.35rem 0.55rem;
    border-radius: 0.35rem;
    background: rgba(45, 156, 255, 0.12);
    font-family: var(--md-code-font-family);
  }
</style>

<script>
  (() => {
    const dimensions = [
      "animal / living",
      "movement / action",
      "place / nature",
      "technology",
      "research / abstract",
      "positive tone",
    ];

    const lexicon = new Map([
      ["cat", [0.95, 0.25, 0.20, 0.00, 0.05, 0.25]],
      ["dog", [0.92, 0.35, 0.25, 0.00, 0.05, 0.30]],
      ["sits", [0.25, 0.45, 0.25, 0.00, 0.05, 0.10]],
      ["plays", [0.30, 0.80, 0.35, 0.00, 0.05, 0.50]],
      ["mat", [0.10, 0.05, 0.65, 0.00, 0.02, 0.05]],
      ["grass", [0.25, 0.15, 0.90, 0.00, 0.05, 0.20]],
      ["ai", [0.00, 0.05, 0.00, 0.95, 0.80, 0.35]],
      ["artificial", [0.00, 0.05, 0.00, 0.85, 0.75, 0.20]],
      ["intelligence", [0.00, 0.05, 0.00, 0.80, 0.85, 0.25]],
      ["research", [0.00, 0.05, 0.00, 0.55, 0.95, 0.30]],
      ["super", [0.00, 0.05, 0.00, 0.10, 0.10, 0.80]],
      ["fun", [0.05, 0.25, 0.05, 0.10, 0.10, 0.95]],
    ]);

    const stopWords = new Set(["the", "a", "an", "on", "is", "are", "to", "of", "and", "in"]);

    function normalize(text) {
      return text
        .toLowerCase()
        .replace(/[^a-z0-9\s]/g, " ")
        .replace(/\s+/g, " ")
        .trim();
    }

    function tokenize(text) {
      const normalized = normalize(text);
      return normalized ? normalized.split(" ") : [];
    }

    function fallbackVector(token) {
      let hash = 0;
      for (const character of token) {
        hash = (hash * 33 + character.charCodeAt(0)) >>> 0;
      }
      return dimensions.map((_, index) => (((hash >> (index * 4)) & 15) / 15) * 0.18);
    }

    function sentenceVector(sentence) {
      const vectors = tokenize(sentence)
        .filter((token) => !stopWords.has(token))
        .map((token) => lexicon.get(token) || fallbackVector(token));

      if (!vectors.length) {
        return dimensions.map(() => 0);
      }

      const averaged = dimensions.map((_, index) =>
        vectors.reduce((sum, vector) => sum + vector[index], 0) / vectors.length
      );

      const magnitude = Math.hypot(...averaged) || 1;
      return averaged.map((value) => value / magnitude);
    }

    function cosine(a, b) {
      return a.reduce((sum, value, index) => sum + value * b[index], 0);
    }

    function format(value) {
      return value.toFixed(3);
    }

    function renderBars(vector) {
      return dimensions.map((dimension, index) => {
        const value = Math.max(0, vector[index]);
        const width = Math.round(value * 100);
        return `
          <div class="bar-row">
            <span>${dimension}</span>
            <span class="bar-track"><span class="bar-fill" style="width: ${width}%"></span></span>
            <span>${format(vector[index])}</span>
          </div>
        `;
      }).join("");
    }

    function sentenceColor(index) {
      return ["#2d9cff", "#35c46b", "#ffb020", "#b678ff", "#ff5a5f", "#15c8c8"][index % 6];
    }

    function clamp(value, min, max) {
      return Math.max(min, Math.min(max, value));
    }

    function drawArrow(context, startX, startY, endX, endY, color) {
      const angle = Math.atan2(endY - startY, endX - startX);
      const headLength = 20;

      context.strokeStyle = color;
      context.fillStyle = color;
      context.lineWidth = 7;
      context.lineCap = "round";
      context.beginPath();
      context.moveTo(startX, startY);
      context.lineTo(endX, endY);
      context.stroke();

      context.beginPath();
      context.moveTo(endX, endY);
      context.lineTo(
        endX - headLength * Math.cos(angle - Math.PI / 7),
        endY - headLength * Math.sin(angle - Math.PI / 7)
      );
      context.lineTo(
        endX - headLength * Math.cos(angle + Math.PI / 7),
        endY - headLength * Math.sin(angle + Math.PI / 7)
      );
      context.closePath();
      context.fill();
    }

    function drawCosinePlot(rows) {
      const canvas = document.getElementById("cosine-plot");
      const context = canvas.getContext("2d");
      const width = canvas.width;
      const height = canvas.height;
      const originX = 180;
      const originY = height - 120;
      const length = 345;
      const firstColor = sentenceColor(0);
      const secondColor = sentenceColor(1);
      const thirdColor = sentenceColor(2);
      const hasTwoRows = rows.length >= 2;
      const similarity = hasTwoRows ? clamp(cosine(rows[0].vector, rows[1].vector), -1, 1) : 0;
      const angle = Math.acos(similarity);
      const angleDegrees = angle * 180 / Math.PI;
      const first = { x: originX + length, y: originY };
      const second = {
        x: originX + Math.cos(angle) * length,
        y: originY - Math.sin(angle) * length,
      };
      const hasThirdRow = rows.length >= 3;
      const thirdSimilarity = hasThirdRow ? clamp(cosine(rows[0].vector, rows[2].vector), -1, 1) : 0;
      const thirdAngle = hasThirdRow ? Math.acos(thirdSimilarity) : 0;
      const thirdLength = length * 0.92;
      const third = {
        x: originX + Math.cos(thirdAngle) * thirdLength,
        y: originY - Math.sin(thirdAngle) * thirdLength,
      };

      context.clearRect(0, 0, width, height);
      context.fillStyle = getComputedStyle(document.body)
        .getPropertyValue("--md-code-bg-color")
        .trim() || "#f5f5f5";
      context.fillRect(0, 0, width, height);

      context.strokeStyle = "rgba(127, 127, 127, 0.35)";
      context.lineWidth = 3;
      context.beginPath();
      context.moveTo(70, originY);
      context.lineTo(width - 70, originY);
      context.moveTo(originX, height - 58);
      context.lineTo(originX, 70);
      context.stroke();

      context.strokeStyle = "rgba(255, 176, 32, 0.75)";
      context.lineWidth = 5;
      context.beginPath();
      context.arc(originX, originY, 95, -angle, 0);
      context.stroke();

      drawArrow(context, originX, originY, first.x, first.y, firstColor);
      drawArrow(context, originX, originY, second.x, second.y, secondColor);
      if (hasThirdRow) {
        drawArrow(context, originX, originY, third.x, third.y, thirdColor);
      }

      const textColor = getComputedStyle(document.body)
        .getPropertyValue("--md-default-fg-color")
        .trim() || "#222";
      context.fillStyle = textColor;
      context.font = "bold 24px Segoe UI, sans-serif";
      context.textAlign = "left";
      context.textBaseline = "alphabetic";
      context.fillText("Origin", originX - 35, originY + 36);
      context.fillText("Sentence 1", first.x + 20, first.y + 8);
      context.fillText("Sentence 2", second.x + 20, second.y - 12);
      if (hasThirdRow) {
        context.fillText("Sentence 3", third.x + 20, third.y - 12);
      }
      context.font = "22px Segoe UI, sans-serif";
      context.fillText(`angle = ${angleDegrees.toFixed(2)}°`, originX + 105, originY - 28);
      context.fillText(`cosine similarity = ${similarity.toFixed(4)}`, 650, 115);
      if (hasThirdRow) {
        context.fillText(`sentence 1 vs 3 = ${thirdSimilarity.toFixed(4)}`, 650, 260);
      }

      context.fillStyle = "rgba(45, 156, 255, 0.12)";
      context.fillRect(650, 145, 370, 95);
      context.fillStyle = textColor;
      context.font = "20px Segoe UI, sans-serif";
      context.fillText("Cosine similarity measures direction,", 675, 180);
      context.fillText("not raw vector length.", 675, 212);

      document.getElementById("cosine-summary").innerHTML = hasTwoRows
        ? `Cosine similarity ≈ <strong>${similarity.toFixed(4)}</strong>, or <strong>${(similarity * 100).toFixed(2)}%</strong> similar.`
        : "Enter at least two sentences to compare their embedding directions.";
    }

    function repeatedPattern(firstSentence, secondSentence) {
      const first = tokenize(firstSentence);
      const second = tokenize(secondSentence);
      const animalWords = new Set(["cat", "dog"]);
      const verbWords = new Set(["sits", "plays"]);
      const placeWords = new Set(["mat", "grass"]);
      const matchesTeachingPattern = [first, second].every((tokens) =>
        tokens.includes("the") &&
        tokens.some((token) => animalWords.has(token)) &&
        tokens.some((token) => verbWords.has(token)) &&
        tokens.includes("on") &&
        tokens.some((token) => placeWords.has(token))
      );

      return matchesTeachingPattern
        ? "That makes sense because both sentences follow the same structure: <span class=\"sentence-pattern\">the [animal] [verb] on the [surface/location]</span>."
        : "A high value means the sentences point in a similar semantic direction. A lower value means their embedding directions are farther apart.";
    }

    function renderInterpretation(rows) {
      const target = document.getElementById("cosine-interpretation");
      if (rows.length < 2) {
        target.innerHTML = "<p>Enter at least two sentences to see the cosine similarity interpretation.</p>";
        return;
      }

      const similarity = clamp(cosine(rows[0].vector, rows[1].vector), -1, 1);
      const thirdSimilarity = rows.length >= 3
        ? clamp(cosine(rows[0].vector, rows[2].vector), -1, 1)
        : null;
      const angleDegrees = Math.acos(similarity) * 180 / Math.PI;

      target.innerHTML = `
        <p><strong>Cosine similarity ≈ ${similarity.toFixed(4)}, or ${(similarity * 100).toFixed(2)}% similar.</strong></p>
        ${thirdSimilarity === null ? "" : `<p>The third sentence has cosine similarity ≈ <strong>${thirdSimilarity.toFixed(4)}</strong> against sentence 1, so it points in a much different direction.</p>`}
        <p>Interpretation:</p>
        <dl class="interpretation-list">
          <dt>1.0</dt><dd>identical direction / extremely similar meaning</dd>
          <dt>0.0</dt><dd>unrelated / orthogonal</dd>
          <dt>-1.0</dt><dd>opposite direction</dd>
        </dl>
        <p>These two embeddings have an angle of about <strong>${angleDegrees.toFixed(2)}°</strong> between them.</p>
        <p>When the angle is small, the vectors point in almost the same semantic direction.</p>
        <p>${repeatedPattern(rows[0].sentence, rows[1].sentence)}</p>
        <p>The original embeddings are 6-dimensional, so we cannot literally draw the full space on a flat screen. The plot projects the two vectors into 2D while preserving the angle between them, which is exactly what cosine similarity measures.</p>
      `;
    }

    function render() {
      const sentences = document.getElementById("embedding-input").value
        .split("\n")
        .map((sentence) => sentence.trim())
        .filter(Boolean);

      const rows = sentences.map((sentence) => ({
        sentence,
        vector: sentenceVector(sentence),
      }));

      drawCosinePlot(rows);
      renderInterpretation(rows);

      document.getElementById("embedding-output").innerHTML = rows.map((row, index) => `
        <article class="embedding-card">
          <div class="embedding-sentence">${index + 1}. ${row.sentence}</div>
          <div class="embedding-vector">[${row.vector.map(format).join(", ")}]</div>
          ${renderBars(row.vector)}
        </article>
      `).join("");

    }

    document.getElementById("embedding-input").addEventListener("input", render);
    render();
  })();
</script>
