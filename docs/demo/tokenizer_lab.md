# Tokenizer Demo

Type a sentence and inspect the teaching pipeline from text to tokens to token IDs.

<div class="magpai-demo">
  <label class="magpai-label" for="tokenizer-input">Input sentence</label>
  <textarea id="tokenizer-input" class="magpai-textarea" rows="3">Are MAG sales up in Chicago?</textarea>

  <div class="magpai-grid">
    <section class="magpai-panel">
      <h2>Normalized Text</h2>
      <pre id="normalized-output"></pre>
    </section>
    <section class="magpai-panel">
      <h2>Token IDs</h2>
      <pre id="token-id-output"></pre>
    </section>
  </div>

  <section class="magpai-panel">
    <h2>Tokens</h2>
    <div id="token-output" class="token-row"></div>
  </section>

  <section class="magpai-panel">
    <h2>Token Table</h2>
    <table class="magpai-table">
      <thead>
        <tr>
          <th>Position</th>
          <th>Token</th>
          <th>Token ID</th>
          <th>Vocabulary</th>
        </tr>
      </thead>
      <tbody id="token-table-body"></tbody>
    </table>
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

  .magpai-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
    gap: 1rem;
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

  .token-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .token-pill {
    padding: 0.35rem 0.55rem;
    border: 1px solid #2d9cff;
    border-radius: 0.35rem;
    background: rgba(45, 156, 255, 0.12);
    color: var(--md-default-fg-color);
    font-family: var(--md-code-font-family);
  }

  .magpai-table {
    width: 100%;
    border-collapse: collapse;
  }

  .magpai-table th,
  .magpai-table td {
    padding: 0.45rem;
    border-bottom: 1px solid var(--md-default-fg-color--lightest);
    text-align: left;
  }

  .known-token {
    color: #1f9d55;
    font-weight: 700;
  }

  .generated-token {
    color: #b7791f;
    font-weight: 700;
  }
</style>

<script>
  (() => {
    const demoVocab = new Map([
      ["<pad>", 0],
      ["are", 1],
      ["mag", 2],
      ["sales", 3],
      ["up", 4],
      ["in", 5],
      ["chicago", 6],
      ["?", 7],
    ]);

    function normalize(text) {
      return text
        .toLowerCase()
        .replace(/([?!.,;:])/g, " $1 ")
        .replace(/\s+/g, " ")
        .trim();
    }

    function tokenize(text) {
      const normalized = normalize(text);
      return normalized ? normalized.split(" ") : [];
    }

    function generatedId(token) {
      let hash = 0;
      for (const character of token) {
        hash = (hash * 31 + character.charCodeAt(0)) >>> 0;
      }
      return 100 + (hash % 900);
    }

    function render() {
      const input = document.getElementById("tokenizer-input").value;
      const normalized = normalize(input);
      const tokens = tokenize(input);
      const rows = tokens.map((token, index) => {
        const known = demoVocab.has(token);
        return {
          index: index + 1,
          token,
          id: known ? demoVocab.get(token) : generatedId(token),
          known,
        };
      });

      document.getElementById("normalized-output").textContent = normalized || "(empty)";
      document.getElementById("token-id-output").textContent =
        "[" + rows.map((row) => row.id).join(", ") + "]";

      document.getElementById("token-output").innerHTML = rows
        .map((row) => `<span class="token-pill">${row.token}</span>`)
        .join("");

      document.getElementById("token-table-body").innerHTML = rows
        .map((row) => `
          <tr>
            <td>${row.index}</td>
            <td><code>${row.token}</code></td>
            <td>${row.id}</td>
            <td class="${row.known ? "known-token" : "generated-token"}">
              ${row.known ? "demo vocab" : "generated"}
            </td>
          </tr>
        `)
        .join("");
    }

    document.getElementById("tokenizer-input").addEventListener("input", render);
    render();
  })();
</script>
