from fastapi import FastAPI
import asyncio
from typing import Dict, List

app = FastAPI(title="API Assíncrona de Dados")

# Simulação de fontes de dados
async def fetch_data_source_1() -> Dict:
    await asyncio.sleep(1)  # Simula uma operação I/O
    return {"source": "API 1", "data": "Dados da primeira fonte"}

async def fetch_data_source_2() -> Dict:
    await asyncio.sleep(2)  # Simula uma operação I/O
    return {"source": "API 2", "data": "Dados da segunda fonte"}

@app.get("/data")
async def get_data():
    """
    Endpoint que busca dados de múltiplas fontes de forma assíncrona
    """
    # Usando asyncio.gather para executar as chamadas em paralelo
    results = await asyncio.gather(
        fetch_data_source_1(),
        fetch_data_source_2()
    )
    
    return {
        "message": "Dados obtidos com sucesso",
        "results": results
    }

@app.get("/health")
async def health_check():
    """
    Endpoint para verificar a saúde da API
    """
    return {"status": "healthy"} 