# Guia de Apresentação — Café & Cálculo

> Material de estudo para a equipe **entender e explicar** o projeto. Cobre, em
> linguagem acessível: (1) o modelo matemático, (2) as variáveis de entrada,
> (3) como o cálculo é feito e (4) como implementamos a solução no código. Sempre
> que aparece um termo técnico, ele é explicado logo em seguida.

---

## Em uma frase

O sistema descobre **os dois preços que dão o maior lucro possível** para um negócio
que vende dois produtos parecidos (que "brigam" pelo mesmo cliente), usando
**cálculo de duas variáveis**.

---

## Parte 1 — O modelo matemático (a ideia por trás)

**A situação.** Imagine uma cafeteria que vende dois itens parecidos: um *café
especial* e um *cappuccino*. Eles são **substitutos** — ou seja, o cliente
geralmente compra **um OU o outro**, não os dois. Se o café fica mais caro, parte
das pessoas migra para o cappuccino, e vice-versa.

**Por que isso é um problema de DUAS variáveis.** Como os produtos competem, o preço
de um afeta as vendas do outro. Então não dá para escolher o melhor preço de cada
um separadamente: as duas decisões estão **amarradas**. Precisamos de uma fórmula
que dependa dos **dois preços ao mesmo tempo** — uma *função de duas variáveis*.

**O que queremos maximizar (a função objetivo).** *Função objetivo* é simplesmente
o número que queremos deixar o maior (ou menor) possível. Aqui é o **lucro**. E
lucro, de forma simples, é:

> lucro = (preço − custo) × quantidade vendida, somado para os dois produtos, menos
> os custos fixos.

**A hipótese sobre a demanda.** *Demanda* é a quantidade que o cliente compra. O
modelo assume que a demanda de cada produto:
- **cai** quando o **próprio** preço sobe (quanto mais caro, menos gente compra); e
- **sobe** quando o preço do **outro** produto sobe (substituição: se o concorrente
  encareceu, sobra cliente para mim).

Essa é a essência do artigo de referência (Forbes, 1988): o preço ótimo de cada
item depende do seu custo e de como os dois produtos se influenciam.

---

## Parte 2 — As variáveis de entrada

Existem **dois tipos** de número no modelo.

### a) Variáveis de decisão (o que o dono controla)

| Símbolo | O que é |
|---|---|
| **p₁** | preço do Produto 1 (ex.: café especial) |
| **p₂** | preço do Produto 2 (ex.: cappuccino) |

São as **respostas** que o sistema calcula: o par de preços ideal.

### b) Parâmetros (descrevem o negócio; o usuário informa)

| Símbolo | Nome técnico | Em linguagem simples |
|---|---|---|
| **a₁, a₂** | demanda-base (intercepto) | Quantas unidades venderia por dia se o preço fosse quase zero. É o "teto" de procura. |
| **b₁, b₂** | sensibilidade ao preço próprio | A cada R$ 1,00 de aumento no **próprio** preço, quantas unidades a **menos** vende por dia. |
| **g** | efeito cruzado / de substituição | A cada R$ 1,00 de aumento no preço de **um** produto, quantas unidades a **mais** do **outro** vende. |
| **m₁, m₂** | custo unitário (marginal) | Quanto custa produzir **uma** unidade (ingredientes/insumos). |
| **F** | custo fixo | Custos que **não** dependem da quantidade (parte do aluguel, energia). É opcional. |

**Exemplo (cafeteria do relatório):** a₁=120, b₁=12, m₁=3 (café especial);
a₂=90, b₂=10, m₂=2,5 (cappuccino); g=4; F=50. Com esses números, o sistema
encontra **p₁\* = R$ 9,00** e **p₂\* = R$ 8,75**, dando um lucro de **R$ 472,62/dia**.

> No site, esses parâmetros aparecem com nomes amigáveis (ex.: "Sensibilidade ao
> preço") e há 6 cenários reais pré-preenchidos (cafeteria, hamburgueria, pizzaria,
> açaiteria, lanchonete, padaria), todos calibrados para dar preços de mercado.

---

## Parte 3 — Como o cálculo é feito (passo a passo)

### Passo 1 — Escrever a demanda

q₁ = a₁ − b₁·p₁ + g·p₂  e  q₂ = a₂ − b₂·p₂ + g·p₁

