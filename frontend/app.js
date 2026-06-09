"use strict";

// ===========================================================================
// Cenários REAIS (preços de mercado 2024–2026). Cada um é autoconsistente:
// os parâmetros foram calibrados para que o preço ótimo caia em valores reais.
// ===========================================================================
const CENARIOS = [
  {
    rotulo: "☕ Cafeteria — Café especial × Cappuccino",
    descricao:
      "Café especial (coado, grãos premium) e cappuccino disputam o mesmo cliente. Faixa real: especial ~R$ 8–10, cappuccino ~R$ 8–11. (Cenário do relatório.)",
    p1: { nome: "Café especial", a: 120, b: 12, m: 3.0 },
    p2: { nome: "Cappuccino", a: 90, b: 10, m: 2.5 },
    g: 4, F: 50,
  },
  {
    rotulo: "🍔 Hamburgueria — X-Burguer × X-Salada",
    descricao:
      "Dois lanches concorrentes no cardápio. Faixa real: X-Burguer ~R$ 20–25, X-Salada ~R$ 24–28.",
    p1: { nome: "X-Burguer", a: 63, b: 3, m: 9.0 },
    p2: { nome: "X-Salada", a: 53, b: 2.5, m: 11.0 },
    g: 1.2, F: 150,
  },
  {
    rotulo: "🍕 Pizzaria — Pizza Broto × Pizza Grande",
    descricao:
      "Mesma pizza em dois tamanhos. Faixa real: broto ~R$ 30–38, grande ~R$ 45–60.",
    p1: { nome: "Pizza Broto", a: 45, b: 1.2, m: 14.0 },
    p2: { nome: "Pizza Grande", a: 43, b: 0.8, m: 24.0 },
    g: 0.3, F: 200,
  },
  {
    rotulo: "🍧 Açaiteria — Açaí 300ml × Açaí 500ml",
    descricao:
      "Mesmo açaí em dois tamanhos. Faixa real: 300ml ~R$ 13–16, 500ml ~R$ 18–22.",
    p1: { nome: "Açaí 300ml", a: 55, b: 4, m: 6.0 },
    p2: { nome: "Açaí 500ml", a: 47, b: 3, m: 9.0 },
    g: 1.5, F: 100,
  },
  {
    rotulo: "🥤 Lanchonete — Refrigerante × Suco natural",
    descricao:
      "Duas bebidas: o cliente escolhe uma ou outra. Faixa real: refri lata ~R$ 6–8, suco natural ~R$ 9–12.",
    p1: { nome: "Refrigerante lata", a: 44, b: 6, m: 3.0 },
    p2: { nome: "Suco natural", a: 34, b: 4, m: 5.0 },
    g: 2.0, F: 70,
  },
  {
    rotulo: "🥪 Padaria — Misto quente × Pão na chapa",
    descricao:
      "Dois lanches rápidos de balcão. Faixa real: misto quente ~R$ 7–9, pão na chapa ~R$ 5–7.",
    p1: { nome: "Misto quente", a: 52, b: 7, m: 3.0 },
    p2: { nome: "Pão na chapa", a: 50, b: 8, m: 2.0 },
    g: 3.0, F: 60,
  },
];

// Formatação
const brl = (x) =>
  new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" }).format(x);
const num = (x) =>
  new Intl.NumberFormat("pt-BR", { maximumFractionDigits: 1 }).format(x);
const fmt = (x) =>
  new Intl.NumberFormat("pt-BR", { maximumFractionDigits: 2 }).format(x);

const form = document.getElementById("form");
const selectCenario = document.getElementById("cenario");
const cartaoResultado = document.getElementById("cartao-resultado");

let cenarioAtual = CENARIOS[0];

// ---- Inicialização: popular o seletor e aplicar o primeiro cenário --------
CENARIOS.forEach((c, i) => {
  const opt = document.createElement("option");
  opt.value = String(i);
  opt.textContent = c.rotulo;
  selectCenario.appendChild(opt);
});
selectCenario.addEventListener("change", () => aplicarCenario(CENARIOS[+selectCenario.value]));
aplicarCenario(CENARIOS[0]);

