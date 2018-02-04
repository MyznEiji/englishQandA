""" Only Reader feature """

import csv

from views import console


def readQuestions(speakColor, name, qFile, trueAnswers, falseAnswers, grades):
    # 選択したcsvの問題を出題する
    with open("data/questions/{qFile}".format(qFile=qFile),
              "r") as csvFile:

        reader = csv.DictReader(csvFile)

        for i, row in enumerate(reader):
            template = console.getTemplate("question.txt", speakColor)
            print(template.substitute({
                "qNum": i + 1,
                "en": row["En"]
            }))

            answer = input()

            # 答えの正誤判定
            if answer == row["Jp"]:
                template = console.getTemplate(
                    "trueComment.txt", speakColor, "on_blue")
                print(template.substitute({"robotName": name}))
                trueAnswers[row["En"]] = row["Jp"]
                grades.append(1)

            else:
                template = console.getTemplate(
                    "falseComment.txt", speakColor, "on_red")
                print(template.substitute({
                    "robotName": name,
                    "jp": row["Jp"]
                }))
                falseAnswers[row["En"]] = row["Jp"]
                grades.append(0)
