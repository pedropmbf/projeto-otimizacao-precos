# 3. Persona e Contexto

## 3.1 Quem é

**Marina Albuquerque**, 34 anos — proprietária da cafeteria **"Grão & Co."**,
no bairro do Umarizal, em Belém (PA).

Formada em Administração, Marina trabalhou seis anos em um banco antes de realizar
o sonho de abrir o próprio negócio. Há dois anos toca a cafeteria, que vende cerca
de 80 a 100 cafés por dia. Seus dois carros-chefe são o **café especial coado** e
o **cappuccino** — itens parecidos, que disputam o mesmo cliente: quem entra
geralmente pede um **ou** o outro. Marina entende de atendimento e de café, mas
define os preços "no olho", olhando o que a concorrência cobra.

## 3.2 Dor / problema explícito

Marina precisa **decidir o preço de venda dos dois cafés**, mas não tem como saber
qual combinação de preços dá o maior lucro. O problema é que os produtos
**competem entre si**:

- Quando ela faz **promoção no cappuccino**, percebe que vende menos do café coado
  (canibalização), mas **não consegue medir o efeito líquido no lucro total**.
- Se sobe o preço de um, parte dos clientes migra para o outro — e ela não sabe
  calcular o ponto de equilíbrio.
- A decisão atual é **por intuição e imitação da concorrência**, o que é
  ineficiente: ora ela deixa de lucrar cobrando barato demais, ora espanta cliente
  cobrando caro demais, e as promoções às vezes **reduzem** o lucro sem que ela
  perceba.

> Em resumo: Marina toma uma decisão **multivariável** (dois preços que interagem)
> usando uma régua de **uma variável de cada vez**. É exatamente onde a otimização
> de duas variáveis ajuda.

## 3.3 Métricas de sucesso (quantitativas)

| Indicador | Situação atual (estimada) | Meta com o sistema |
|---|---|---|
| Lucro diário com os dois cafés | ~ R$ 400/dia (preços "no olho") | ~ R$ 472/dia no cenário-exemplo (**+18%**) |
| Ganho mensal adicional | — | ≈ **R$ 1.600/mês** (22 dias úteis) |
| Tempo para decidir/ajustar preços | horas de tentativa e erro | **< 1 minuto** por simulação |
| Promoções que reduzem o lucro total | acontece sem ela perceber | **0** — o sistema avisa quando não compensa |

> Os valores de "situação atual" são estimativas da própria persona; a meta é o
> resultado calculado pelo sistema no **cenário-exemplo** documentado na modelagem
> (a1=120, b1=12, m1=3; a2=90, b2=10, m2=2,5; g=4; F=50), que produz preços ótimos
> de **R$ 9,00** e **R$ 8,75** e lucro de **R$ 472,62/dia**.

## 3.4 Impacto esperado do sistema

- **Decisão baseada em dados, não em achismo:** Marina informa seus números do dia
  a dia (demanda, sensibilidade a preço, custo) e recebe o **par de preços ótimo**
  com o **lucro esperado**.
- **Entendimento do trade-off:** o sistema mostra, em linguagem simples, *por que*
  aquele é o melhor preço, considerando que os dois cafés competem.
- **Simulação de cenários ("e se?"):** ela testa, por exemplo, "e se o custo do
  leite subir R$ 1,00?" e vê na hora como os preços ótimos mudam (análise de
  sensibilidade).
- **Confiança para precificar:** em vez de copiar o concorrente, ela passa a ter um
  critério objetivo, ajustável sempre que os custos ou a demanda mudarem.
