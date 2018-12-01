"""
    class that manage the temperature logs
"""
import os
import logging
from datetime import datetime
from engine.date_formating import DateFormating


class Temperature:
    """
        Methods:
            check_log_path:
                check if the log file exist
            missing_logs:
                check if temperature logging is working
    """

    def __init__(self, log_path):
        self.log_path = os.path.expanduser(log_path)
        logging.info("Temperature log path: %s" % (self.log_path))

    def check_log_path(self):
        """
            return:
                True if log file exist
                False if the log file is missing
        """
        return os.path.isfile(self.log_path)

    def missing_logs(self):
        """
            return:
                a message if the last temperature log is older then 30 min
                or OK if logging is fine
        """
        temp_log = self.get_last_temp_log()
        time_format = "%b %d %H:%M:%S"
        datetime_from_log = datetime.strptime(temp_log[:temp_log.rindex(" ")], time_format)
        current_time = datetime.strptime(DateFormating(time_format).date_now(), time_format)
        time_delta_in_minutes = (current_time - datetime_from_log).total_seconds() / 60
        if time_delta_in_minutes > 30:
            msg = "\n--- CHECK THE SENSOR ---\n--- LAST LOG: %d MINUTES AGO ---" \
                  % (time_delta_in_minutes)
            logging.info(msg)
            return msg
        return "OK"

    def get_last_temp_log(self):
        """
            return:
                last temperature log
        """
        with open(self.log_path, "r") as file:
            return file.readlines()[-1]
