"""
    Check is the system was reboot
"""
from time import sleep
import logging
from engine.commands import Commands


class Reboot:
    def __init__(self, sleep_time):
        self.sleep_time = sleep_time

    def start(self, temp_log_file):
        sleep(self.sleep_time * 60)
        if temp_log_file:
            logging.info("--- SYSTEM REBOOT --- you can start send commands")
            return "\n--- SYSTEM REBOOT ---\nyou can start send commands\n" + Commands().commands_list()
        else:
            logging.info("--- SYSTEM REBOOT --- !!! LOG FILE IS MISSING !!!")
            return "\n--- SYSTEM REBOOT ---\n!!! LOG FILE IS MISSING !!!"