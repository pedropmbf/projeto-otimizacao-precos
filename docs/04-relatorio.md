# Relatório — Projeto Otimização

> **Documento-base do relatório em PDF (5–10 páginas).** Revise, preencha os
> campos *(entre parênteses)*, ajuste os números da persona para as estimativas
> reais da equipe e exporte para PDF (sugestão: VS Code + extensão *Markdown PDF*,
> ou Pandoc — veja o fim do arquivo). As fórmulas em `$$...$$` renderizam no
> GitHub e no Pandoc.

---

**Centro Universitário do Pará (CESUPA) — Ciência da Computação**
**Disciplina:** Resolução de Problemas Multivariáveis — Prof. Pedro Girotto
**Equipe:** *(nome 1, nome 2, nome 3)*
**Título:** Café & Cálculo — Otimização de preços de produtos relacionados por
um monopolista multiproduto

---

## 1. Introdução

A precificação de produtos que competem entre si é uma decisão cotidiana de
qualquer comércio e, ao mesmo tempo, um problema de **otimização de função de
várias variáveis**. Quando dois itens são **substitutos**, o preço de um afeta a
demanda do outro: a decisão deixa de ser "qual o melhor preço deste produto?" e
passa a ser "qual o **par de preços** que maximiza o lucro total?".

Este projeto modela esse problema, resolve-o analiticamente com o ferramental da
disciplina (derivadas parciais, gradiente e teste da Hessiana) e entrega uma
**aplicação full stack** que automatiza o cálculo para um usuário leigo — a dona de
uma cafeteria. O objetivo é transformar uma decisão hoje feita "no olho" em uma
recomendação objetiva, explicável e baseada em dados.

## 2. Prospecção do Problema (artigo de referência)

**Referência.** FORBES, Kevin F. *Pricing of related products by a multiproduct
monopolist.* **Review of Industrial Organization**, v. 3, n. 3, p. 55–73, 1988.
DOI: 10.1007/BF02229566.

**Recorte (abstract).** *"For a firm selling two products, the profit maximizing
price of a particular item is found to depend upon its marginal cost, the own and
cross-price elasticities and the budget shares of both products."* — Forbes (1988).
Em tradução livre: *para uma empresa que vende dois produtos, o preço que maximiza
o lucro de um item depende de seu custo marginal e das elasticidades de preço
própria e cruzada.*

**Por que é adequado.** O artigo trata literalmente de uma função de **duas
variáveis** (os preços de dois produtos) a ser **maximizada** (o lucro), com as
variáveis **interagindo** via efeito cruzado. Isso cobre todo o conteúdo da
disciplina: a função objetivo é multivariável, o ótimo exige resolver
$\nabla \pi = 0$, e a natureza do ponto crítico é determinada pela Hessiana. Além
disso, é um problema **real** e reconhecível, com uma persona natural. Detalhes em
`docs/01-prospeccao.md`.

## 3. Persona e sua dor

**Marina Albuquerque**, 34, dona da cafeteria *Grão & Co.* (Belém-PA). Vende ~80–100
cafés/dia; seus carros-chefe são o **café especial coado** e o **cappuccino** —
itens que disputam o mesmo cliente.

**Dor.** Marina define preços por intuição e imitando a concorrência. Como os dois
cafés são substitutos, promoções em um **canibalizam** o outro, e ela não consegue
medir o **efeito líquido no lucro**. Resultado: ora cobra barato demais (perde
margem), ora caro demais (perde cliente), e algumas promoções **reduzem** o lucro
sem que ela perceba.

**Métricas de sucesso.** (i) aumentar o lucro diário dos dois cafés — no
cenário-exemplo, de ~R\$ 400 para **R\$ 472,62** (**+18%**), ≈ R\$ 1.600/mês;
(ii) reduzir o tempo de decisão de preços para **< 1 minuto**; (iii) **zero**
promoções que diminuem o lucro total.

**Impacto.** Decisão baseada em dados; entendimento do trade-off entre os dois
produtos; simulação de cenários ("e se o custo do leite subir?"). Detalhes em
`docs/03-persona.md`.

## 4. Modelagem Matemática

### 4.1 Variáveis e função objetivo

Variáveis de decisão: $p_1, p_2$ — preços dos Produtos 1 e 2. Parâmetros (informados
pela persona): demanda-base $a_i$, sensibilidade ao preço próprio $b_i$, efeito
cruzado $g$, custos $m_i$ e custo fixo $F$.

Demanda linear (substitutos, $g>0$):
$$q_1 = a_1 - b_1 p_1 + g\,p_2, \qquad q_2 = a_2 - b_2 p_2 + g\,p_1$$

Lucro (função objetivo):
$$\pi(p_1,p_2) = (p_1-m_1)q_1 + (p_2-m_2)q_2 - F$$
$$= -b_1 p_1^2 - b_2 p_2^2 + 2g\,p_1 p_2 + (a_1 + b_1 m_1 - g m_2)p_1 + (a_2 + b_2 m_2 - g m_1)p_2 - (a_1 m_1 + a_2 m_2 + F)$$

É **quadrática** em duas variáveis; o termo $2g\,p_1p_2$ acopla as decisões.
**Domínio:** $p_i \ge m_i$ e $q_i \ge 0$ (preços cobrem custo e demandas não
negativas).

### 4.2 Gradiente e ponto ótimo

$$\frac{\partial \pi}{\partial p_1} = -2b_1 p_1 + 2g\,p_2 + (a_1 + b_1 m_1 - g m_2), \qquad \frac{\partial \pi}{\partial p_2} = -2b_2 p_2 + 2g\,p_1 + (a_2 + b_2 m_2 - g m_1)$$

