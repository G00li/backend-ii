# Aula 05 - Programação Assíncrona com asyncio e FastAPI

Este projeto demonstra o uso de programação assíncrona em Python usando FastAPI e asyncio para criar uma API que busca dados de múltiplas fontes simultaneamente.

## Estrutura do Projeto

- `main.py`: Implementação da API FastAPI
- `test_api.py`: Testes da API
- `requirements.txt`: Dependências do projeto

## Instalação

1. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando o Projeto

Para iniciar o servidor:
```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`

## Documentação da API

A documentação interativa da API está disponível em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

- `GET /health`: Verifica o status da API
- `GET /data`: Busca dados de múltiplas fontes de forma assíncrona

## Executando os Testes

Para executar os testes:
```bash
pytest test_api.py
```

## Funcionalidades

- Endpoints assíncronos usando FastAPI
- Busca de dados de múltiplas fontes em paralelo
- Testes automatizados
- Documentação automática da API 