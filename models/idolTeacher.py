""" Defined a idolTeacher model"""

import os
import csv

import termcolor

from views import console
from models import idol
import data


class IdolTeacher(idol.Idol):
    """Handle data model on Teacher."""

    newLine = "\n\n"
    line = "-" * 60
    questionListPosts = []

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

        # dataディレクトリのファイルを全て読み込み出力
        questionsFile = os.listdir("data")
        print(self.newLine)
        for i, file in enumerate(questionsFile):
            if not file in self.questionListPosts:
                self.questionListPosts.append(file)
            print("[", i, "]", file, "の問題\n")

    @_helloDecorator
    def chooseQuestions(self):
        """Collect user's answer from user. """

        template = console.getTemplate(
            "questionListSelect.txt", self.speakColor)

        while True:
            selectedQuestion = input(template.substitute({
                "idolName": self.name,
                "userName": self.userName,
            }))
            if selectedQuestion.isdigit():
                selectedQuestion = int(selectedQuestion)
                break
            self.showQuestionsList()
            print(termcolor.colored("数字で選択してください", "red"))

        return selectedQuestion

    @_helloDecorator
    def englishQuestionsStart(self):
        """Start english questions."""
        selectedQuestionNum = self.chooseQuestions()
        qFile = str(self.questionListPosts[selectedQuestionNum])

        # 選択したcsvの問題を出題する
        with open("data/{qFile}".format(qFile=qFile), "r") as csvFile:
            reader = csv.DictReader(csvFile)

            for i, row in enumerate(reader):
                template = console.getTemplate("question.txt", self.speakColor)
                print(template.substitute({"qNum": i + 1, "en": row["En"]}))

                answer = input()

                # 答えの正誤判定
                if answer == row["Jp"]:
                    template = console.getTemplate(
                        "trueComment.txt", self.speakColor, "on_blue")
                    print(template.substitute())
                else:
                    template = console.getTemplate(
                        "falseComment.txt", self.speakColor, "on_red")
                    print(template.substitute({"jp": row["Jp"]}))

    def writeQuestion(self):
        """Write question and answer"""

        template = console.getTemplate(
            "newFileName.txt", self.speakColor)
        fileName = input(template.substitute())
        with open("data/{fileName}.csv".format(fileName=fileName), "w") as csvFile:
            fieldNames = ["En", "Jp"]
            writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
            writer.writeheader()

            while True:
                template = console.getTemplate(
                    "enWord.txt", self.speakColor)
                enWord = input(template.substitute())

                template = console.getTemplate(
                    "jpWord.txt", self.speakColor)
                jpWord = input(template.substitute())
                writer.writerow({"En": enWord, "Jp": jpWord})

                template = console.getTemplate(
                    "continueToWrite.txt", "blue")
                while True:
                    yOrN = input(template.substitute())
                    if yOrN == "y":
                        break
                    elif yOrN == "n":
                        exit()
                    else:
                        print(termcolor.colored("入力値が正しくありません", "red"))
