from gpiozero import DigitalOutputDevice
from time import sleep


class OnOffRelay:

    def __init__(self, gpio_no):
        self.relay = DigitalOutputDevice(gpio_no, active_high=False)

    def relay_on(self, time_on):
        self.relay.on()
        sleep(time_on)
        self.relay_off()

    def relay_off(self):
        self.relay.off()