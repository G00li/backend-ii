import fastapi 
import json 
from pydantic import BaseModel 

app = fastapi.FastAPI()

class Book(BaseModel):
    id: int
    title: str 
    author: str
    genre: str
    description: str
    isbn: str
    image: str
    published: str
    publisher: str

def load_books(): 
    try:
        with open("books.json", "r", encoding = "utf-8") as file:
            data = json.load(file)
            return data.get("data", [])
    except FileNotFoundError:
        return {"message": "Arquivo nao encontrado"}
    
books = load_books()


@app.get("/")
def Homepage():
    return {"message": "Bem vindo a API de livros"}


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"message": "Livro nao encontrado"}
