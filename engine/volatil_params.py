"""
    read/write in a file the volatile params
"""
import json
import os
from engine.automation_config import AutomationConfig


class VolatileParams(AutomationConfig):
    """
        VolatileParams inherit AutomationConfig
        Methods:
            change_param
    """

    def __init__(self):
        self.path = "volatile_params.json"
        if not os.path.isfile(self.path):
            with open(self.path, "w") as json_file:
                json.dump({}, json_file)
        # with open(self.path) as file:
        #     self.args = json.load(file)
        super(VolatileParams, self).__init__(self.path)

    def change_param(self, param, value=None):
        """
            Check if volatile_params.json exist, if not the file is created
            Update the value of the parameter in the volatile_params.json

            param:
                Parameter that need to be changed
            value:
                The value of the parameter
                :rtype:
        """
        with open(self.path, "r") as json_file:
            data = json.load(json_file)

        data[param] = value

        with open(self.path, "w") as json_file:
            json.dump(data, json_file)
