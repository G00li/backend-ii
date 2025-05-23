import pytest
import os
import logging
from logger_example import setup_standard_logging, setup_loguru

def test_standard_logger_creation():
    logger = setup_standard_logging()
    assert isinstance(logger, logging.Logger)
    assert logger.name == 'standard'
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) == 2  # Console e arquivo

def test_loguru_setup():
    logger = setup_loguru()
    assert logger is not None
    # Verifica se o diretório de logs foi criado
    assert os.path.exists('logs')

def test_log_file_creation():
    # Limpa logs existentes
    if os.path.exists('logs'):
        for file in os.listdir('logs'):
            os.remove(os.path.join('logs', file))
    
    # Configura os loggers
    standard_logger = setup_standard_logging()
    loguru_logger = setup_loguru()
    
    # Gera alguns logs
    standard_logger.info("Teste de log padrão")
    loguru_logger.info("Teste de log Loguru")
    
    # Verifica se os arquivos foram criados
    assert os.path.exists('logs/standard.log')
    assert any(file.startswith('loguru_') for file in os.listdir('logs')) 