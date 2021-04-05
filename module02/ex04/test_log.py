from ai42.logging.log import log
from time import sleep


class Logged:
    asd = 0

    @log
    def __init__(self):
        self.asd = 1
        sleep(0.2)

    @log
    def idk(self):
        print('idk')
        sleep(0.85)


obj = Logged()
obj.idk()
obj.idk()
obj.idk()
