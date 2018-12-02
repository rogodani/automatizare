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
        if command == "1":
            pass
        elif command == "2":
            OnOffRelay(17).relay_on()
        elif command == "3":
            OnOffRelay(18).relay_on()
        elif command == "4":
            OnOffRelay(18).relay_on()
        elif command == "5":
            OnOffRelay(18).relay_on()
        elif command == "6":
            OnOffRelay.all_lights_off(AutomationConfig("test.json").lights_gpios())
