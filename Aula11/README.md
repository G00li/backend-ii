# Aula 11 – Construindo APIs GraphQL com Python

Exemplo de API GraphQL usando Strawberry e FastAPI.

## Como rodar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```
2. Rode a API:
```bash
uvicorn main:app --reload
```
3. Acesse o playground em `http://localhost:8000/graphql`

## Exemplo de query
```graphql
{
  user { id name }
}
```

## Exemplo de mutation
```graphql
mutation {
  updateName(name: "Maria") { id name }
}
``` 