(o sinal **−** no próprio preço e **+** no preço do outro traduzem a substituição).

### Passo 2 — Escrever o lucro

π(p₁,p₂) = (p₁ − m₁)·q₁ + (p₂ − m₂)·q₂ − F

Substituindo as demandas, o lucro vira uma **função quadrática** (tem preços ao
quadrado) com um **termo cruzado** 2g·p₁·p₂. Esse termo cruzado é o que **liga** as
duas variáveis — a "prova matemática" de que o problema é de duas variáveis de
verdade.

### Passo 3 — Derivadas parciais

*Derivada parcial* é a **taxa de variação** do lucro quando mexemos em **apenas um**
preço, mantendo o outro **fixo**. Ela responde: "se eu aumentar só p₁ um tiquinho, o
lucro sobe ou desce, e com que força?". Calculamos duas:

∂π/∂p₁ = −2b₁·p₁ + 2g·p₂ + (a₁ + b₁·m₁ − g·m₂)
∂π/∂p₂ = −2b₂·p₂ + 2g·p₁ + (a₂ + b₂·m₂ − g·m₁)

### Passo 4 — Gradiente e a condição de ótimo

O *gradiente* (símbolo **∇π**) é só o **par** dessas duas derivadas juntas. Ele
aponta a direção em que o lucro **mais cresce**. Pense no lucro como um **morro**:
no **topo** do morro o terreno é plano — não há direção que suba. Matematicamente,
isso significa **gradiente igual a zero**:

> **∇π = 0**  ⟺  ∂π/∂p₁ = 0  **e**  ∂π/∂p₂ = 0

Ou seja: no melhor par de preços, nenhuma mudancinha em p₁ ou p₂ aumenta o lucro.

### Passo 5 — Resolver o sistema (achar os preços)

∇π = 0 vira **duas equações com duas incógnitas** (p₁ e p₂). Como o lucro é
quadrático, essas equações são **lineares** e têm **uma única solução**, com
fórmula fechada (resolvida por regra de Cramer):

p₁\* = (b₂·K₁ + g·K₂) / [2(b₁b₂ − g²)]   ;   p₂\* = (b₁·K₂ + g·K₁) / [2(b₁b₂ − g²)]

onde K₁ = a₁ + b₁·m₁ − g·m₂ e K₂ = a₂ + b₂·m₂ − g·m₁.

### Passo 6 — Confirmar que é MÁXIMO (e não mínimo ou sela)

Achar onde o gradiente zera não basta: aquele ponto pode ser um **máximo**, um
**mínimo** ou um **ponto de sela** (um ponto que **sobe** numa direção e **desce**
em outra, como uma sela de cavalo). Para distinguir, usamos a **Hessiana**.

A *Hessiana* é a matriz das **segundas derivadas** (a "aceleração" do lucro — se a
curva está virada para baixo ou para cima):

H = [ −2b₁   2g  ;  2g   −2b₂ ]

O *teste da segunda derivada* calcula um número:

D = (−2b₁)·(−2b₂) − (2g)² = 4·(b₁b₂ − g²)

- Se **D > 0** e a curvatura é para baixo (−2b₁ < 0) → **máximo** ✅
- Se D > 0 e curvatura para cima → mínimo
- Se **D < 0** → ponto de sela
- Se D = 0 → o teste não decide

Como b₁ é sempre positivo, a condição de máximo vira simplesmente **b₁·b₂ > g²**: o
efeito do **preço próprio** precisa ser mais forte que o **efeito cruzado**. Em
palavras: se os produtos se canibalizam demais (substituição forte), não existe um
preço ótimo — sinal de que o cardápio precisa ser repensado.

### Passo 7 — Análise de sensibilidade

*Sensibilidade* (ou estática comparativa) responde: "se um parâmetro mudar, como o
preço ótimo muda?". Por exemplo, derivando a fórmula do ótimo em relação ao custo,
descobrimos que **∂p₁\*/∂m₁ = 1/2**: a cada R$ 1,00 de aumento no custo, o preço
ótimo sobe **R$ 0,50** (repasse de 50% — metade é absorvida, metade repassada).

---

## Parte 4 — Como implementamos a solução no código

### Visão geral (arquitetura em 3 camadas)

> **Navegador (front-end)** → **Servidor/API (back-end)** → **Motor de cálculo (SymPy)**