function aplicarCenario(c) {
  cenarioAtual = c;
  document.getElementById("leg-p1").textContent = "Produto 1 — " + c.p1.nome;
  document.getElementById("leg-p2").textContent = "Produto 2 — " + c.p2.nome;
  document.getElementById("descricao-cenario").textContent = c.descricao;
  form.elements["a1"].value = c.p1.a;
  form.elements["b1"].value = c.p1.b;
  form.elements["m1"].value = c.p1.m;
  form.elements["a2"].value = c.p2.a;
  form.elements["b2"].value = c.p2.b;
  form.elements["m2"].value = c.p2.m;
  form.elements["g"].value = c.g;
  form.elements["F"].value = c.F;
}

// ---- Envio do formulário --------------------------------------------------
form.addEventListener("submit", async (ev) => {
  ev.preventDefault();
  const btn = document.getElementById("btn-calcular");
  btn.disabled = true;
  btn.textContent = "Calculando...";

  const dados = {
    a1: parseFloat(form.elements["a1"].value),
    b1: parseFloat(form.elements["b1"].value),
    m1: parseFloat(form.elements["m1"].value),
    a2: parseFloat(form.elements["a2"].value),
    b2: parseFloat(form.elements["b2"].value),
    m2: parseFloat(form.elements["m2"].value),
    g: parseFloat(form.elements["g"].value),
    F: parseFloat(form.elements["F"].value) || 0,
    nome1: cenarioAtual.p1.nome,
    nome2: cenarioAtual.p2.nome,
  };

  try {
    const resp = await fetch("/api/otimizar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados),
    });
    if (!resp.ok) {
      const detalhe = await resp.json().catch(() => ({}));
      mostrarErro(formatarErroValidacao(detalhe));
      return;
    }
    const r = await resp.json();
    if (!r.ok) {
      mostrarErro((r.erros || ["Erro desconhecido."]).join(" "));
      return;
    }
    renderizar(r);
  } catch (e) {
    mostrarErro("Não foi possível falar com o servidor. Ele está rodando?");
  } finally {
    btn.disabled = false;
    btn.textContent = "Calcular preços ótimos";
  }
});

function formatarErroValidacao(detalhe) {
  if (detalhe && Array.isArray(detalhe.detail)) {
    return "Confira os campos: " + detalhe.detail.map((d) => (d.loc ? d.loc.slice(-1)[0] : "?")).join(", ");
  }
  return "Dados inválidos. Verifique se preencheu todos os campos com números.";
}

function mostrarErro(msg) {
  cartaoResultado.classList.remove("oculto");
  document.getElementById("avisos").innerHTML = `<div class="erro">⚠️ ${msg}</div>`;
  ["r-p1", "r-p2", "r-lucro"].forEach((id) => (document.getElementById(id).textContent = "—"));
  document.getElementById("bloco-grafico").classList.add("oculto");
  cartaoResultado.scrollIntoView({ behavior: "smooth" });
}

