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

    def __init__(self, CONFIG_FILE):
        self.menu = dict(AutomationConfig("menu.json").args)
        self.CONFIG = AutomationConfig(CONFIG_FILE)

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
            OnOffRelay(self.CONFIG.get_param("doorLights")).relay_on()
        elif command == "3":
            OnOffRelay(self.CONFIG.get_param("parkingPlaceLights")).relay_on()
        elif command == "4":
            OnOffRelay(self.CONFIG.get_param("kitchenTerraceLights")).relay_on()
        elif command == "5":
            OnOffRelay(self.CONFIG.get_param("backyardLights")).relay_on()
        elif command == "6":
            OnOffRelay.all_lights_off(self.CONFIG.lights_gpios())