O usuário digita os números no navegador; eles viajam para o servidor; o servidor
faz a conta e devolve a resposta; o navegador mostra de forma bonita.

### Back-end (Python)

**`optimizer.py` — o cérebro matemático.** Usa a biblioteca **SymPy**, que é uma
ferramenta de **matemática simbólica**: ela trabalha com **letras e fórmulas** (não
só números), igual a gente faz no papel. O que ela faz, na ordem:
1. **Monta o lucro** π como uma fórmula em p₁, p₂.
2. **Deriva** (`diff`) para obter as derivadas parciais — sozinha, sem a gente
   calcular à mão.
3. **Resolve** (`solve`) o sistema ∇π = 0 e obtém p₁\* e p₂\* em fórmula fechada.
4. **Monta a Hessiana** (`hessian`) e aplica o teste de D para **classificar** o
   ponto (máximo, mínimo ou sela).
5. **Calcula a sensibilidade** derivando a solução em relação aos parâmetros.
6. **Gera os dados do gráfico** (uma malha de valores de lucro em volta do ótimo).
7. **Escreve uma justificativa em texto**, explicando o resultado em português.
8. Faz **validações e avisos** (ex.: recusa b ≤ 0; avisa se o ponto é sela ou se a
   demanda fica negativa) — é a parte que deixa o sistema **robusto**.

**`app.py` — a porta de entrada (API).** Usa o **FastAPI**, um framework para criar
**APIs web**. *API* é a "ponte" que recebe os dados do front-end e devolve o
resultado. O **Pydantic** valida as entradas (garante que vieram números válidos).
A rota principal é **POST `/api/otimizar`**: recebe os parâmetros, chama o
`optimizer.py` e devolve tudo em formato **JSON** (um formato de texto que o
navegador entende). O `app.py` também **serve a página** do front-end.

### Front-end (HTML, CSS e JavaScript)

- **`index.html`** desenha a tela: o seletor de cenário, os campos de entrada e a
  área de resultado.
- **`style.css`** cuida da aparência (cores de cafeteria, layout responsivo).
- **`app.js`** é a lógica: quando o usuário clica em "Calcular", ele empacota os
  números e os **envia para a API** (`fetch`). Quando a resposta chega, ele mostra:
  - os **cards** com os preços ótimos e o lucro;
  - o **mapa de lucro**, desenhado com a biblioteca **Plotly** (gráficos
    interativos) — são as **curvas de nível** (linhas que ligam combinações de
    preços com o mesmo lucro), com uma ⭐ no topo do "morro";
  - as **fórmulas**, renderizadas com **MathJax** (que transforma a linguagem de
    fórmulas em matemática bonita na tela);
  - a **justificativa** em texto vinda do back-end.

### O fluxo, do começo ao fim

1. O usuário escolhe um cenário (ou edita os números) e clica em **Calcular**.
2. O `app.js` envia os parâmetros em JSON para **POST `/api/otimizar`**.
3. O FastAPI valida e chama `solve_pricing()` no `optimizer.py`.
4. O SymPy deriva, resolve ∇π = 0, monta a Hessiana, classifica e calcula tudo.
5. A API devolve: preços ótimos, lucro, classificação, fórmulas, gráfico e texto.
6. O `app.js` desenha os cards, o mapa de lucro e as fórmulas para o usuário.

> **Por que separar back-end e front-end?** Porque a **matemática fica centralizada
> e confiável** no servidor (um lugar só, fácil de testar), enquanto o navegador
> cuida apenas de mostrar — exatamente o que o enunciado pede: "persona insere dados
> → back-end calcula → front-end exibe".

---

## Roteiro rápido (como explicar em ~1 minuto)

"Nosso sistema ajuda um negócio a precificar dois produtos que competem entre si.
Modelamos o **lucro** como uma **função de dois preços**; como os produtos são
substitutos, ela tem um **termo que liga as duas variáveis**. Para achar o melhor
par de preços, calculamos o **gradiente** e resolvemos **∇π = 0** — o ponto onde o
lucro para de crescer. Depois usamos a **Hessiana** para confirmar que é um
**máximo**. No código, o **Python com SymPy** faz toda essa conta de forma
**simbólica** no back-end (FastAPI), e o front-end mostra os preços, um **mapa de
lucro** e a explicação. Resultado: uma decisão que antes era no 'achismo' vira um
número exato, em segundos."
