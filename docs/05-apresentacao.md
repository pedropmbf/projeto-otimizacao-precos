# Slides — Café & Cálculo (10 slides de conteúdo)

> **Para gerar no Gamma.** Estes são os **10 slides de conteúdo** sobre o
> funcionamento e a implementação técnica/matemática do projeto. **Capa**, **demo
> ao vivo** e **declaração de uso de IA** serão adicionados por você à parte.
> As fórmulas usam símbolos comuns (π, ∇, ∂, ², ₁, ₂) para colar sem problema no
> Gamma. Cada slide traz o conteúdo + uma sugestão de fala.

---

## Slide 1 — O problema: dois preços que se influenciam

**Ideia central:** precificar **dois produtos que competem pelo mesmo cliente**
(produtos *substitutos* — o cliente compra um **ou** o outro).

- Exemplos reais: café especial × cappuccino; X-Burguer × X-Salada; pizza broto ×
  grande.
- O preço de um **afeta a venda do outro**: baixar o preço do café "rouba" clientes
  do cappuccino.
- Por isso **não** dá para otimizar um preço de cada vez — as duas decisões estão
  ligadas. É um problema de **otimização de função de duas variáveis**.

> **Fala:** "Todo comércio com itens parecidos enfrenta isso: mexer no preço de um
> mexe na venda do outro. Tratamos os dois preços juntos."

---

## Slide 2 — As variáveis de entrada

**Dois tipos de número.**

**Variáveis de decisão (o que calculamos):**
- **p₁** = preço do Produto 1  ·  **p₂** = preço do Produto 2

**Parâmetros (o usuário informa, descrevem o negócio):**
- **a₁, a₂** — demanda-base: quanto venderia se o preço fosse quase zero.
- **b₁, b₂** — sensibilidade ao preço próprio: vendas perdidas por +R$ 1,00 no
  próprio preço.
- **g** — efeito de substituição: vendas ganhas no outro produto por +R$ 1,00 no
  preço de um.
- **m₁, m₂** — custo de uma unidade  ·  **F** — custo fixo (opcional).

> **Fala:** "O usuário só informa números do dia a dia; o sistema cuida da
> matemática."

---

## Slide 3 — Modelando a demanda (substitutos)

**Demanda** = quantidade que o cliente compra. Para cada produto:

> q₁ = a₁ − b₁·p₁ + g·p₂
> q₂ = a₂ − b₂·p₂ + g·p₁

- O sinal **−** no próprio preço: ficou mais caro → vende **menos**.
- O sinal **+** no preço do outro: o concorrente encareceu → sobra cliente para mim
  (**substituição**).
- O coeficiente **g** mede a força dessa troca entre os produtos.

> **Fala:** "Essas duas retas traduzem em número o comportamento do cliente."

---

## Slide 4 — A função objetivo: o lucro

**Função objetivo** = o que queremos deixar o **maior** possível. Aqui, o **lucro**:

> π(p₁,p₂) = (p₁ − m₁)·q₁ + (p₂ − m₂)·q₂ − F

Substituindo as demandas, vira uma **função quadrática** (preços ao quadrado):

> π = −b₁·p₁² − b₂·p₂² + **2g·p₁·p₂** + (…)·p₁ + (…)·p₂ − (…)

- O termo **2g·p₁·p₂** é o **termo cruzado**: é ele que **liga** as duas variáveis.
- É a prova de que o problema é **genuinamente de duas variáveis** (não dois
  problemas separados).

> **Fala:** "Se esse termo cruzado não existisse, bastaria resolver dois problemas
> simples. Ele é o coração do projeto."

---

## Slide 5 — Derivadas parciais e gradiente

**Derivada parcial** = taxa de variação do lucro mexendo em **um só** preço, com o
outro **fixo**. Responde: "aumentar só p₁ faz o lucro subir ou descer?"

> ∂π/∂p₁ = −2b₁·p₁ + 2g·p₂ + (a₁ + b₁·m₁ − g·m₂)
> ∂π/∂p₂ = −2b₂·p₂ + 2g·p₁ + (a₂ + b₂·m₂ − g·m₁)

**Gradiente (∇π)** = as duas derivadas juntas; aponta a direção de **maior
crescimento** do lucro.