Resolvendo $\nabla \pi = 0$ (sistema linear; $K_1 = a_1 + b_1 m_1 - g m_2$,
$K_2 = a_2 + b_2 m_2 - g m_1$):
$$p_1^{*} = \frac{b_2 K_1 + g K_2}{2(b_1 b_2 - g^2)}, \qquad p_2^{*} = \frac{b_1 K_2 + g K_1}{2(b_1 b_2 - g^2)}$$

### 4.3 Classificação (Hessiana)

$$H = \begin{bmatrix} -2b_1 & 2g \\ 2g & -2b_2 \end{bmatrix}, \qquad D = (-2b_1)(-2b_2) - (2g)^2 = 4(b_1 b_2 - g^2)$$

Como $-2b_1 < 0$, o ponto crítico é **máximo** se, e só se, $b_1 b_2 > g^2$ (efeito
próprio supera o cruzado). Sendo $\pi$ quadrática com Hessiana negativa definida, o
máximo local é **global**. Derivação completa em `docs/02-modelagem.md`.

## 5. Implementação

### 5.1 Arquitetura

Fluxo: **persona insere dados → back-end calcula → front-end exibe a recomendação.**

- **Back-end (Python, FastAPI + SymPy).** O módulo `optimizer.py` constrói a função
  de lucro **simbolicamente**, calcula as derivadas parciais, resolve $\nabla\pi=0$
  em forma fechada, monta a Hessiana e classifica o ponto pelo teste da segunda
  derivada. Faz ainda **validações** (ex.: $b_i>0$), **checagens de viabilidade**
  (demanda/margem negativas, ponto de sela) e **análise de sensibilidade**
  (estática comparativa). Retorna o ponto ótimo $(p_1^*, p_2^*)$, o valor $\pi^*$,
  as fórmulas em LaTeX e uma justificativa textual.
- **Front-end (HTML/CSS/JS).** Formulário com rótulos em linguagem leiga (a persona
  não vê "coeficiente cruzado", e sim "efeito de substituição"), botão de exemplo,
  e uma seção **"Como a solução foi obtida"** que renderiza o gradiente e a
  Hessiana (MathJax) ao lado da explicação em texto.

### 5.2 "Como a solução foi obtida" (justificativa ao usuário)

O sistema apresenta ao usuário, em linguagem acessível: o ponto ótimo, o lucro
máximo, a classificação (com o valor de $D$ e o sinal de $f_{p_1p_1}$) e a
sensibilidade. Assim, mesmo sem conhecimento matemático, a persona entende *por
que* aqueles são os melhores preços.

## 6. Resultados e interpretação

Cenário da persona: $a_1=120, b_1=12, m_1=3$; $a_2=90, b_2=10, m_2=2{,}5$; $g=4$;
$F=50$.

| Saída | Valor |
|---|---|
| Preço ótimo — Café Especial ($p_1^*$) | **R\$ 9,00** |
| Preço ótimo — Cappuccino ($p_2^*$) | **R\$ 8,75** |
| Demanda ótima | 47 e 38,5 un./dia |
| Lucro máximo ($\pi^*$) | **R\$ 472,62/dia** |
| Hessiana | $\begin{bmatrix} -24 & 8 \\ 8 & -20 \end{bmatrix}$, $D=416>0$ ⟹ máximo |
| Sensibilidade | repasse de custo de **50%** ($\partial p_1^*/\partial m_1 = 1/2$) |

**Interpretação.** O modelo confirma analiticamente um par de preços que maximiza o
lucro. A leitura de sensibilidade dá à persona uma regra prática: ao subir o custo
de um café em R\$ 1,00, repassar **metade** ao preço. O sistema também sinaliza
quando os parâmetros não geram um máximo válido (canibalização forte, $g^2 \ge
b_1b_2$), orientando a repensar o portfólio.

## 7. Conclusão

O projeto traduziu um problema real de precificação em uma função de lucro de duas
variáveis, encontrou o ótimo analiticamente (gradiente + Hessiana) e o
materializou em um sistema full stack que comunica a solução a um usuário leigo. O
caso evidencia o valor do cálculo multivariável em decisões de negócio: por
considerar a **interação** entre os produtos, a recomendação supera a precificação
"um produto de cada vez". *(Trabalhos futuros: estimar os parâmetros a partir do
histórico de vendas; estender para 3+ produtos; incluir restrições de capacidade
via multiplicadores de Lagrange.)*

## 8. Declaração de uso de Inteligência Artificial

*(Ajuste conforme o uso real da equipe.)* Utilizamos o assistente de IA **Claude
(Anthropic)** como apoio em: (i) busca e triagem do artigo de referência;
(ii) estruturação da modelagem e geração do código (FastAPI/SymPy e front-end);
(iii) redação dos documentos. **Toda a matemática foi conferida manualmente pela
equipe** — o exemplo numérico da §6 foi recalculado à mão e confere com a saída do
sistema. A IA foi ferramenta de apoio; a compreensão do conteúdo, as decisões de
modelagem e a verificação são de autoria da equipe.

## Referências

FORBES, Kevin F. Pricing of related products by a multiproduct monopolist.
**Review of Industrial Organization**, v. 3, n. 3, p. 55–73, 1988. DOI:
10.1007/BF02229566.

STEWART, James. **Cálculo, volume 2.** São Paulo: Cengage Learning. *(capítulo de
derivadas parciais, gradiente e máximos/mínimos — ajustar edição usada na
disciplina.)*

---

### Como exportar para PDF

- **VS Code:** instale a extensão *Markdown PDF* → botão direito no arquivo →
  *Markdown PDF: Export (pdf)*.
- **Pandoc** (renderiza as fórmulas): `pandoc 04-relatorio.md -o relatorio.pdf
  --pdf-engine=xelatex`.
