import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger("MeuLogger")
logger.setLevel(logging.DEBUG)

handler = TimedRotatingFileHandler(
    filename="logs_desafio.log", 
    when='D', 
    interval = 1, 
    backupCount=5,
    encoding='utf-8'
)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


logger.debug("Mensagem de DEBUG para teste")
logger.info("Mensagem de INFO para teste")
logger.warning("Mensagem de WARNING para teste")
logger.error("Mensagem de ERROR para teste")