- Pense no lucro como um **morro**. No **topo**, o terreno é plano: o gradiente é
  **zero**. Essa é a **condição de ótimo**: **∇π = 0**.

> **Fala:** "No melhor par de preços, nenhuma mudancinha aumenta o lucro — o
> gradiente zera."

---

## Slide 6 — Encontrando o ponto ótimo

Impor **∇π = 0** dá **duas equações com duas incógnitas** (p₁ e p₂). Como o lucro é
quadrático, o sistema é **linear** e tem **solução única em fórmula fechada**
(via regra de Cramer):

> p₁\* = (b₂·K₁ + g·K₂) / [2(b₁b₂ − g²)]
> p₂\* = (b₁·K₂ + g·K₁) / [2(b₁b₂ − g²)]
>
> com K₁ = a₁ + b₁·m₁ − g·m₂  e  K₂ = a₂ + b₂·m₂ − g·m₁

- "Fórmula fechada" = uma expressão exata, sem tentativa e erro.
- Esse é o **par de preços** que o sistema recomenda.

> **Fala:** "Não chutamos: resolvemos o sistema e obtemos os preços exatos."

---

## Slide 7 — Classificando o ponto: teste da Hessiana

Zerar o gradiente não basta — o ponto pode ser **máximo**, **mínimo** ou **sela**
(*sela* = sobe numa direção e desce noutra). Para decidir, usamos a **Hessiana**
(matriz das **segundas** derivadas — a "curvatura" do lucro):

> H = [ −2b₁   2g ;  2g   −2b₂ ]
> D = (−2b₁)(−2b₂) − (2g)² = 4·(b₁b₂ − g²)

- **D > 0** e curvatura para baixo → **MÁXIMO** ✅
- D < 0 → sela  ·  D = 0 → teste não decide
- Como b₁ > 0, a condição de máximo vira **b₁·b₂ > g²**: o **efeito próprio** supera
  o **cruzado**. Se a substituição é forte demais, não há ótimo — o cardápio
  precisa mudar.

> **Fala:** "A Hessiana garante que achamos um pico de lucro, não um vale ou uma
> sela."

---

## Slide 8 — Exemplo resolvido + sensibilidade

**Cenário cafeteria:** a₁=120, b₁=12, m₁=3 (café especial); a₂=90, b₂=10, m₂=2,5
(cappuccino); g=4; F=50.

| Resultado | Valor |
|---|---|
| Preço ótimo café especial (p₁\*) | **R$ 9,00** |
| Preço ótimo cappuccino (p₂\*) | **R$ 8,75** |
| Lucro máximo (π\*) | **R$ 472,62/dia** |
| Hessiana / teste | D = 416 > 0 e curvatura p/ baixo ⟹ **máximo** |

**Sensibilidade:** ∂p₁\*/∂m₁ = **1/2** → cada R$ 1,00 de aumento no custo eleva o
preço ótimo em **R$ 0,50** (repassa metade, absorve metade).

> **Fala:** "Além do preço, entregamos uma regra prática: repasse 50% de qualquer
> aumento de custo."

---

## Slide 9 — Arquitetura da solução (implementação)

Fluxo exigido pelo projeto: **persona insere dados → back-end calcula → front-end
exibe**. Implementado em **3 camadas**:

- **Front-end (HTML/CSS/JS):** formulário com 6 cenários reais e rótulos em
  linguagem leiga. Envia os números à API (`fetch`) e mostra o resultado.
- **Back-end / API (Python + FastAPI):** rota **POST /api/otimizar** recebe os
  dados (validados pelo **Pydantic**), chama o motor e devolve **JSON**.
- **Motor de cálculo (SymPy):** faz toda a matemática de forma **simbólica**.

Saídas exibidas: preços ótimos, lucro, **mapa de lucro** (curvas de nível com o
ótimo destacado, via **Plotly**) e as **fórmulas** (renderizadas com **MathJax**).

> **Fala:** "A matemática fica centralizada e testável no servidor; o navegador só
> apresenta."

---

## Slide 10 — O motor de cálculo em código (SymPy) + robustez

**SymPy** = biblioteca de **matemática simbólica** (trabalha com fórmulas, como no
papel). No `optimizer.py`, ela:

