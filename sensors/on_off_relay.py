import os


class OnOffRelay:

    def __init__(self, gpio_no):
        self.gpio_no = gpio_no
        os.system("gpio -g mode " + self.gpio_no + " out")

    def relay_on(self):
        print("relay on ----------")
        os.system("gpio -g write " + self.gpio_no + " 0")

    def relay_off(self):
        os.system("gpio -g write " + self.gpio_no + " 1")