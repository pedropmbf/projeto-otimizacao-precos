# 2. Modelagem Matemática

Modela-se a decisão de preços de **dois produtos substitutos** vendidos por um
mesmo estabelecimento, maximizando o **lucro total**. A formulação segue o modelo
de monopolista multiproduto de Forbes (1988): o preço ótimo de cada item depende
do seu custo marginal e das elasticidades **própria** e **cruzada**.

---

## 2.1 Variáveis de decisão

| Símbolo | Significado | Unidade |
|---|---|---|
| $p_1$ | preço de venda do **Produto 1** (café especial coado) | R$/unidade |
| $p_2$ | preço de venda do **Produto 2** (cappuccino) | R$/unidade |

São as duas variáveis que a persona controla. Todo o resto são **parâmetros**
informados por ela (estimados a partir das vendas).

| Parâmetro | Significado |
|---|---|
| $a_1, a_2$ | demanda-base (intercepto) de cada produto |
| $b_1, b_2$ | sensibilidade da demanda ao **preço próprio** (efeito próprio) |
| $g$ | sensibilidade ao **preço do outro** produto (efeito cruzado) |
| $m_1, m_2$ | custo unitário (marginal) de cada produto |
| $F$ | custo fixo (não depende da quantidade) |

## 2.2 Hipóteses do modelo

1. **Demanda linear** nos preços (aproximação de 1ª ordem, válida na faixa usual
   de preços do negócio).
2. **Produtos substitutos:** encarecer um produto **aumenta** a demanda do outro,
   logo o coeficiente cruzado é simétrico e positivo, $g > 0$. (Para
   complementares, bastaria $g < 0$; o modelo continua válido.)
3. **Custo marginal constante** $m_i$ por unidade (sem economia de escala na
   faixa considerada).
4. O estabelecimento **define os preços** (poder de mercado local — premissa de
   monopolista multiproduto do artigo).

## 2.3 Funções de demanda

$$q_1(p_1,p_2) = a_1 - b_1\,p_1 + g\,p_2$$
$$q_2(p_1,p_2) = a_2 - b_2\,p_2 + g\,p_1$$

Interpretação dos sinais: $-b_i\,p_i$ (demanda cai com o **próprio** preço) e
$+g\,p_j$ (demanda **sobe** quando o **concorrente interno** encarece — efeito de
substituição).

## 2.4 Função objetivo (lucro)

$$\pi(p_1,p_2) = \underbrace{(p_1 - m_1)\,q_1}_{\text{margem prod. 1}} + \underbrace{(p_2 - m_2)\,q_2}_{\text{margem prod. 2}} - F$$

Substituindo as demandas e expandindo:

$$\boxed{\;\pi(p_1,p_2) = -b_1 p_1^{2} - b_2 p_2^{2} + 2g\,p_1 p_2 + (a_1 + b_1 m_1 - g m_2)\,p_1 + (a_2 + b_2 m_2 - g m_1)\,p_2 - (a_1 m_1 + a_2 m_2 + F)\;}$$

É uma **função quadrática** de duas variáveis. O termo cruzado $2g\,p_1 p_2$ é o
que torna o problema **genuinamente multivariável**: as duas decisões interagem e
não podem ser otimizadas separadamente.

## 2.5 Domínio e restrições

O domínio econômico é a região do plano $(p_1, p_2)$ em que faz sentido operar:

$$p_1 \ge m_1, \quad p_2 \ge m_2 \quad\text{(preço cobre o custo)}$$
$$q_1 \ge 0, \quad q_2 \ge 0 \quad\text{(demandas não negativas)}$$

Sobre os parâmetros: $a_i > 0$, $b_i > 0$ e, para que exista um máximo interior,
$b_1 b_2 > g^2$ (ver §2.8). Quando o ótimo irrestrito cai fora dessa região, a
solução está na **fronteira** (ex.: parar de vender um item) — o sistema detecta e
avisa.

