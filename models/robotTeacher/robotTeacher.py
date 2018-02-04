""" Defined a robotTeacher model"""


import os
import csv

import termcolor

from views import console
from models import robot
from models.robotTeacher import shower
from models.robotTeacher import selecter
from models.robotTeacher import reader
from models.robotTeacher import writer
import data


class RobotTeacher(robot.Robot):
    """Handle data model on Teacher."""

    newLine = "\n\n"
    line = "-" * 60


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
        print("前回の成績発表")

    @_helloDecorator
    def createQuestions(self):
        """Create new questions"""

        enPosts = []
        jpPosts = []

        writer.writeQuestion(
            self.speakColor,
            self.name,
            enPosts,
            jpPosts)

    @_helloDecorator
    def englishQuestionsStart(self):
        """Start english questions."""

        trueAnswers = {}
        falseAnswers = {}
        grades = []
        questionListPosts = []

        # 問題のリストを出力
        questionListPosts = shower.showQuestionsList(questionListPosts)

        # 問題の選択待ち
        selectedQuestionNum = selecter.selectedQuestions(
            self.speakColor,
            self.name,
            self.userName,
            questionListPosts)

        # 選択した問題を代入
        qFile = str(questionListPosts[selectedQuestionNum])

        # 選択した問題を出力
        reader.readQuestions(
            self.speakColor,
            self.name, qFile,
            trueAnswers,
            falseAnswers,
            grades)

        # 成績を書き込み
        writer.WriteGradesOneOrZero(qFile, grades)

    @_helloDecorator
    def thankYou(self):
        """Show words of appreciation to users. """

        template = console.getTemplate(
            "goodBy.txt", self.speakColor)

        print(template.substitute({
            "robotName": self.name,
            "userName": self.userName,
        }))

        exit()