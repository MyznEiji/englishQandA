""" Only write feature """

import csv
import termcolor
from datetime import datetime

from views import console
from models.robotTeacher import selecter
from models.robotTeacher import shower


def WriteGradesOneOrZero(qFile, grades, falseAnswers):
    """Write Grades to csv data"""

    # ファイル名の.csvを削除
    qFile = qFile.rstrip(".csv")

    # 正答率をgradesに追加
    allNum = len(grades)
    trueNum = allNum - len(falseAnswers)
    correctAnswerRate = round(trueNum / allNum * 100, 2)
    grades.append(correctAnswerRate)

    # 間違えた単語をgradesに追加
    grades.append(falseAnswers)

    # テストした日にちを追加
    now = datetime.now().strftime("%d/%m /%Y - %H:%M")
    grades.append(now)

    # csvに成績を書き込む
    write_fp = csv.writer(
        open("data/grades/{qFile}Grades.csv".format(qFile=qFile), "a"))
    write_fp.writerow(grades)

    return correctAnswerRate


def writeGradesBook(fileName, enPosts):
    """Write GradeBook"""

    # 新しく作った英単語帳の成績表を作成
    with open("data/grades/{fileName}Grades.csv"
              .format(fileName=fileName), "w") as csvFile:
        fieldNames = enPosts
        fieldNames.append("correctAnswerRate")
        fieldNames.append("wrongWord")
        fieldNames.append("testDate")
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        writer.writeheader()


def writeQuestion(speakColor, name, enPosts, jpPosts):
    """Write question and answer"""

    currentFile = shower.showQuestionsList()

    template = console.getTemplate(
        "newFileName.txt", speakColor)
    fileName = input(template.substitute({"robotName": name}))

    # 新しい英単語帳を作成
    with open("data/questions/{fileName}.csv".format(fileName=fileName),
              "w") as csvFile:
        fieldNames = ["En", "Jp"]
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        writer.writeheader()

        # 英単語の書き込みの繰り返し
        while True:
            # 英単語を登録
            template = console.getTemplate(
                "enWord.txt", speakColor)
            enWord = input(template.substitute(
                {"robotName": name}))
            enPosts.append(enWord)

            # 英語の意味を登録
            template = console.getTemplate(
                "jpWord.txt", speakColor)
            jpWord = input(template.substitute(
                {"robotName": name}))
            jpPosts.append(jpWord)

            # csvのファイルに書き込む
            writer.writerow({"En": enWord, "Jp": jpWord})

            # まだ英単語を書き込むかYes or No
            template = console.getTemplate(
                "continueToWrite.txt", "blue")
            yOrN = selecter.selectedYesOrNo(name, template)
            if not yOrN == "y":
                break

    # 今回作った英単語帳の成績表のベース
    writeGradesBook(fileName, enPosts)
