"""
    connecting, parsing and sending messages on twitter
"""

class TwitterIntegration:
    """
        Methods:
            get_param
            twitter_api_details
    """

    def __init__(self, consumerKey, consumerSecret, accessTokenKey, accessTokenSecret):
        self.consumerKey = consumerKey
        self.consumerSecret = consumerSecret
        self.accessTokenKey = accessTokenKey
        self.accessTokenSecret = accessTokenSecret