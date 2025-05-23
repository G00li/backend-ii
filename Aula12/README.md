# Aula 12 – Desenvolvendo Serviços gRPC em Python

Este exemplo mostra como criar um serviço gRPC simples em Python que retorna o cubo de um número.

## Como rodar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```
2. Gere os arquivos Python a partir do proto:
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. cube.proto
```
3. Rode o servidor:
```bash
python server.py
```
4. Em outro terminal, rode o cliente:
```bash
python client.py
```

## Teste automatizado
```bash
pytest test_grpc.py
``` 