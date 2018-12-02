"""
    Parsing the provided automation config file
"""
import json


class AutomationConfig:
    """
        Methods:
            get_param
            twitter_api_details
    """
    # twitter api connection details
    CONSUMER_KEY = 'consumerKey'
    CONSUMER_SECRET = 'consumerSecret'
    ACCESS_TOKEN_KEY = 'accessTokenKey'
    ACCESS_TOKEN_SECRET = 'accessTokenSecret'

    def __init__(self, config):
        with open(config) as file:
            self.args = json.load(file)

    def get_param(self, param, default=None):
        """
            Parameters:
                param: the parameter which should be check in the automation config file
                default: the default value to be set for a param if it's value is None
            Return:
                The parameter value
        """
        value = self.args.get(param)
        if value is None:
            value = default
        return value

    def twitter_api_details(self):
        """
            Return:
                The connection parameters for twitter api"
        """
        return (self.get_param(self.CONSUMER_KEY), self.get_param(self.CONSUMER_SECRET),
                self.get_param(self.ACCESS_TOKEN_KEY), self.get_param(self.ACCESS_TOKEN_SECRET))

    def lights_gpios(self):
        return [self.get_param(item) for item in self.args if "lights" in str(item).lower()]