**Caso restrito (ótimo na fronteira).** Se os parâmetros levam o ponto crítico
analítico a uma região com $q_i < 0$ (economicamente inviável), o problema deixa de
ter solução no interior e torna-se uma **otimização restrita** sobre uma região
**fechada e limitada** (compacta). Como $\pi$ é contínua nessa região, o **teorema de
Weierstrass** garante que o máximo existe; e, por $\pi$ ser **côncava** sobre um
domínio **convexo**, esse máximo localiza-se necessariamente na **fronteira** — onde
$q_i = 0$ ou $p_i = m_i$ —, o que, em termos econômicos, significa **descontinuar** o
item canibalizado. Nesta versão, o sistema **detecta** essa situação (quando
$q_i < 0$ ou a margem fica negativa) e **alerta** a persona recomendando rever o
portfólio; a resolução automática do ótimo de fronteira fica como trabalho futuro.

## 2.6 Derivadas parciais e gradiente

$$\frac{\partial \pi}{\partial p_1} = -2b_1\,p_1 + 2g\,p_2 + (a_1 + b_1 m_1 - g m_2)$$
$$\frac{\partial \pi}{\partial p_2} = -2b_2\,p_2 + 2g\,p_1 + (a_2 + b_2 m_2 - g m_1)$$

$$\nabla \pi = \left( \frac{\partial \pi}{\partial p_1},\; \frac{\partial \pi}{\partial p_2} \right)$$

**Interpretação:** cada parcial é a *receita marginal líquida* de mexer em um
preço. No ótimo ela é zero — subir mais o preço perderia, em demanda (própria e do
rival), mais do que ganharia em margem.

## 2.7 Ponto crítico: resolução de $\nabla \pi = 0$

Igualando as parciais a zero, obtém-se o sistema linear (defina
$K_1 = a_1 + b_1 m_1 - g m_2$ e $K_2 = a_2 + b_2 m_2 - g m_1$):

$$\begin{cases} 2b_1\,p_1 - 2g\,p_2 = K_1 \\ -2g\,p_1 + 2b_2\,p_2 = K_2 \end{cases}
\iff
\begin{bmatrix} 2b_1 & -2g \\ -2g & 2b_2 \end{bmatrix}
\begin{bmatrix} p_1 \\ p_2 \end{bmatrix}
=
\begin{bmatrix} K_1 \\ K_2 \end{bmatrix}$$

O determinante é $\Delta = 4b_1 b_2 - 4g^2 = 4(b_1 b_2 - g^2)$. Por **Cramer**
(solução em forma fechada):

$$\boxed{\;p_1^{*} = \frac{b_2\,K_1 + g\,K_2}{2\,(b_1 b_2 - g^2)}, \qquad p_2^{*} = \frac{b_1\,K_2 + g\,K_1}{2\,(b_1 b_2 - g^2)}\;}$$

## 2.8 Classificação do ponto crítico (teste da Hessiana)

A matriz Hessiana é **constante**:

$$H = \begin{bmatrix} \dfrac{\partial^2 \pi}{\partial p_1^2} & \dfrac{\partial^2 \pi}{\partial p_1 \partial p_2} \\[2mm] \dfrac{\partial^2 \pi}{\partial p_2 \partial p_1} & \dfrac{\partial^2 \pi}{\partial p_2^2} \end{bmatrix} = \begin{bmatrix} -2b_1 & 2g \\ 2g & -2b_2 \end{bmatrix}$$

Aplicando o **teste da segunda derivada** para funções de duas variáveis, com
$D = \pi_{p_1 p_1}\,\pi_{p_2 p_2} - (\pi_{p_1 p_2})^2$:

$$D = (-2b_1)(-2b_2) - (2g)^2 = 4(b_1 b_2 - g^2)$$

| Condição | Classificação |
|---|---|
| $D > 0$ e $\pi_{p_1p_1} = -2b_1 < 0$ | **máximo local** |
| $D > 0$ e $\pi_{p_1p_1} > 0$ | mínimo local |
| $D < 0$ | ponto de sela |
| $D = 0$ | teste inconclusivo |

Como $b_1 > 0$, tem-se sempre $\pi_{p_1p_1} < 0$. Portanto o ponto crítico é um
**máximo** se, e somente se,

