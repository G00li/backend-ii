# Aula 13 – Boas Práticas de Web com Django e FastAPI

Este exemplo mostra como criar um endpoint "Hello World" tanto em Django quanto em FastAPI.

## FastAPI

1. Instale as dependências:
```bash
pip install fastapi uvicorn
```
2. Rode:
```bash
uvicorn fastapi_app.main:app --reload
```
3. Acesse: http://localhost:8000/

## Django

1. Instale as dependências:
```bash
pip install django
```
2. Crie um projeto Django e adicione a view do arquivo `views.py`.
3. Configure a URL para apontar para a view `hello`.
4. Rode:
```bash
python manage.py runserver
```
5. Acesse: http://localhost:8000/ 