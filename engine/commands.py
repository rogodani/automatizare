"""
    preparing a message with the commands
"""
class Commands():
    """
        Methods:
            commands_list
    """
    @staticmethod
    def commands_list():
        """
            return:
                a message with the avaibale commands
        """
        msg = ""
        with open("commands.txt",'r') as f:
            for line in f:
                msg += line
            return msg