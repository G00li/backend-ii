# Aula 04 - Multi-processing em Python

Este projeto demonstra o uso de multi-processing em Python para calcular fatoriais de números em paralelo.

## Estrutura do Projeto

- `factorial_processor.py`: Implementação principal do processamento paralelo
- `test_factorial.py`: Testes unitários para a função fatorial
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

Para executar o processador de fatorial:
```bash
python factorial_processor.py
```

## Executando os Testes

Para executar os testes:
```bash
pytest test_factorial.py
```

## Funcionalidades

- Cálculo de fatorial usando multi-processing
- Medição de tempo de execução para cada cálculo
- Testes unitários para garantir a corretude do cálculo 