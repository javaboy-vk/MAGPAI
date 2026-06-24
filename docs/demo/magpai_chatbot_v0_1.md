# MAGPAI Chatbot Demo

<div class="magpai-chatbot-demo">
  <section class="chatbot-console" aria-label="MAGPAI chatbot console">
    <div class="console-header">
      <div>
        <div class="console-title">MAGPAI - Tiny AI Business Assistant - v0.1</div>
        <div class="console-subtitle">Fictitious MAG Company AI Learning Demo</div>
      </div>
      <label class="trace-toggle">
        <input id="chatbot-trace-toggle" type="checkbox" />
        <span>Trace</span>
      </label>
    </div>

    <label class="prompt-label" for="chatbot-question">MAGPAI&gt;</label>
    <div class="prompt-row">
      <input
        id="chatbot-question"
        class="prompt-input"
        type="text"
        placeholder="Type a prompt, then click Run"
        autocomplete="off"
      />
      <button id="chatbot-run" class="run-button" type="button">Run</button>
    </div>

    <section class="response-panel" aria-live="polite">
      <h2>MAGPAI Response</h2>
      <div id="chatbot-response"></div>
    </section>
  </section>

  <section id="chatbot-trace-panel" class="trace-panel" hidden>
    <h2>MAGPAI Thinking Trace</h2>
    <ol id="trace-steps" class="trace-steps"></ol>

    <div class="trace-grid">
      <section>
        <h3>Tokens</h3>
        <pre id="trace-tokens"></pre>
      </section>
      <section>
        <h3>Vectors</h3>
        <pre id="trace-vectors"></pre>
      </section>
      <section>
        <h3>Model Output</h3>
        <pre id="trace-model"></pre>
      </section>
      <section>
        <h3>Sales Data</h3>
        <pre id="trace-data"></pre>
      </section>
    </div>
  </section>

  <section id="chatbot-chart-panel" class="chart-panel" hidden>
    <h2>Generated Chart</h2>
    <svg class="sales-chart" viewBox="0 0 1200 650" role="img" aria-labelledby="sales-chart-title sales-chart-desc">
      <title id="sales-chart-title">Chicago MAG Sales</title>
      <desc id="sales-chart-desc">Bar chart comparing last month and this month Chicago MAG sales.</desc>
      <text class="chart-title" x="600" y="54" text-anchor="middle">Chicago MAG Sales</text>
      <text class="chart-scale" x="108" y="90">1e6</text>
      <text class="chart-axis-label" x="-338" y="36" transform="rotate(-90)">Sales</text>

      <g class="chart-grid">
        <line x1="120" y1="130" x2="1160" y2="130"></line>
        <line x1="120" y1="184" x2="1160" y2="184"></line>
        <line x1="120" y1="238" x2="1160" y2="238"></line>
        <line x1="120" y1="292" x2="1160" y2="292"></line>
        <line x1="120" y1="346" x2="1160" y2="346"></line>
        <line x1="120" y1="400" x2="1160" y2="400"></line>
        <line x1="120" y1="454" x2="1160" y2="454"></line>
        <line x1="120" y1="508" x2="1160" y2="508"></line>
      </g>

      <g class="chart-ticks">
        <text x="104" y="515" text-anchor="end">0.0</text>
        <text x="104" y="461" text-anchor="end">0.2</text>
        <text x="104" y="407" text-anchor="end">0.4</text>
        <text x="104" y="353" text-anchor="end">0.6</text>
        <text x="104" y="299" text-anchor="end">0.8</text>
        <text x="104" y="245" text-anchor="end">1.0</text>
        <text x="104" y="191" text-anchor="end">1.2</text>
        <text x="104" y="137" text-anchor="end">1.4</text>
      </g>

      <line class="chart-axis" x1="120" y1="508" x2="1160" y2="508"></line>
      <line class="chart-axis" x1="120" y1="86" x2="120" y2="508"></line>

      <rect id="last-month-bar" class="chart-bar previous" x="170" y="184" width="350" height="324"></rect>
      <rect id="this-month-bar" class="chart-bar current" x="806" y="103" width="350" height="405"></rect>

      <text id="last-month-value" class="chart-value" x="345" y="164" text-anchor="middle">$1.2M</text>
      <text id="this-month-value" class="chart-value" x="981" y="83" text-anchor="middle">$1.5M</text>
      <text class="chart-category" x="345" y="546" text-anchor="middle">Last Month</text>
      <text class="chart-category" x="981" y="546" text-anchor="middle">This Month</text>
      <text id="chart-change" class="chart-change" x="600" y="620" text-anchor="middle">Change: +25% month over month</text>
    </svg>
  </section>
</div>

