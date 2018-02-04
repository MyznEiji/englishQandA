"""Only select feature"""

import termcolor

from views import console
from models.robotTeacher import shower


def selectedQuestions(speakColor, name, userName, questionListPosts):
    """Select question list """

    template = console.getTemplate(
        "questionListSelect.txt", speakColor)

    while True:

        selectedQuestion = input(template.substitute({
            "robotName": name,
            "userName": userName,
        }))

        if not selectedQuestion.isdigit():
            print(termcolor.colored("数字で選択してください", "red"))
            continue
        if int(selectedQuestion) > len(questionListPosts) - 1:
            print(termcolor.colored("数字を正確に入力してください", "red"))
            continue

        # 選択した番号を代入
        selectedQuestion = int(selectedQuestion)
        break

    return selectedQuestion
