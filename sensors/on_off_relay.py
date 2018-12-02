import os


class OnOffRelay:

    def __init__(self, gpio_no):
        self.gpio_no = str(gpio_no)
        os.system("gpio -1 mode " + self.gpio_no + " out")

    def relay_on(self):
        print("relay on ----------")
        os.system("gpio -1 write " + self.gpio_no + " 0")

    def relay_off(self):
        os.system("gpio -1 write " + self.gpio_no + " 1")

    @staticmethod
    def all_lights_off(gpios):
        for gpio in gpios:
            os.system("gpio -1 write " + str(gpio) + " 1")