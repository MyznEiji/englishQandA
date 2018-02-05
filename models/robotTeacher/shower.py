""" Only show feature """

import os

import termcolor

from models.robotTeacher import reader


def showQuestionsList():
    """ Show current files to user."""


    # dataディレクトリのファイルを全て読み込み出力
    questionsFile = os.listdir("data/questions")
    print("\n\n")
    for i, file in enumerate(questionsFile):
        print(termcolor.colored(
            "[ {i} ] {file} の問題\n".format(i=i, file=file), "blue"))
    return questionsFile


def showPreviousGrades():
    """Show previousGrades to the user."""
    print("前回の成績発表")
