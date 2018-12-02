"""
    preparing a message with the commands
"""

from engine.automation_config import AutomationConfig
from sensors.on_off_relay import OnOffRelay


class Menu():
    """
        Methods:
            commands_list
    """

    def __init__(self):
        self.menu = dict(AutomationConfig("menu.json").args)

    def menu_list(self):
        """
            return:
                a message with the avaibale commands
        """
        msg = ""
        for key in self.menu.keys():
            msg += key + ": " + self.menu[key] + "\n"
        return msg

    def menu_options(self):
        return self.menu.keys()

    def commands(self, command):
        print("command:", command)
        if command == "2":
            OnOffRelay(17).relay_on(time_on=3)
