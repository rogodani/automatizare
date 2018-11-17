"""
    connecting, parsing and sending messages on twitter
"""
import twitter


class TwitterIntegration:
    """
        Methods:
            get_param
            twitter_api_details
    """

    def __init__(self, connection_details):
        print(connection_details)
        self.consumer_key = connection_details[0]
        self.consumer_secret = connection_details[1]
        self.access_token_key = connection_details[2]
        self.access_token_secret = connection_details[3]
        self.api = twitter.Api(consumer_key=self.consumer_key,
                               consumer_secret=self.consumer_secret,
                               access_token_key=self.access_token_key,
                               access_token_secret=self.access_token_secret)