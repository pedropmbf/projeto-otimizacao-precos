# ☕ Café & Cálculo — Otimizador de Preços

Aplicação **full stack** que calcula os **preços que maximizam o lucro** de dois
produtos relacionados (substitutos) de uma cafeteria, usando **funções de várias
variáveis, derivadas parciais, gradiente e o teste da Hessiana**.

O sistema resolve, de forma **simbólica** (SymPy), o problema de otimização
$\nabla \pi = 0$, **classifica** o ponto crítico e entrega ao usuário leigo uma
**recomendação de preços** com a justificativa matemática de como ela foi obtida.

> Projeto da disciplina **Resolução de Problemas Multivariáveis** — Ciência da
> Computação, Centro Universitário do Pará (CESUPA). Metodologia *Project Based
> Learning* (PBL).

---

## 👥 Equipe

| Nome | Matrícula |
|---|---|
| *PEDRO PAULO DE MAGALHAES BEZERRA FILHO* |24070313 |
| *YURI MONTEIRO ALENCAR AGUIAR* |24070309 |
| *JOAO VITOR RATH DE SOUZA FRANCO* |24070338 |

---

## 📖 Descrição do projeto

- **Problema real (PBL):** precificação de produtos relacionados por um
  estabelecimento, baseado em FORBES, K. F. *Pricing of related products by a
  multiproduct monopolist.* Review of Industrial Organization, 3(3), 55–73, 1988.
  DOI: [10.1007/BF02229566](https://doi.org/10.1007/BF02229566).
- **Persona:** Marina, dona de uma cafeteria, que precisa decidir o preço de dois
  cafés que competem entre si (café coado × cappuccino).
- **Modelo:** lucro $\pi(p_1, p_2)$ — função quadrática de duas variáveis com termo
  cruzado; ótimo em forma fechada; classificação pela Hessiana.
  Veja a derivação completa em [`docs/02-modelagem.md`](docs/02-modelagem.md).

A documentação acadêmica está em [`docs/`](docs/):
[Prospecção](docs/01-prospeccao.md) · [Modelagem](docs/02-modelagem.md) ·
[Persona](docs/03-persona.md) · [Relatório](docs/04-relatorio.md) ·
[Slides (10)](docs/05-apresentacao.md) · [Guia de apresentação](docs/06-guia-apresentacao.md).

---

## 🧰 Requisitos

- **Python 3.10+** (testado em 3.13)
- Navegador web moderno (Chrome, Edge, Firefox)
- Conexão à internet **apenas** para o front-end (carrega o MathJax via CDN para
  renderizar as fórmulas)

Bibliotecas Python (instaladas via `requirements.txt`): FastAPI, Uvicorn,
Pydantic e SymPy.

---

## 🚀 Instalação e execução (passo a passo)

### 1. Obter o código

```bash
git clone https://github.com/pedropmbf/projeto-otimizacao-precos.git
cd projeto-otimizacao-precos
```

### 2. Criar e ativar um ambiente virtual

**Windows (PowerShell):**
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Iniciar o servidor

```bash
uvicorn app:app --reload
```

### 5. Abrir no navegador

Acesse **http://127.0.0.1:8000** — a interface será carregada automaticamente.

> A documentação interativa da API (Swagger) fica em
> **http://127.0.0.1:8000/docs**.

---

## 💡 Exemplo de uso

1. No seletor **"Tipo de negócio"**, escolha um cenário real (o padrão é a
   **Cafeteria** do relatório). Há 6 cenários calibrados com preços de mercado:
   cafeteria, hamburgueria, pizzaria, açaiteria, lanchonete e padaria. Você pode
   editar qualquer valor para a sua realidade.
2. Clique em **"Calcular preços ótimos"**.
3. O sistema retorna (cenário Cafeteria):

| Saída | Valor |
|---|---|
| Preço ótimo — Café Especial | **R$ 9,00** (~47 un./dia) |
| Preço ótimo — Cappuccino | **R$ 8,75** (~38 un./dia) |
| Lucro máximo estimado | **R$ 472,62/dia** |
| Classificação do ponto crítico | **máximo** (D = 416 > 0, $f_{p_1p_1} < 0$) |

Além dos números, o sistema desenha um **mapa de lucro** (curvas de nível com o
ponto ótimo destacado) e a seção **"Como a solução foi obtida"** com o gradiente,
a Hessiana e a explicação em texto.

### Exemplo via API (sem interface)

```bash
curl -X POST http://127.0.0.1:8000/api/otimizar ^
  -H "Content-Type: application/json" ^
  -d "{\"a1\":120,\"b1\":12,\"a2\":90,\"b2\":10,\"g\":4,\"m1\":3,\"m2\":2.5,\"F\":50}"
```

Cada parâmetro de entrada:

| Campo | Significado |
|---|---|
| `a1`, `a2` | demanda-base (intercepto) de cada produto |
| `b1`, `b2` | sensibilidade ao preço próprio (**> 0**) |
| `g` | efeito de substituição entre os produtos (substitutos: **> 0**) |
| `m1`, `m2` | custo unitário de cada produto |
| `F` | custo fixo (opcional, padrão 0) |

---

## 📁 Estrutura do projeto

```
projeto-otimizacao-precos/
├── backend/
│   ├── app.py            # API FastAPI + serve o front-end
│   ├── optimizer.py      # Motor simbólico (SymPy): gradiente, ∇π=0, Hessiana
│   └── requirements.txt
├── frontend/
│   ├── index.html        # Interface da persona
│   ├── style.css
│   └── app.js            # Chama a API e renderiza a recomendação
├── docs/                 # Documentação acadêmica (vira o relatório)
│   ├── 01-prospeccao.md
│   ├── 02-modelagem.md
│   ├── 03-persona.md
│   ├── 04-relatorio.md
│   └── 05-apresentacao.md
├── LICENSE
└── README.md
```

---

## 🤖 Uso de Inteligência Artificial

Este projeto utilizou assistência de IA (Claude). O uso está **declarado e
detalhado** na seção correspondente do relatório
([`docs/04-relatorio.md`](docs/04-relatorio.md)). A modelagem matemática foi
**verificada manualmente** (ver exemplo resolvido em
[`docs/02-modelagem.md`](docs/02-modelagem.md)).

---

## 📜 Licença

Distribuído sob a licença **MIT**. Veja [`LICENSE`](LICENSE).
