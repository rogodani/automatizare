"""
    class that manage the temperature logs
"""
import os
from datetime import datetime
from engine.date_formating import DateFormating


class Temperature:
    """
        Methods:
    """

    def __init__(self, log_path):
        self.log_path = os.path.expanduser(log_path)

    def check_log_path(self):
        print(self.log_path)
        return os.path.isfile(self.log_path)

    def missing_logs(self):
        temp_log = self.last_temp_log()
        time_format = "%b %d %H:%M:%S"
        datetime_from_log = datetime.strptime(temp_log[:temp_log.rindex(" ")], time_format)
        current_time = datetime.strptime(DateFormating(time_format).date_now(), time_format)
        time_delta_in_minutes = (current_time - datetime_from_log).total_seconds() / 60
        if (time_delta_in_minutes > 30):
            pass
            # TODO
            # uncommet de following line after the reply is available
            # reply("\n--- CHECK THE SENSOR ---\n--- LAST LOG: %d MINUTES AGO ---" % (time_delta_in_minutes))

    def last_temp_log(self):
        with open(self.log_path, "r") as file:
            return file.readlines()[-1]
