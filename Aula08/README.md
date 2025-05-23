# Aula 08 - Introdução ao Testing em Python com pytest

Este projeto demonstra o uso do pytest para testar uma calculadora em Python, mostrando diferentes técnicas de teste e boas práticas.

## Estrutura do Projeto

- `calculator.py`: Implementação da calculadora
- `test_calculator.py`: Testes da calculadora
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

## Executando os Testes

Para executar todos os testes:
```bash
pytest
```

Para executar os testes com cobertura:
```bash
pytest --cov=calculator
```

## Funcionalidades da Calculadora

- Adição
- Subtração
- Multiplicação
- Divisão
- Potenciação
- Fatorial

## Exemplos de Testes

### Testes Básicos
```python
def test_add(calculator):
    assert calculator.add(2, 3) == 5
```

### Testes de Exceções
```python
def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5, 0)
```

### Testes Parametrizados
```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
])
def test_add_parametrized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected
```

## Características

- Uso de fixtures do pytest
- Testes parametrizados
- Verificação de exceções
- Cobertura de código
- Documentação clara
- Tipagem estática 