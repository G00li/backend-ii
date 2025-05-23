import logging
from logging.handlers import TimedRotatingFileHandler
from loguru import logger
import sys
import os

# Configuração do logging padrão do Python
def setup_standard_logging():
    # Cria o diretório de logs se não existir
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Configura o logger padrão
    standard_logger = logging.getLogger('standard')
    standard_logger.setLevel(logging.DEBUG)
    
    # Handler para arquivo com rotação diária
    file_handler = TimedRotatingFileHandler(
        'logs/standard.log',
        when='midnight',
        interval=1,
        backupCount=7,
        encoding='utf-8'
    )
    
    # Formato do log
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    
    # Handler para console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    # Adiciona os handlers ao logger
    standard_logger.addHandler(file_handler)
    standard_logger.addHandler(console_handler)
    
    return standard_logger

# Configuração do Loguru
def setup_loguru():
    # Remove o handler padrão
    logger.remove()
    
    # Adiciona handler para console
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="DEBUG"
    )
    
    # Adiciona handler para arquivo com rotação
    logger.add(
        "logs/loguru_{time}.log",
        rotation="1 day",
        retention="7 days",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        level="DEBUG"
    )
    
    return logger

def main():
    # Configura os loggers
    standard_logger = setup_standard_logging()
    loguru_logger = setup_loguru()
    
    # Exemplos de uso do logger padrão
    standard_logger.debug("Esta é uma mensagem de debug")
    standard_logger.info("Esta é uma mensagem de informação")
    standard_logger.warning("Esta é uma mensagem de aviso")
    standard_logger.error("Esta é uma mensagem de erro")
    
    # Exemplos de uso do Loguru
    loguru_logger.debug("Esta é uma mensagem de debug do Loguru")
    loguru_logger.info("Esta é uma mensagem de informação do Loguru")
    loguru_logger.warning("Esta é uma mensagem de aviso do Loguru")
    loguru_logger.error("Esta é uma mensagem de erro do Loguru")
    
    # Exemplo de log com contexto
    try:
        1/0
    except Exception as e:
        loguru_logger.exception("Ocorreu um erro: {}", e)

if __name__ == "__main__":
    main() 