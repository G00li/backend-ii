# Aula 06 - Padrões Avançados de Async e Técnicas de Concorrência

Este projeto implementa um limitador de taxa (rate limiter) assíncrono em Python, demonstrando padrões avançados de programação assíncrona e técnicas de concorrência.

## Estrutura do Projeto

- `rate_limiter.py`: Implementação do limitador de taxa assíncrono
- `test_rate_limiter.py`: Testes do limitador de taxa
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

Para executar o exemplo:
```bash
python rate_limiter.py
```

## Executando os Testes

Para executar os testes:
```bash
pytest test_rate_limiter.py
```

## Funcionalidades

- Limitador de taxa assíncrono usando asyncio
- Decorator para fácil aplicação do limite de taxa
- Suporte a múltiplas chamadas concorrentes
- Testes automatizados com pytest-asyncio

## Exemplo de Uso

```python
@rate_limit(max_calls=2, time_period=1.0)
async def minha_funcao():
    # Esta função será limitada a 2 chamadas por segundo
    pass
```

## Características

- Controle preciso de taxa de chamadas
- Suporte a operações assíncronas
- Thread-safe usando asyncio.Lock
- Fácil de integrar com código existente 