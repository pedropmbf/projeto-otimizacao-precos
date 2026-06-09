"""
API do projeto de otimizacao (FastAPI).

Fluxo:  persona insere dados (front-end)  ->  POST /api/otimizar  ->
        motor simbolico resolve  ->  front-end exibe a recomendacao.

Como executar:
    uvicorn app:app --reload
e abrir http://127.0.0.1:8000
"""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from optimizer import solve_pricing

app = FastAPI(
    title="Otimizador de Precos - Cafeteria",
    description=(
        "Calcula os precos que maximizam o lucro de dois produtos "
        "relacionados, usando derivadas parciais, gradiente e Hessiana."
    ),
    version="1.0.0",
)

# Libera o acesso do front-end (mesmo quando servido de outra origem)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Parametros(BaseModel):
    """Parametros numericos informados pela persona."""

    a1: float = Field(..., description="Demanda-base do Produto 1 (intercepto)")
    b1: float = Field(..., gt=0, description="Sensibilidade ao preco proprio do Produto 1")
    a2: float = Field(..., description="Demanda-base do Produto 2 (intercepto)")
    b2: float = Field(..., gt=0, description="Sensibilidade ao preco proprio do Produto 2")
    g: float = Field(..., description="Efeito cruzado entre os produtos (substitutos: g>0)")
    m1: float = Field(..., ge=0, description="Custo unitario do Produto 1")
    m2: float = Field(..., ge=0, description="Custo unitario do Produto 2")
    F: float = Field(0.0, ge=0, description="Custo fixo (opcional)")
    nome1: str = Field("Produto 1", description="Nome do Produto 1")
    nome2: str = Field("Produto 2", description="Nome do Produto 2")

    model_config = {
        "json_schema_extra": {
            "example": {
                "a1": 120, "b1": 12, "a2": 90, "b2": 10,
                "g": 4, "m1": 3, "m2": 2.5, "F": 50,
            }
        }
    }


@app.post("/api/otimizar")
def otimizar(params: Parametros) -> dict:
    """Recebe os parametros e devolve a solucao otima completa."""
    return solve_pricing(params.model_dump())


@app.get("/api/saude")
def saude() -> dict:
    """Endpoint simples de verificacao."""
    return {"status": "ok"}


# ---- Servir o front-end estatico -----------------------------------------
# Mantido por ULTIMO para nao sobrepor as rotas /api/*.
_FRONTEND = Path(__file__).resolve().parent.parent / "frontend"
if _FRONTEND.is_dir():
    app.mount("/", StaticFiles(directory=str(_FRONTEND), html=True), name="frontend")
