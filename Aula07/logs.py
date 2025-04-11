import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename= 'app.log', 
    filemode= 'w'
)


logging.debug("Esta é uma mensagem de DEBUG")
logging.info("Essa é uma mensagem de ERRO")
logging.warning("Essa é uma mensagem de Warning")
logging.error("Esta é uma mensagem de Erro")