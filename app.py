from recognition import Recognition
import json


class App:

    def __init__(self):
        self.config = self.read_config()
        self.recognition = Recognition(config=self.config)

    def run(self):
        self.read_config()
        self.recognition.reader()

    @staticmethod
    def read_config():
        with open('./config.json') as c:
            config = json.load(c)

        return config


if __name__ == '__main__':
    app = App()
    app.run()
