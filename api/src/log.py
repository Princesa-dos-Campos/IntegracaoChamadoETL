import logging
from logging.config import fileConfig

class Log():
    def __init__(self):
        try:
            fileConfig('logging_config.ini')
            self.logger = logging.getLogger()
            self.logger.debug("Tempo restante: 'dados a serem impressos")
            print("Registro de Log realizado")
        except Exception as e:
            print("Erro no registro de Log...", e)
