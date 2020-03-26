from loguru import logger
import json


class Version:

    def __init__(self):
        pass

    @staticmethod
    def show_version():
        with open('./config.json') as c:
            config = json.load(c)

        logger.info('Name: {}'.format(config['project']['name']))
        logger.info('Version: {}'.format(config['project']['version']))
        logger.info('Started: {}'.format(config['project']['date']))


if __name__ == '__main__':
    v = Version()
    v.show_version()
