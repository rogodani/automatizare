"""
    Format date
"""
from datetime import datetime


class DateFormating:
    """
        Methods:
            date_now
    """
    def __init__(self, date_format):
        self.date_format = date_format

    def date_now(self):
        """
            return:
                the actual date in date_format format
        """
        return datetime.now().strftime(self.date_format)