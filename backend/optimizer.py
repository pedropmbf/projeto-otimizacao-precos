"""
Motor de otimizacao simbolico do projeto.

Modelo: precificacao de DOIS produtos relacionados (substitutos) por um
unico estabelecimento (monopolista multiproduto), inspirado em
Forbes, K. F. (1988), "Pricing of related products by a multiproduct
monopolist", Review of Industrial Organization, 3(3), 55-73.

Variaveis de decisao  : p1, p2  (precos de venda de cada produto)
Parametros do problema : a1,b1,a2,b2,g,m1,m2,F  (informados pela persona)

Demanda (linear, com efeito cruzado de substitutos):
    q1 = a1 - b1*p1 + g*p2
    q2 = a2 - b2*p2 + g*p1

Lucro (funcao objetivo):
    pi(p1,p2) = (p1 - m1)*q1 + (p2 - m2)*q2 - F

Todo o trabalho matematico (derivadas parciais, gradiente, sistema
nabla(pi)=0, Hessiana e classificacao) e feito de forma SIMBOLICA com
SymPy. Os parametros numericos da persona sao substituidos no final.
"""

from __future__ import annotations

import sympy as sp

# --------------------------------------------------------------------------
# 1) Construcao simbolica do modelo (feita uma unica vez ao importar)
# --------------------------------------------------------------------------

# Variaveis de decisao (precos)
p1, p2 = sp.symbols("p1 p2", real=True)

# Parametros do problema
a1, b1, a2, b2, g, m1, m2, F = sp.symbols(
    "a1 b1 a2 b2 g m1 m2 F", real=True
)

# Funcoes de demanda (substitutos: demanda cai com o preco proprio e
# sobe com o preco do concorrente interno -> coeficiente cruzado g > 0)
q1 = a1 - b1 * p1 + g * p2
q2 = a2 - b2 * p2 + g * p1

# Funcao objetivo: lucro total
profit = (p1 - m1) * q1 + (p2 - m2) * q2 - F

# Gradiente: derivadas parciais de primeira ordem
dpi_dp1 = sp.diff(profit, p1)
dpi_dp2 = sp.diff(profit, p2)
gradient = sp.Matrix([dpi_dp1, dpi_dp2])

# Hessiana: matriz das derivadas parciais de segunda ordem
H = sp.hessian(profit, (p1, p2))  # = [[-2*b1, 2*g], [2*g, -2*b2]]

# Solucao simbolica geral do sistema nabla(pi) = 0 (forma fechada)
_sol = sp.solve([dpi_dp1, dpi_dp2], [p1, p2], dict=True)[0]
p1_star_sym = sp.simplify(_sol[p1])
p2_star_sym = sp.simplify(_sol[p2])

# Sensibilidade (estatica comparativa): como o otimo reage a cada parametro
SENS = {
    "dp1_dm1": sp.simplify(sp.diff(p1_star_sym, m1)),
    "dp1_dm2": sp.simplify(sp.diff(p1_star_sym, m2)),
    "dp2_dm2": sp.simplify(sp.diff(p2_star_sym, m2)),
    "dp2_dm1": sp.simplify(sp.diff(p2_star_sym, m1)),
    "dp1_da1": sp.simplify(sp.diff(p1_star_sym, a1)),
    "dp2_da2": sp.simplify(sp.diff(p2_star_sym, a2)),
}

# Parametros na ordem em que serao substituidos
_PARAM_SYMBOLS = (a1, b1, a2, b2, g, m1, m2, F)
_PARAM_NAMES = ("a1", "b1", "a2", "b2", "g", "m1", "m2", "F")


# --------------------------------------------------------------------------
# 2) Strings em LaTeX (para o front-end exibir a "conta" de forma bonita)
# --------------------------------------------------------------------------

LATEX = {
    "q1": sp.latex(q1),
    "q2": sp.latex(q2),
    "profit": r"\pi(p_1,p_2) = (p_1-m_1)\,q_1 + (p_2-m_2)\,q_2 - F",
    "grad1": sp.latex(sp.expand(dpi_dp1)),
    "grad2": sp.latex(sp.expand(dpi_dp2)),
    "hessian": sp.latex(H),
    "p1_star": sp.latex(p1_star_sym),
    "p2_star": sp.latex(p2_star_sym),
}


# --------------------------------------------------------------------------
# 3) Funcao publica: resolve para um conjunto numerico de parametros
# --------------------------------------------------------------------------

def _f(x) -> float:
    """Converte uma expressao SymPy numerica para float Python."""
    return float(sp.N(x))


