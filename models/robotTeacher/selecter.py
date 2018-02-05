"""Only select feature"""

import termcolor

from views import console
from models.robotTeacher import shower


def selectedQuestions(speakColor, name, questionListPosts):
    """Select question list """

    template = console.getTemplate(
        "questionListSelect.txt", speakColor)

    while True:

        selectedQuestion = input(template.substitute({
            "robotName": name,
        }))

        if not selectedQuestion.isdigit():
            print(termcolor.colored("整数で選択してください", "red"))
            continue
        if int(selectedQuestion) > len(questionListPosts) - 1:
            print(termcolor.colored("数字を正確に入力してください", "red"))
            continue

        # 選択した番号を代入
        selectedQuestion = int(selectedQuestion)
        break

    return selectedQuestion


def selectedYesOrNo(name, template):

    while True:
        yOrN = input(template.substitute(
            {"robotName": name}))

        if yOrN == "y" or yOrN == "n":
            break
        print(termcolor.colored("入力値が正しくありません", "red"))
    return yOrN


def selectedMenu(speakColor, name, userName):
    """Selected Menu """

    template = console.getTemplate(
        "showMenu.txt", speakColor)

    while True:

        menuAnswer = input(template.substitute({
            "robotName": name,
            "userName": userName,
        }))

        if not menuAnswer.isdigit():
            print(termcolor.colored("整数で選択してください", "red"))
            continue
        menuAnswer = int(menuAnswer)

        if 0 <= menuAnswer and menuAnswer < 4:
            break
        print(termcolor.colored("入力値が正しくありません", "red"))
    return menuAnswer
