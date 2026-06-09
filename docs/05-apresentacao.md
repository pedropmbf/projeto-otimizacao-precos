# Roteiro da Apresentação (10–15 min)

Sugestão de **12 slides** + demo ao vivo. Tempo-alvo entre parênteses. Divida a
fala entre os integrantes (ex.: 1 abre, 1 faz a matemática, 1 conduz a demo).

---

### Slide 1 — Capa (0:30)
Título *Café & Cálculo*, nomes da equipe, disciplina e professor.
**Fala:** "Vamos mostrar como cálculo de duas variáveis ajuda uma cafeteria a
lucrar mais."

### Slide 2 — O problema real + artigo (1:00)
- Precificar dois produtos que **competem entre si**.
- Artigo: Forbes (1988), *Pricing of related products by a multiproduct
  monopolist* — o preço ótimo depende do custo e das elasticidades **própria e
  cruzada**.
- **Recorte** na tela (citação do abstract).

### Slide 3 — A persona e sua dor (1:00)
- Marina, dona da *Grão & Co.*; vende café coado e cappuccino.
- Decide preço "no olho"; promoções canibalizam e ela não mede o efeito no lucro.
- **Gancho:** "Ela decide duas coisas que interagem usando uma régua de uma
  variável."

### Slide 4 — Variáveis e função objetivo (1:30)
- $p_1, p_2$ (preços). Demanda: $q_i = a_i - b_i p_i + g\,p_j$.
- Lucro $\pi(p_1,p_2) = (p_1-m_1)q_1 + (p_2-m_2)q_2 - F$.
- Destacar o **termo cruzado** $2g\,p_1p_2$ → "é isto que torna o problema de duas
  variáveis de verdade".

### Slide 5 — Gradiente e ponto ótimo (2:00)
- Mostrar $\partial\pi/\partial p_1$ e $\partial\pi/\partial p_2$.
- $\nabla\pi=0$ vira sistema linear → solução em forma fechada $p_1^*, p_2^*$.

### Slide 6 — Classificação pela Hessiana (1:30)
- $H=\begin{bmatrix}-2b_1 & 2g\\ 2g & -2b_2\end{bmatrix}$, $D=4(b_1b_2-g^2)$.
- **Máximo ⟺ $b_1b_2 > g^2$** (efeito próprio supera o cruzado). Interpretar.

### Slide 7 — Exemplo resolvido (1:00)
- Números da persona → $p_1^*=9{,}00$, $p_2^*=8{,}75$, $\pi^*=472{,}62$.
- $H=\begin{bmatrix}-24&8\\8&-20\end{bmatrix}$, $D=416>0$ ⟹ máximo (feito à mão).

### Slide 8 — Arquitetura do sistema (1:00)
- Diagrama: **Front-end → API (FastAPI) → motor SymPy → resposta**.
- SymPy faz a conta **simbolicamente** (deriva, resolve, classifica).

### Slide 9 — 🔴 DEMO AO VIVO (3:00)
1. Abrir http://127.0.0.1:8000.
2. Deixar no cenário **Cafeteria** (padrão) → "Calcular preços ótimos".
3. Mostrar os três cards (preços + lucro) e a classificação "máximo".
4. Mostrar o **mapa de lucro**: as curvas de nível e a ⭐ no topo do morro.
5. Expandir **"Como a solução foi obtida"** → gradiente e Hessiana renderizados.
6. **Trocar o cenário** (ex.: Pizzaria ou Hamburgueria) e recalcular → mostrar que
   o mesmo sistema serve a vários negócios, com preços reais.
7. **Mexer num parâmetro** (ex.: aumentar o custo) e recalcular → o preço ótimo
   sobe (sensibilidade na prática).
8. *(Opcional)* Forçar um caso de **sela** (efeito de substituição alto) e mostrar
   o **aviso** do sistema.

> Plano B da demo: ter um **print/gravação** caso a internet (MathJax) falhe.

### Slide 10 — Resultados e impacto (1:00)
- Lucro +18% no cenário; repasse de custo de 50%; decisão em < 1 min.
- Como muda o dia a dia da Marina.

### Slide 11 — Conclusão (0:30)
- Cálculo multivariável → decisão de negócio melhor por considerar a **interação**.
- Futuro: estimar parâmetros das vendas; 3+ produtos; restrições (Lagrange).

### Slide 12 — Uso de IA + Referências (0:30)
- Declarar uso da IA (apoio) e a **verificação manual** da matemática.
- Referência do artigo e do livro de Cálculo.

---

## Checklist pré-demo
- [ ] Servidor rodando (`uvicorn app:app --reload`) **antes** de começar.
- [ ] Página aberta e testada (escolher um cenário e calcular).
- [ ] Internet ok (MathJax via CDN) **ou** print/vídeo de backup.
- [ ] Zoom do navegador aumentado para a sala enxergar.
- [ ] Combinar quem fala cada parte e quem opera a demo.