def solve_pricing(params: dict) -> dict:
    """
    Recebe um dicionario com os parametros numericos e devolve a solucao
    otima completa, com classificacao do ponto critico, sensibilidade e
    uma justificativa legivel em portugues.
    """
    # ---- leitura e validacao basica das entradas -------------------------
    erros: list[str] = []
    avisos: list[str] = []

    try:
        vals = {name: float(params[name]) for name in _PARAM_NAMES}
    except (KeyError, TypeError, ValueError):
        # F (custo fixo) e opcional; assume 0 se ausente/invalido
        vals = {}
        for name in _PARAM_NAMES:
            raw = params.get(name, 0.0 if name == "F" else None)
            if raw is None:
                erros.append(f"Parametro obrigatorio ausente: '{name}'.")
            else:
                try:
                    vals[name] = float(raw)
                except (TypeError, ValueError):
                    erros.append(f"Parametro '{name}' nao e um numero valido.")
    if erros:
        return {"ok": False, "erros": erros, "avisos": avisos}

    # Coerencia do modelo: sensibilidade de preco propria deve ser positiva
    if vals["b1"] <= 0 or vals["b2"] <= 0:
        erros.append(
            "Os coeficientes de preco proprio b1 e b2 devem ser positivos "
            "(a demanda precisa cair quando o proprio preco sobe)."
        )
    if erros:
        return {"ok": False, "erros": erros, "avisos": avisos}

    subs = {sym: vals[name] for sym, name in zip(_PARAM_SYMBOLS, _PARAM_NAMES)}

    # ---- Hessiana numerica e classificacao (teste da 2a derivada) --------
    Hn = H.subs(subs)
    h11 = _f(Hn[0, 0])
    h12 = _f(Hn[0, 1])
    h22 = _f(Hn[1, 1])
    detH = h11 * h22 - h12 * h12  # D = f_xx*f_yy - (f_xy)^2

    if detH < 0:
        classificacao = "ponto de sela"
    elif detH == 0:
        classificacao = "indeterminado (teste inconclusivo)"
    elif h11 < 0:
        classificacao = "maximo"
    else:
        classificacao = "minimo"

    autovalores = sorted(_f(ev) for ev in Hn.eigenvals(multiple=True))

    # Se nao for maximo, o problema de lucro nao tem otimo interior util
    if classificacao != "maximo":
        avisos.append(
            "Atencao: com estes parametros o ponto critico NAO e um maximo "
            f"(classificacao: {classificacao}). Para haver preco otimo de "
            "lucro e necessario b1*b2 > g^2 (o efeito de preco proprio deve "
            "superar o cruzado). Revise os coeficientes de demanda."
        )

    # ---- ponto otimo (substitui os numeros na solucao simbolica) ---------
    p1v = _f(p1_star_sym.subs(subs))
    p2v = _f(p2_star_sym.subs(subs))

    q1v = _f(q1.subs(subs).subs({p1: p1v, p2: p2v}))
    q2v = _f(q2.subs(subs).subs({p1: p1v, p2: p2v}))
    lucro = _f(profit.subs(subs).subs({p1: p1v, p2: p2v}))

    # ---- checagens de dominio / viabilidade economica --------------------
    if p1v < vals["m1"] or p2v < vals["m2"]:
        avisos.append(
            "O preco otimo ficou abaixo do custo unitario de algum produto "
            "(margem negativa). A solucao interior nao e economicamente "
            "viavel com estes dados."
        )
    if q1v < 0 or q2v < 0:
        avisos.append(
            "A demanda otima de algum produto ficou negativa (q < 0). Na "
            "pratica isso significa parar de vender esse item: o otimo real "
            "esta na fronteira do dominio, nao no interior."
        )

    # ---- sensibilidade (estatica comparativa, avaliada nos numeros) ------
    sensibilidade = {k: _f(v.subs(subs)) for k, v in SENS.items()}

    # ---- nomes dos produtos (opcionais) ----------------------------------
    nome1 = str(params.get("nome1") or "Produto 1")
    nome2 = str(params.get("nome2") or "Produto 2")

    # ---- justificativa legivel (PT-BR) -----------------------------------
    justificativa = _montar_justificativa(
        nome1, nome2, p1v, p2v, q1v, q2v, lucro,
        h11, h12, h22, detH, classificacao, sensibilidade,
    )

    return {
        "ok": True,
        "erros": [],
        "avisos": avisos,
        "entrada": vals,
        "modelo": {
            "lucro_latex": LATEX["profit"],
            "q1_latex": LATEX["q1"],
            "q2_latex": LATEX["q2"],
            "grad_latex": [
                r"\frac{\partial \pi}{\partial p_1} = " + LATEX["grad1"],
                r"\frac{\partial \pi}{\partial p_2} = " + LATEX["grad2"],
            ],
            "hessiana_latex": r"H = " + LATEX["hessian"],
            "p1_star_latex": r"p_1^{*} = " + LATEX["p1_star"],
            "p2_star_latex": r"p_2^{*} = " + LATEX["p2_star"],
        },
        "solucao": {
            "p1": round(p1v, 2),
            "p2": round(p2v, 2),
            "q1": round(q1v, 2),
            "q2": round(q2v, 2),
            "lucro": round(lucro, 2),
            "classificacao": classificacao,
            "hessiana_num": [[h11, h12], [h12, h22]],
            "det_hessiana": detH,
            "autovalores": autovalores,
        },
        "sensibilidade": sensibilidade,
        "nomes": {"p1": nome1, "p2": nome2},
        "grafico": _malha_lucro(subs, p1v, p2v),
        "justificativa": justificativa,
    }


