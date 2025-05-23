# Aula 07 - Implementando Práticas de Logging em Python

Este projeto demonstra diferentes abordagens para implementar logging em Python, utilizando tanto o módulo de logging padrão quanto a biblioteca Loguru.

## Estrutura do Projeto

- `logger_example.py`: Implementação dos sistemas de logging
- `test_logger.py`: Testes do sistema de logging
- `requirements.txt`: Dependências do projeto
- `logs/`: Diretório onde os arquivos de log são armazenados

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
python logger_example.py
```

## Executando os Testes

Para executar os testes:
```bash
pytest test_logger.py
```

## Funcionalidades

### Logging Padrão do Python
- Rotação diária de arquivos de log
- Formatação personalizada
- Múltiplos handlers (console e arquivo)
- Níveis de log configuráveis

### Loguru
- Interface mais amigável
- Rotação automática de logs
- Formatação colorida no console
- Retenção configurável de logs

## Exemplo de Uso

```python
# Usando o logger padrão
standard_logger.info("Mensagem de informação")

# Usando o Loguru
loguru_logger.info("Mensagem de informação do Loguru")
```

## Características

- Suporte a múltiplos níveis de log (DEBUG, INFO, WARNING, ERROR)
- Rotação automática de arquivos de log
- Formatação personalizada
- Logs tanto em console quanto em arquivo
- Tratamento de exceções com stack trace 