"""
    connecting, parsing and sending messages on twitter
"""
import twitter
from engine.volatil_params import VolatileParams
from engine.date_formating import DateFormating
import logging


class TwitterIntegration:
    """
        Methods:
            get_twitter_request:
                get the user timeline
            reply:
                reply to twitter messages
    """

    def __init__(self, connection_details, users):
        self.consumer_key = connection_details[0]
        self.consumer_secret = connection_details[1]
        self.access_token_key = connection_details[2]
        self.access_token_secret = connection_details[3]
        self.api = twitter.Api(consumer_key=self.consumer_key,
                               consumer_secret=self.consumer_secret,
                               access_token_key=self.access_token_key,
                               access_token_secret=self.access_token_secret)
        self.users = users
        logging.info("Twitter API initialized")

    def get_twitter_request(self, reboot=False):
        # TODO: should be update to have diffrent outputs when the system reboots
        # TODO: shoul be update to work with multiple messages
        user_timeline = self.api.GetUserTimeline(screen_name="DRogozan", count=1)
        print(user_timeline)
        VolatileParams().change_param("test")
        print(VolatileParams().get_param("test"))

    def reply(self, msg, status_id=None):
        user = "@" + self.users
        answer = user + "\n" + DateFormating("%Y-%m-%d %H:%M").date_now() + "\n" + msg
        if status_id:
            self.api.PostUpdate(answer, in_reply_to_status_id=status_id)
        else:
            self.api.PostUpdate(answer)
