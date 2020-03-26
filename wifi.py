from PyAccessPoint import pyaccesspoint as pa
from loguru import logger


class Wifi:

    def __init__(self):
        self.config = self.read_config()

    def create_network(self):
        logger.info('Configurando o ponto de acesso...')

        wifi = pa.AccessPoint(ssid=self.config['wifi']['ssid'], password=self.config['wifi']['password'])

        logger.info('Iniciando o ponto de acesso...')

        wifi.stop()
        wifi.start()

        logger.success('Processo concluído.')

    @staticmethod
    def read_config():
        with open('./config.json') as c:
            config = c.read()
            print(config)

        return config

    def run(self):
        self.create_network()


if __name__ == '__main__':
    w = Wifi()
    w.run()