$$\boxed{\,b_1 b_2 > g^2\,}$$

ou seja, **o efeito de preço próprio supera o cruzado**. Além disso, como $\pi$ é
quadrática com Hessiana constante negativa definida, esse máximo local é também o
**máximo global**.

> **Interpretação:** se os produtos forem substitutos "fracos" ($g$ pequeno), há um
> par de preços que maximiza o lucro. Se a substituição for forte demais
> ($g^2 \ge b_1 b_2$), os produtos praticamente canibalizam um ao outro e não
> existe ótimo interior — sinal de que deveriam ser repensados (ex.: diferenciar
> ou descontinuar um deles).

## 2.9 Exemplo numérico resolvido

Parâmetros (cenário da persona): $a_1=120,\,b_1=12,\,m_1=3$; $a_2=90,\,b_2=10,\,m_2=2{,}5$; $g=4$; $F=50$.

**Passo 1 — constantes:**
$K_1 = 120 + 12(3) - 4(2{,}5) = 146$ e $K_2 = 90 + 10(2{,}5) - 4(3) = 103$.
Denominador: $b_1 b_2 - g^2 = 120 - 16 = 104$.

**Passo 2 — preços ótimos:**
$$p_1^{*} = \frac{10(146) + 4(103)}{2(104)} = \frac{1872}{208} = \mathbf{9{,}00} \qquad p_2^{*} = \frac{12(103) + 4(146)}{2(104)} = \frac{1820}{208} = \mathbf{8{,}75}$$

**Passo 3 — demandas e lucro:**
$q_1 = 120 - 12(9) + 4(8{,}75) = 47$;  $q_2 = 90 - 10(8{,}75) + 4(9) = 38{,}5$.
$$\pi^{*} = (9-3)(47) + (8{,}75-2{,}5)(38{,}5) - 50 = 282 + 240{,}625 - 50 = \mathbf{472{,}625}$$

**Passo 4 — classificação:**
$H = \begin{bmatrix} -24 & 8 \\ 8 & -20 \end{bmatrix}$, $D = (-24)(-20) - 8^2 = 416 > 0$ e $\pi_{p_1p_1} = -24 < 0$ ⟹ **máximo** (confirmado).

> **Resultado:** cobrar **R\$ 9,00** no café coado e **R\$ 8,75** no cappuccino dá
> o maior lucro diário possível, **R\$ 472,62**, vendendo ~47 e ~38 unidades.

## 2.10 Análise de sensibilidade (estática comparativa)

Derivando o ótimo em relação aos parâmetros obtêm-se resultados exatos e
interpretáveis:

$$\frac{\partial p_1^{*}}{\partial m_1} = \frac{b_1 b_2 - g^2}{2(b_1 b_2 - g^2)} = \frac{1}{2}, \qquad \frac{\partial p_1^{*}}{\partial a_1} = \frac{b_2}{2(b_1 b_2 - g^2)}, \qquad \frac{\partial p_1^{*}}{\partial m_2} = 0$$

- **Repasse de custo de 50%:** cada R\$ 1,00 de aumento no custo do Produto 1
  eleva seu preço ótimo em exatamente R\$ 0,50 — o estabelecimento absorve metade
  e repassa metade.
- **Aumento de demanda:** no exemplo, $\partial p_1^{*}/\partial a_1 = 10/208 \approx 0{,}048$ — mais procura permite preço um pouco maior.
- O preço ótimo de um produto **não depende** do custo do outro
  ($\partial p_1^{*}/\partial m_2 = 0$), uma consequência elegante da simetria do
  efeito cruzado.

---

### Resumo do que a disciplina cobre aqui

- **Função de várias variáveis:** $\pi(p_1, p_2)$ — §2.4
- **Derivadas parciais e gradiente:** §2.6
- **Resolução de $\nabla \pi = 0$ (ponto crítico):** §2.7
- **Hessiana e classificação (máx/mín/sela):** §2.8
- **Interpretação no contexto + sensibilidade:** §2.9–2.10
