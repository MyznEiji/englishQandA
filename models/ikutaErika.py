""" Defined a Ikuta Erika model """

from views import console


defaultName = "生田絵梨花"


class IkutaErika(object):
    """Base model for Ikuta Erika"""

    def __init__(self, name=defaultName, userName="",
                 speakColor="green"):
        self.name = name
        self.userName = userName
        self.speakColor = speakColor

    def hello(self):
        """Returns words to the user that the Ikuta Erika speaks at the beginning."""

        while True:
            template = console.getTemplate("hello.txt", self.speakColor)
            userName = input(template.substitute({
                "personName": self.name}))

            if userName:
                self.userName = userName.title()
                break

class IkutaErikaTeacher(IkutaErika):
    """Handle data model on Teacher."""

    def __init__(self, name=defaultName):
        super().__init__(name=name)
