# Aula 10 – Segurança em Aplicações Python

Este exemplo mostra como criar um endpoint FastAPI que sanitiza a entrada do usuário, evitando ataques como XSS.

## Como rodar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```
2. Rode a API:
```bash
uvicorn main:app --reload
```
3. Teste:
```bash
pytest
```

## Exemplo de uso

`GET /safe-echo?user_input=<b>Oi!</b>` retorna `{ "safe_message": "&lt;b&gt;Oi!&lt;/b&gt;" }` 