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
from models.robotTeacher import graphView
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
    def menu(self):

        # メニューの表示,選択
        menuAnswer = selecter.selectedMenu(
            self.speakColor,
            self.name,
            self.userName)
        # 選択したメニューを実行

        if menuAnswer == 0:
            return self.createQuestions()
        elif menuAnswer == 1:
            return self.plactice()
        elif menuAnswer == 2:
            return self.englishTest()
        elif menuAnswer == 3:
            # 成績を表示するメソッド
            return self.gradesShow()
            グラフ表示ファイル
            showファイルで呼び出し表示する

    @_helloDecorator
    def gradesShow(self):
        """ show grades to user """
        """
            成績を見たいものを表示
            選択
            グラフ表示
        """
        # 問題を表示
        questionListPosts = shower.showQuestionsList()

        # 問題の選択待ち
        selectedQuestionNum = selecter.selectedQuestions(
            self.speakColor,
            self.name,
            questionListPosts)

        # 選択した問題
        qFile = questionListPosts[selectedQuestionNum]

        # グラフを表示する
        graphView.gradesGraphView(qFile)

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
    def englishTest(self):
        """Start english questions."""

        trueAnswers = {}
        falseAnswers = {}
        grades = []
        questionListPosts = []

        # 前回の成績発表
        shower.showPreviousGrades()

        # 問題のリストを出力
        questionListPosts = shower.showQuestionsList()

        # 問題の選択待ち
        selectedQuestionNum = selecter.selectedQuestions(
            self.speakColor,
            self.name,
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
        correctAnswerRate = writer.WriteGradesOneOrZero(
            qFile,
            grades,
            falseAnswers)

        # 成績発表
        template = console.getTemplate(
            "resultAnnounce.txt", self.speakColor)

        print(template.substitute({
            "trueNum": len(trueAnswers),
            "allNum": len(trueAnswers) + len(falseAnswers),
            "correctAnswerRate": correctAnswerRate,
            "trueAnswers": trueAnswers,
            "falseAnswers": falseAnswers,
            "robotName": self.name
        }))

    @_helloDecorator
    def plactice(self):
        """English words plactice"""
        print("英単語の練習")

    @_helloDecorator
    def thankYou(self):
        """Show words of appreciation to users. """

        template = console.getTemplate(
            "goodBy.txt", self.speakColor)

        print(template.substitute({
            "robotName": self.name,
            "userName": self.userName,
        }))