1. **Monta** o lucro π como fórmula;
2. **Deriva** (`diff`) → gradiente;
3. **Resolve** (`solve`) ∇π = 0 → preços ótimos em fórmula fechada;
4. **Monta a Hessiana** (`hessian`) e **classifica** o ponto;
5. **Calcula a sensibilidade** e **gera o gráfico** e a **justificativa em texto**.

**Robustez (o que dá nota de "Excelente"):**
- valida entradas (recusa b ≤ 0);
- **avisa** quando o ponto é **sela** (b₁b₂ ≤ g²) ou quando a demanda fica negativa;
- devolve uma explicação legível de **como** o resultado foi obtido.

> **Fala:** "Não é só calcular: o sistema confere se o resultado faz sentido e
> explica a conta ao usuário."

---

# Slides complementares (criar no Gamma)

> **Ordem final sugerida:** Capa → Slides 1–10 → Conclusão → Demo ao vivo →
> Declaração de IA. Estes quatro ficam separados porque serão montados/ajustados
> diretamente no Gamma.

## Capa

**Título:** Café & Cálculo
**Subtítulo:** Otimização de preços de dois produtos relacionados usando cálculo de
várias variáveis

- Disciplina: Resolução de Problemas Multivariáveis — Prof. Pedro Girotto
- Centro Universitário do Pará (CESUPA) — Ciência da Computação
- **Equipe:**
  - Pedro Paulo de Magalhães Bezerra Filho — 24070313
  - Yuri Monteiro Alencar Aguiar — 24070309
  - João Vitor Rath de Souza Franco — 24070338

**Visual:** tons de café (marrom/creme), xícara ☕ + símbolo matemático (∇ ou ∂).
Frase: *"Transformando o 'achismo' na precificação em um número exato, em segundos."*

## Conclusão — do cálculo à decisão de negócio

- Traduzimos um **problema real de precificação** em uma **função de lucro de duas
  variáveis** e achamos o melhor par de preços **analiticamente** (gradiente ∇π = 0
  e teste da Hessiana).
- Entregamos numa **aplicação full stack**: a conta roda no back-end (Python +
  SymPy) e a recomendação aparece de forma simples para um usuário **leigo**.
- **Lição central:** por considerar a **interação** entre os produtos (o termo
  cruzado), a recomendação supera precificar "um item de cada vez".
- **Resultado concreto:** decisão antes "no olho" → **número exato em segundos**,
  com **+18% de lucro** no cenário-exemplo e a regra de **repassar 50%** de aumentos
  de custo.
- **Trabalhos futuros:** estimar os parâmetros pelo histórico de vendas; estender
  para 3+ produtos; incluir restrições de capacidade (multiplicadores de Lagrange).

> **Fala:** "Mostramos que derivadas parciais e Hessiana resolvem uma decisão real
> de negócio — e que dá para colocar isso na mão de quem não é matemático."

## Demo ao vivo — o sistema em ação

1. Abrir `http://127.0.0.1:8000`.
2. Cenário **Cafeteria** → **"Calcular preços ótimos"**.
3. Mostrar os 3 cards: café **R$ 9,00**, cappuccino **R$ 8,75**, lucro **R$ 472,62/dia**.
4. Apontar o **mapa de lucro** e a ⭐ no topo do morro (o ótimo).
5. Expandir **"Como a solução foi obtida"** → gradiente e Hessiana renderizados.
6. **Trocar de cenário** (Pizzaria/Hamburgueria) e recalcular → serve a vários
   negócios.
7. **Mexer num custo** e recalcular → o preço ótimo sobe (sensibilidade na prática).

> **Plano B:** ter print/vídeo gravado, caso a internet (MathJax/Plotly) falhe.

## Declaração de uso de Inteligência Artificial

- Utilizamos o assistente de IA **Claude (Anthropic)** como **apoio** em: busca e
  triagem do artigo; estruturação da modelagem e geração do código (FastAPI/SymPy e
  front-end); redação dos documentos.
- **Toda a matemática foi conferida manualmente pela equipe** — o exemplo numérico
  (R$ 9,00 / R$ 8,75 / R$ 472,62) foi recalculado à mão e confere.
- A IA foi **ferramenta de apoio**; as decisões, a compreensão e a verificação são
  de **autoria da equipe**.

> **Fala:** "Usamos IA de forma transparente e consciente, conferindo toda a
> matemática manualmente."
