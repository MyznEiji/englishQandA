""" Defined a idol model """

from views import console


class Idol(object):
    """Base model for Idol"""

    def __init__(self, name="", userName="",
                 speakColor="green"):
        self.name = name
        self.userName = userName
        self.speakColor = speakColor

    def hello(self):
        """Returns words to the user that the Ikuta Erika speaks at the beginning."""

        while True:
            template = console.getTemplate("hello.txt", self.speakColor)
            userName = input(template.substitute({
                "idolName": self.name}))

            if userName:
                self.userName = userName.title()
                break
