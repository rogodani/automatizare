"""
    class that manage the temperature logs
"""
import os


class Temperature:
    """
        Methods:
    """

    def __init__(self, outdoor_log_path):
        self.outdoor_log_path = outdoor_log_path

    def check_log_path(self, log_path):
        return os.path.isfile(log_path)