<style>
  .md-grid {
    max-width: 96rem;
  }

  .md-content {
    min-width: 0;
  }

  .magpai-chatbot-demo {
    display: grid;
    gap: 1rem;
  }

  .chatbot-console,
  .trace-panel,
  .chart-panel {
    padding: 1rem;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.35rem;
    background: var(--md-code-bg-color);
  }

  .console-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1rem;
  }

  .console-title {
    font-weight: 700;
  }

  .console-subtitle {
    color: var(--md-default-fg-color--light);
    font-size: 0.8rem;
  }

  .trace-toggle {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-weight: 700;
    white-space: nowrap;
  }

  .prompt-label {
    display: block;
    margin-bottom: 0.35rem;
    font-family: var(--md-code-font-family);
    font-weight: 700;
  }

  .prompt-row {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    gap: 0.5rem;
  }

  .prompt-input {
    box-sizing: border-box;
    width: 100%;
    min-width: 0;
    padding: 0.7rem;
    border: 1px solid var(--md-default-fg-color--lighter);
    border-radius: 0.35rem;
    font: inherit;
  }

  .run-button {
    padding: 0.7rem 1rem;
    border: 0;
    border-radius: 0.35rem;
    background: var(--md-primary-fg-color);
    color: var(--md-primary-bg-color);
    cursor: pointer;
    font: inherit;
    font-weight: 700;
  }

  .response-panel {
    margin-top: 1rem;
  }

  .response-panel h2,
  .trace-panel h2,
  .chart-panel h2 {
    margin: 0 0 0.75rem;
    font-size: 1rem;
  }

  .response-panel p {
    margin: 0.35rem 0;
  }

  .trace-steps {
    margin-top: 0;
  }

  .trace-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.75rem;
  }

  .trace-grid section {
    min-width: 0;
  }

  .trace-grid h3 {
    margin: 0 0 0.35rem;
    font-size: 0.9rem;
  }

  .trace-grid pre {
    box-sizing: border-box;
    overflow-x: hidden;
    min-height: 6rem;
    margin: 0;
    padding: 0.7rem;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.35rem;
    background: var(--md-default-bg-color);
    font-size: 0.75rem;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
  }

  .sales-chart {
    display: block;
    width: 100%;
    max-width: 76rem;
    margin: 0 auto;
    background: #ffffff;
    color: #111111;
  }

  .chart-title {
    font-size: 40px;
    font-weight: 800;
  }

  .chart-scale,
  .chart-ticks,
  .chart-category {
    font-size: 22px;
  }

  .chart-axis-label {
    font-size: 28px;
  }

  .chart-grid line {
    stroke: #aeb4bc;
    stroke-dasharray: 8 5;
    stroke-opacity: 0.38;
  }

  .chart-axis {
    stroke: #111111;
    stroke-width: 2;
  }

  .chart-bar.previous {
    fill: #069bff;
  }

  .chart-bar.current {
    fill: #2ca25f;
  }

  .chart-value {
    font-size: 28px;
    font-weight: 800;
  }

  .chart-change {
    fill: #186a36;
    font-size: 30px;
    font-weight: 800;
  }

  @media (max-width: 44rem) {
    .trace-grid {
      grid-template-columns: 1fr;
    }

    .console-header,
    .prompt-row {
      grid-template-columns: 1fr;
    }

    .console-header {
      display: grid;
    }

    .run-button {
      width: 100%;
    }
  }
</style>

