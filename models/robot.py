""" Defined a robot model """

from views import console


class Robot(object):
    """Base model for robot"""

    def __init__(self, name="", userName="",
                 speakColor="yellow"):
        self.name = name
        self.userName = userName
        self.speakColor = speakColor

    def hello(self):
        """Returns words to the user that the robot speaks at the beginning."""

        while True:
            template = console.getTemplate("hello.txt", self.speakColor)
            userName = input(template.substitute({
                "robotName": self.name}))

            if userName:
                self.userName = userName.title()
                break
