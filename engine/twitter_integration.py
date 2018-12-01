"""
    connecting, parsing and sending messages on twitter
"""
import twitter
import logging
from engine.volatil_params import VolatileParams
from engine.date_formating import DateFormating
from engine.menu import Menu


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

    def get_twitter_request(self, no_of_msg=None):
        if no_of_msg == 1:
            user_timeline = self.api.GetUserTimeline(screen_name=self.users, count=no_of_msg)
        else:
            user_timeline = self.api.GetUserTimeline(screen_name=self.users,since_id=VolatileParams().get_param("lastTweetId" + self.users))
        if len(user_timeline) > 0:
            print(user_timeline[0].id)
            VolatileParams().change_param("lastTweetId" + self.users, user_timeline[0].id)

        for item in user_timeline:
            msg_text = " ".join(word for word in item.text.lower().split(" ") if not word.startswith("@"))
            for option in Menu().menu_options():
                if option in msg_text:
                    Menu().commands(option)

        return user_timeline

        # for item in user_timeline:
        #     print(item.text.lower())
        # VolatileParams().change_param("test")
        # print(VolatileParams().get_param("test"))

    def reply(self, msg, status_id=None):
        user = "@" + self.users
        answer = user + "\n" + DateFormating("%Y-%m-%d %H:%M").date_now() + "\n" + msg
        if status_id:
            self.api.PostUpdate(answer, in_reply_to_status_id=status_id)
        else:
            self.api.PostUpdate(answer)
