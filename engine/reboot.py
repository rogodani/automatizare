"""
    Check is the system was reboot
"""
from time import sleep
import logging
from engine.menu import Menu


class Reboot:
    """
        Methods:
            start
    """

    def __init__(self, sleep_time):
        self.sleep_time = sleep_time
        logging.info("Reboot delay: %d" % (self.sleep_time))

    def start(self, temp_log_file):
        """
            Parameters:
                temp_log_file: path to the temperature log file
            Return:
                a message if the system is ready or not
        """
        sleep(self.sleep_time * 60)
        if temp_log_file:
            msg = "--- SYSTEM REBOOT --- you can start send commands"
            logging.info(msg)
            return msg + Menu().menu_list()
        msg = "--- SYSTEM REBOOT --- !!! LOG FILE IS MISSING !!!"
        logging.info(msg)
        return msg
