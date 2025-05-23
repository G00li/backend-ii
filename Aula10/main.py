from fastapi import FastAPI, Query
from html import escape

app = FastAPI()

@app.get("/safe-echo")
def safe_echo(user_input: str = Query(..., min_length=1, max_length=100)):
    sanitized = escape(user_input)
    return {"safe_message": sanitized}

@app.get("/health")
def health():
    return {"status": "ok"} 