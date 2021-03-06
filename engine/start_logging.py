"""
    start the logging
"""

import logging
import os


class StartLogging:
    """
        Methods:
            start:
                launch the logging after checking is the log dir and file exist
            launch:
                launch the logging
            check_log_dir:
                check if the log dir exist
            check_log_file:
                check if log file exist
            create_log_file:
                create the log file
    """

    def __init__(self, log_dir, log_file):
        """
            Parameters:
                log_dir:
                    path to log directory
                log_file:
                    log file name
        """
        self.log_dir = os.path.expanduser(log_dir)
        self.log_file = log_file
        self.path = self.log_dir + self.log_file

    def start(self):
        """
            Launch the logging process after checking if the log dir and file exist
        """
        if not self.check_log_dir():
            os.mkdir(os.path.expanduser(self.log_dir))
            self.create_log_file()
            self.launch()
            logging.info("Creating log directory %s and log file %s" % (self.log_dir, self.log_file))
        elif not self.check_log_file():
            self.create_log_file()
            logging.info("Creating log file %s in %s" % (self.log_dir, self.log_file))
        else:
            self.launch()
            logging.info('Logging start')

    def launch(self):
        """
            Launch the logging process
        """
        logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename=self.path, level=logging.INFO)
        logging.getLogger().addHandler(logging.StreamHandler())

    def check_log_dir(self):
        """
            return:
                True if dir exist
                False if dir is missing
        """
        return os.path.isdir(self.log_dir)

    def check_log_file(self):
        """
            return:
                True if file exist
                False if file is missing
        """
        return os.path.isfile(self.path)

    def create_log_file(self):
        """
            Creating the log file
        """
        open(self.path, 'a').close()
