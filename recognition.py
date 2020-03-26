from imutils.video import VideoStream
from time import localtime, sleep
from loguru import logger
from pyzbar import pyzbar
import pandas as pd
import imutils
import cv2


class Recognition:

    def __init__(self, config):
        self.config = config
        self.cart_log = list()

    def start_camera(self):

        if bool(int(self.config['camera']['raspberry'])):
            camera = VideoStream(usePiCamera=bool(int(self.config['camera']['raspberry'])),
                                 resolution=(self.config['camera']['resolution']['width'],
                                             self.config['camera']['resolution']['height']),
                                 framerate=self.config['camera']['fps']).start()
        else:
            camera = VideoStream(src=self.config['camera']['usb']).start()

        sleep(0.8)

        return camera

    @staticmethod
    def scanner(frame):

        code = ''

        image = pyzbar.decode(frame)

        for data in image:
            text = data.data.decode('utf-8')
            code = '{}'.format(text)

        return code

    def process_image(self, frame):

        frame = imutils.resize(frame, self.config['camera']['resize'])
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        return frame

    @staticmethod
    def get_format_date():

        date = localtime()

        year, month, day, hour, minutes, seconds = date[0], date[1], date[2], date[3], date[4], date[5]

        def verify_number(number):
            if len(str(number)) == 1:
                number = '0{}'.format(number)

            return number

        year = str(year)
        year = year[2:]
        day = verify_number(day)
        month = verify_number(month)
        hour = verify_number(hour)
        minutes = verify_number(minutes)
        seconds = verify_number(seconds)

        format_data = '{}/{}/{} {}:{}:{}'.format(day, month, year, hour, minutes, seconds)

        return format_data

    def reader(self):

        camera = self.start_camera()

        truck = 0

        while True:

            try:

                frame = camera.read()
                frame = self.process_image(frame)

                code = self.scanner(frame)

                if code != '':

                    if code == self.config['project']['pattern']:
                        if len(self.cart_log) > 0:

                            carts = ''

                            for c in self.cart_log:
                                carts += '{} '.format(c)

                            logs = {

                                'number_truck': truck,
                                'total_cart': len(self.cart_log),
                                'carts': carts,
                                'data': self.get_format_date(),
                            }

                            logger.success(logs)
                            self.cart_log = list()

                            df = pd.DataFrame(logs, index=[0])

                            logger.success(logs)

                            with open('./logs/logs.csv', 'a') as f:
                                df.to_csv(f, header=False)

                                logger.success('Saved logs')

                    else:

                        if code.split('-')[0] == 'CAM':
                            truck = code.split('-')[1]
                        else:

                            self.cart_log.append(code)
                            self.cart_log = sorted(list(set(self.cart_log)))

                if bool(int(self.config['camera']['show_image'])):
                    cv2.imshow('Image', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                else:
                    pass
            except Exception as e:
                logger.error(e)

                with open('./logs/error.txt', 'a') as f:
                    f.write('\n{}'.format(str(e)))

        camera.stop()
        cv2.destroyAllWindows()
