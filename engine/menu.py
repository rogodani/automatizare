"""
    preparing a message with the commands
"""


class Menu():
    """
        Methods:
            commands_list
    """

    @staticmethod
    def menu_list():
        """
            return:
                a message with the avaibale commands
        """
        msg = ""
        with open("menu.txt", 'r') as file:
            for line in file:
                msg += line
            return msg
