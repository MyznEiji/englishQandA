""" Defined a idolTeacher model"""

import os

from views import console
from models import idol
import data


class IdolTeacher(idol.Idol):
    """Handle data model on Teacher."""

    def __init__(self, name=""):
        super().__init__(name=name, userName="")

    def _helloDecorator(func):
        """Decorator to say a greeting if you are not greeting the user."""

        def wrapper(self):
            if not self.userName:
                self.hello()
            return func(self)
        return wrapper

    @_helloDecorator
    def previousGrades(self):
        """Show previousGrades to the user."""

    @_helloDecorator
    def showQuestionsList(self):
        """ Show current files to user."""
        questionsFile = os.listdir("data")
        for i, file in enumerate(questionsFile):
            print("[", i, "]", file, "の問題")

    @_helloDecorator
    def chooseQuestions(self):
        """Collect user's answer from user. """

        while True:
            template = console.getTemplate("question.txt", self.speakColor)
            selectedQuestion = input(template.substitute({
                "idolName": self.name,
                "userName": self.userName,
            }))
            if selectedQuestion:
                break

        return selectedQuestion

    @_helloDecorator
    def englishQuestionsStart(self):
        """Start english questions."""

        while True:
            if self.chooseQuestions().isdigit():
                break
            self.showQuestionsList()
            print("数字を入力してください")
            # selectedQuestion = int(self.chooseQuestions())
