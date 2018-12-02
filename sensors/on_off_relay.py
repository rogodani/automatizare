from gpiozero import DigitalOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


class OnOffRelay:

    def __init__(self, gpio_no):
        # factory = PiGPIOFactory(host='192.168.1.101')
        #TODO comment factory
        # self.relay = DigitalOutputDevice(gpio_no, active_high=False, pin_factory=factory)
        # print("initiate the object")
        self.relay = DigitalOutputDevice(gpio_no, active_high=False)

    def relay_on(self):
        self.relay.on()

    def relay_off(self):
        self.relay.off()