def _malha_lucro(subs: dict, p1v: float, p2v: float, n: int = 45) -> dict | None:
    """
    Gera uma malha (grid) de valores do lucro ao redor do ponto otimo, para o
    front-end desenhar as curvas de nivel. Reaproveita a propria funcao de lucro
    simbolica, convertida em funcao numerica rapida via lambdify.
    """
    import math

    if not (math.isfinite(p1v) and math.isfinite(p2v)):
        return None
    if max(abs(p1v), abs(p2v)) > 1e6:
        return None

    f = sp.lambdify((p1, p2), profit.subs(subs), modules="math")

    # Janela centrada no otimo (garante curvas de nivel fechadas em volta dele)
    r1 = max(abs(p1v) * 0.6, 2.0)
    r2 = max(abs(p2v) * 0.6, 2.0)
    x_lo, x_hi = max(p1v - r1, 0.0), p1v + r1
    y_lo, y_hi = max(p2v - r2, 0.0), p2v + r2

    xs = [x_lo + (x_hi - x_lo) * i / (n - 1) for i in range(n)]
    ys = [y_lo + (y_hi - y_lo) * j / (n - 1) for j in range(n)]
    z = [[float(f(x, y)) for x in xs] for y in ys]
    return {"p1": xs, "p2": ys, "z": z}


def _brl(x: float) -> str:
    """Formata um numero como moeda (R$) em padrao brasileiro."""
    s = f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"


def _montar_justificativa(
    nome1, nome2, p1v, p2v, q1v, q2v, lucro,
    h11, h12, h22, detH, classificacao, sens,
) -> str:
    linhas = []
    linhas.append("COMO A SOLUCAO FOI OBTIDA")
    linhas.append("")
    linhas.append(
        "1) Montamos o lucro pi(p1,p2) = (p1-m1)*q1 + (p2-m2)*q2 - F, com as "
        "demandas q1 e q2 dependendo dos dois precos (produtos substitutos)."
    )
    linhas.append(
        "2) Calculamos o gradiente (derivadas parciais) e resolvemos o "
        "sistema nabla(pi)=0 para achar o ponto critico."
    )
    linhas.append(
        f"3) Hessiana: f_xx={h11:.4g}, f_yy={h22:.4g}, f_xy={h12:.4g}. "
        f"O teste da segunda derivada usa D = f_xx*f_yy - (f_xy)^2 = {detH:.4g}."
    )
    if classificacao == "maximo":
        linhas.append(
            f"   Como D > 0 e f_xx < 0, o ponto critico e um MAXIMO de lucro."
        )
    else:
        linhas.append(
            f"   Pela regra do teste, a classificacao foi: {classificacao}."
        )
    linhas.append("")
    linhas.append("RECOMENDACAO")
    linhas.append(
        f"- Preco otimo de {nome1}: {_brl(p1v)}  (vendendo ~{q1v:.1f} un.)"
    )
    linhas.append(
        f"- Preco otimo de {nome2}: {_brl(p2v)}  (vendendo ~{q2v:.1f} un.)"
    )
    linhas.append(f"- Lucro maximo estimado: {_brl(lucro)}")
    linhas.append("")
    linhas.append("SENSIBILIDADE (estatica comparativa)")
    linhas.append(
        f"- Se o custo de {nome1} subir R$ 1,00, seu preco otimo sobe "
        f"~{_brl(sens['dp1_dm1'])} (dp1*/dm1 = {sens['dp1_dm1']:.4g})."
    )
    linhas.append(
        f"- Se a demanda-base de {nome1} subir 1 unidade, seu preco otimo sobe "
        f"~{_brl(sens['dp1_da1'])} (dp1*/da1 = {sens['dp1_da1']:.4g})."
    )
    return "\n".join(linhas)


# --------------------------------------------------------------------------
# 4) Execucao direta para teste rapido no terminal
# --------------------------------------------------------------------------

if __name__ == "__main__":
    exemplo = {
        "a1": 120, "b1": 12, "a2": 90, "b2": 10,
        "g": 4, "m1": 3, "m2": 2.5, "F": 50,
    }
    import json
    res = solve_pricing(exemplo)
    print(json.dumps(res["solucao"], indent=2, ensure_ascii=False))
    print()
    print(res["justificativa"])