<script>
  (() => {
    const embeddingTable = new Map([
      ["are", [0.10, 0.00, 0.00, 0.20]],
      ["mag", [0.90, 0.10, 0.10, 0.80]],
      ["sales", [0.20, 0.90, 0.10, 0.70]],
      ["up", [0.10, 0.80, 0.20, 0.60]],
      ["in", [0.00, 0.10, 0.00, 0.10]],
      ["chicago", [0.10, 0.20, 0.90, 0.75]],
    ]);

    const salesData = {
      location: "Chicago",
      metric: "sales",
      lastMonth: 1200000,
      thisMonth: 1500000,
    };

    function normalize(text) {
      return text.toLowerCase().trim();
    }

    function tokenize(text) {
      const normalized = normalize(text);
      return normalized.replace(/[!"#$%&'()*+,\-./:;<=>?@[\\\]^_`{|}~]/g, "").split(/\s+/).filter(Boolean);
    }

    function vectorize(tokens) {
      return tokens.map((token) => embeddingTable.get(token) || [0.00, 0.00, 0.00, 0.00]);
    }

    function classify(tokens) {
      const tokenSet = new Set(tokens);
      const required = ["are", "mag", "sales", "up", "in", "chicago"];
      const supported = required.every((token) => tokenSet.has(token));

      if (!supported) {
        return {
          intent: "unsupported_question",
          confidence: 0.12,
          metric: null,
          location: null,
          supported: false,
        };
      }

      return {
        intent: "sales_question",
        confidence: 0.97,
        metric: "sales",
        location: "Chicago",
        supported: true,
      };
    }

    function money(value) {
      return `$${(value / 1000000).toFixed(1)}M`;
    }

    function formatVector(vector) {
      return `[${vector.map((value) => value.toFixed(2)).join(", ")}]`;
    }

    function processQuestion(question) {
      const tokens = tokenize(question);
      const vectors = vectorize(tokens);
      const decision = classify(tokens);
      const data = decision.supported ? salesData : null;
      const changePercent = data
        ? ((data.thisMonth - data.lastMonth) / data.lastMonth) * 100
        : null;

      return { question, tokens, vectors, decision, data, changePercent };
    }

    function renderResponse(result) {
      const response = document.getElementById("chatbot-response");

      if (!result.decision.supported || !result.data) {
        response.innerHTML = `
          <p>This v0.1 chatbot currently supports the Chicago MAG sales question.</p>
          <p><code>are mag sales up in Chicago?</code></p>
        `;
        document.getElementById("chatbot-chart-panel").hidden = true;
        return;
      }

      response.innerHTML = `
        <p><strong>Yes. MAG sales are up in Chicago.</strong></p>
        <p>Chicago sales increased from ${money(result.data.lastMonth)} last month to ${money(result.data.thisMonth)} this month, which is a ${result.changePercent.toFixed(0)}% increase month over month.</p>
        <p>MAGPAI generated the chart below from the sales data.</p>
      `;

      renderChart(result);
    }

    function renderTrace(result) {
      const traceEnabled = document.getElementById("chatbot-trace-toggle").checked;
      const tracePanel = document.getElementById("chatbot-trace-panel");
      tracePanel.hidden = !traceEnabled;

      if (!traceEnabled) {
        return;
      }

      const steps = [
        "Text received",
        "Text tokenized",
        "Tokens converted to vectors",
        "Vectors entered tiny neural network",
        `Intent detected: ${result.decision.intent}`,
        `Location detected: ${result.decision.location || "not detected"}`,
        `Metric detected: ${result.decision.metric || "not detected"}`,
        result.data ? "Sales data retrieved" : "Sales data not retrieved",
        result.data ? "Chart generated" : "Chart not generated",
        "Response composed",
      ];

      document.getElementById("trace-steps").innerHTML = steps
        .map((step) => `<li>${step}</li>`)
        .join("");

      document.getElementById("trace-tokens").textContent = JSON.stringify(result.tokens);
      document.getElementById("trace-vectors").textContent = result.tokens
        .map((token, index) => `${token.padEnd(8, " ")} -> ${formatVector(result.vectors[index])}`)
        .join("\n");

      document.getElementById("trace-model").textContent = [
        `matrix shape: ${result.tokens.length} tokens x 4 dimensions`,
        `intent = ${result.decision.intent}`,
        `confidence = ${result.decision.confidence.toFixed(2)}`,
        `metric = ${result.decision.metric || "not detected"}`,
        `location = ${result.decision.location || "not detected"}`,
      ].join("\n");

      document.getElementById("trace-data").textContent = result.data
        ? [
            `last_month = ${result.data.lastMonth}`,
            `this_month = ${result.data.thisMonth}`,
            `change_percent = ${result.changePercent.toFixed(1)}`,
            "chart = browser-generated bar chart",
          ].join("\n")
        : "not retrieved";
    }

    function renderChart(result) {
      const chartPanel = document.getElementById("chatbot-chart-panel");
      chartPanel.hidden = !result.data;

      if (!result.data) {
        return;
      }

      const maxValue = Math.max(result.data.lastMonth, result.data.thisMonth);
      const chartBottom = 508;
      const maxBarHeight = 405;
      const lastHeight = (result.data.lastMonth / maxValue) * maxBarHeight;
      const thisHeight = (result.data.thisMonth / maxValue) * maxBarHeight;
      const lastBar = document.getElementById("last-month-bar");
      const thisBar = document.getElementById("this-month-bar");
      const lastLabel = document.getElementById("last-month-value");
      const thisLabel = document.getElementById("this-month-value");

      lastBar.setAttribute("y", String(chartBottom - lastHeight));
      lastBar.setAttribute("height", String(lastHeight));
      thisBar.setAttribute("y", String(chartBottom - thisHeight));
      thisBar.setAttribute("height", String(thisHeight));
      lastLabel.setAttribute("y", String(chartBottom - lastHeight - 20));
      thisLabel.setAttribute("y", String(chartBottom - thisHeight - 20));
      document.getElementById("last-month-value").textContent = money(result.data.lastMonth);
      document.getElementById("this-month-value").textContent = money(result.data.thisMonth);
      document.getElementById("chart-change").textContent =
        `Change: +${result.changePercent.toFixed(0)}% month over month`;
    }

    function runDemo() {
      const question = document.getElementById("chatbot-question").value.trim();

      if (!question) {
        document.getElementById("chatbot-response").innerHTML = "";
        document.getElementById("chatbot-trace-panel").hidden = true;
        document.getElementById("chatbot-chart-panel").hidden = true;
        return;
      }

      const result = processQuestion(question);
      renderResponse(result);
      renderTrace(result);
    }

    document.getElementById("chatbot-run").addEventListener("click", runDemo);
    document.getElementById("chatbot-question").addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        event.preventDefault();
        runDemo();
      }
    });
    document.getElementById("chatbot-trace-toggle").addEventListener("change", runDemo);
  })();
</script>