// ---- Renderização do resultado -------------------------------------------
function renderizar(r) {
  cartaoResultado.classList.remove("oculto");
  const s = r.solucao;
  const nome1 = r.nomes.p1;
  const nome2 = r.nomes.p2;

  // Cards principais
  document.getElementById("rot-p1").textContent = "Preço ideal — " + nome1;
  document.getElementById("rot-p2").textContent = "Preço ideal — " + nome2;
  document.getElementById("r-p1").textContent = brl(s.p1);
  document.getElementById("r-p2").textContent = brl(s.p2);
  document.getElementById("r-lucro").textContent = brl(s.lucro);
  document.getElementById("r-q1").textContent = `~${num(s.q1)} un./dia`;
  document.getElementById("r-q2").textContent = `~${num(s.q2)} un./dia`;
  document.getElementById("r-classificacao").textContent =
    s.classificacao === "maximo" ? "✔ ponto de máximo confirmado" : `(${s.classificacao})`;

  // Avisos
  document.getElementById("avisos").innerHTML =
    (r.avisos || []).map((a) => `<div class="aviso">⚠️ ${a}</div>`).join("");

  // Matemática (LaTeX) — injeta com delimitadores \[ \] e \( \)
  const m = r.modelo;
  const h = s.hessiana_num;
  document.getElementById("m-legenda-vars").innerHTML =
    `Aqui, \\(p_1\\) = preço de <strong>${nome1}</strong> e \\(p_2\\) = preço de <strong>${nome2}</strong>.`;
  setMath("m-demanda", `\\[ q_1 = ${m.q1_latex} \\qquad q_2 = ${m.q2_latex} \\]`);
  setMath("m-lucro", `\\[ ${m.lucro_latex} \\]`);
  setMath("m-grad1", `\\[ ${m.grad_latex[0]} \\]`);
  setMath("m-grad2", `\\[ ${m.grad_latex[1]} \\]`);
  setMath("m-hess", `\\[ ${m.hessiana_latex} \\]`);

  const sinalD = s.det_hessiana > 0 ? ">" : s.det_hessiana < 0 ? "<" : "=";
  const conclusao =
    s.classificacao === "maximo" ? "<strong>MÁXIMO de lucro</strong>" : `<strong>${s.classificacao}</strong>`;
  document.getElementById("m-teste").innerHTML =
    `Pelo teste da segunda derivada, \\(D = f_{xx}\\,f_{yy} - (f_{xy})^2 = ${fmt(s.det_hessiana)} ${sinalD} 0\\) ` +
    `e \\(f_{xx} = ${fmt(h[0][0])}\\). Logo, o ponto crítico é um ${conclusao}.`;

  // Justificativa textual
  document.getElementById("r-justificativa").textContent = r.justificativa;

  // Tipografar as fórmulas e desenhar o gráfico
  typesetMath();
  desenharGrafico(r);

  cartaoResultado.scrollIntoView({ behavior: "smooth" });
}

function setMath(id, tex) {
  document.getElementById(id).textContent = tex;
}

// Tipografa as fórmulas, esperando o MathJax terminar de carregar
function typesetMath() {
  if (!window.MathJax) return;
  const run = () => window.MathJax.typesetPromise && window.MathJax.typesetPromise();
  if (window.MathJax.startup && window.MathJax.startup.promise) {
    window.MathJax.startup.promise.then(run).catch(() => {});
  } else {
    run();
  }
}

// ---- Mapa de lucro (curvas de nível) com Plotly --------------------------
function desenharGrafico(r) {
  const bloco = document.getElementById("bloco-grafico");
  const g = r.grafico;
  if (!g || typeof Plotly === "undefined") {
    bloco.classList.add("oculto");
    return;
  }
  bloco.classList.remove("oculto");

  const s = r.solucao;
  const nome1 = r.nomes.p1;
  const nome2 = r.nomes.p2;

  const dados = [
    {
      type: "contour",
      x: g.p1,
      y: g.p2,
      z: g.z,
      colorscale: "YlOrBr",
      contours: { coloring: "heatmap" },
      colorbar: { title: { text: "Lucro (R$)", side: "right" } },
      hovertemplate: `${nome1}: R$ %{x:.2f}<br>${nome2}: R$ %{y:.2f}<br>Lucro: R$ %{z:.2f}<extra></extra>`,
    },
    {
      type: "scatter",
      x: [s.p1],
      y: [s.p2],
      mode: "markers+text",
      marker: { color: "#b3261e", size: 16, symbol: "star", line: { color: "#fff", width: 1 } },
      text: ["ótimo"],
      textposition: "top center",
      textfont: { color: "#b3261e", size: 13 },
      hovertemplate: `Ótimo<br>${nome1}: R$ ${fmt(s.p1)}<br>${nome2}: R$ ${fmt(s.p2)}<extra></extra>`,
      showlegend: false,
    },
  ];

  const layout = {
    margin: { t: 10, r: 10, b: 55, l: 65 },
    xaxis: { title: { text: `Preço — ${nome1} (R$)` } },
    yaxis: { title: { text: `Preço — ${nome2} (R$)` } },
    paper_bgcolor: "transparent",
  };

  Plotly.newPlot("grafico", dados, layout, { responsive: true, displayModeBar: false });
}
