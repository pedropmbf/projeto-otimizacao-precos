# 1. Prospecção do Problema (PBL)

## 1.1 Referência completa do artigo

> **FORBES, Kevin F.** *Pricing of related products by a multiproduct monopolist.*
> **Review of Industrial Organization**, v. 3, n. 3, p. 55–73, 1988.
> DOI: [10.1007/BF02229566](https://doi.org/10.1007/BF02229566)

Periódico revisado por pares (Springer), da área de Organização Industrial /
Microeconomia.

## 1.2 Recorte do artigo

Trecho do resumo (abstract) do artigo, que justifica o problema e a necessidade
de otimização:

> *"This paper examines the pricing behavior of a multiproduct monopolist (MPM).
> **For a firm selling two products, the profit maximizing price of a particular
> item is found to depend upon its marginal cost, the own and cross-price
> elasticities and the budget shares of both products.** Conditions are identified
> under which the price charged by a MPM will be greater than, less than, and
> equal to the price charged by an otherwise identical single product monopolist
> as well as the circumstances under which it is profitable for a MPM to utilize
> one product as a loss leader."*
> — Forbes (1988), abstract.

**Tradução livre do trecho em negrito:** *"Para uma empresa que vende dois
produtos, o preço que maximiza o lucro de um item depende do seu custo marginal,
das elasticidades de preço própria e cruzada e das participações no orçamento de
ambos os produtos."*

## 1.3 Por que este problema é adequado à disciplina

O artigo trata exatamente de uma **otimização de função de duas variáveis**, que
é o conteúdo central da disciplina (derivadas parciais, gradiente, máximos e
mínimos). A correspondência é direta:

| Elemento da disciplina | Como aparece no problema |
|---|---|
| **Função de várias variáveis** | Lucro `π(p₁, p₂)` em função dos preços de dois produtos |
| **≥ 2 variáveis de decisão** | `p₁` = preço do Produto 1; `p₂` = preço do Produto 2 |
| **Interdependência (variáveis "bem articuladas")** | Os produtos são **substitutos**: a demanda de um depende do preço do outro (elasticidade **cruzada**), gerando um termo cruzado `p₁·p₂` na função de lucro |
| **Derivadas parciais e gradiente** | Condições de 1ª ordem `∂π/∂p₁ = 0` e `∂π/∂p₂ = 0` (o gradiente `∇π = 0`) |
| **Classificação de ponto crítico** | Teste da Hessiana: o ponto é máximo quando `b₁·b₂ > g²` (efeito de preço próprio supera o cruzado) |
| **Problema real** | Decisão de preços que qualquer comércio com itens concorrentes precisa tomar |

**Justificativa da escolha.** O problema é simultaneamente (i) **real e
reconhecível** — qualquer cafeteria, padaria ou loja decide preços de itens que
competem entre si; (ii) **genuinamente multivariável** — as duas variáveis
interagem (não se trata de dois problemas separados de uma variável); e
(iii) **analiticamente tratável** — a função de lucro é quadrática, então
`∇π = 0` é um sistema linear com solução em forma fechada e Hessiana constante,
permitindo classificação exata pelo teste da segunda derivada. Isso torna o
problema ideal para demonstrar todo o ferramental da disciplina e, ao mesmo
tempo, construir um sistema que entrega uma recomendação prática.

> Observação de integridade acadêmica: o texto entre aspas acima é o resumo
> oficial do artigo (obtido dos metadados do editor). Ao acessar o PDF completo
> pela biblioteca do CESUPA/Springer, vale conferir a introdução e a seção do
> modelo para, se desejarem, citar também uma passagem do corpo do texto.
