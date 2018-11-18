"""
    read/write in a file the volatile params
"""
from engine.automation_config import AutomationConfig
import json
import os


class VolatileParams(AutomationConfig):
    """
        VolatileParams inherit AutomationConfig
        Methods:
            change_param
    """

    def __init__(self):
        self.path = "volatile_params.json"
        if not os.path.isfile(self.path):
            with open(self.path, "w") as jsonFile:
                json.dump({}, jsonFile)
        with open(self.path) as file:
            self.args = json.load(file)

    def change_param(self, param, value=None):
        """
            Check if volatile_params.json exist, if not the file is created
            Update the value of the parameter in the volatile_params.json

            param:
                Parameter that need to be changed
            value:
                The value of the parameter
        """
        with open(self.path, "r") as jsonFile:
            data = json.load(jsonFile)

        print(data)
        data[param] = value

        with open(self.path, "w") as jsonFile:
            json.dump(data, jsonFile)
