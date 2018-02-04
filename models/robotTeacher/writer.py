""" Only write feature """

import csv
import termcolor

from views import console
from models.robotTeacher import selecter

def WriteGradesOneOrZero(qFile, grades):
    """Write Grades to csv data"""

    # ファイル名の.csvを削除
    qFile = qFile.rstrip(".csv")

    # csvに成績を書き込む
    write_fp = csv.writer(
        open("data/grades/{qFile}Grades.csv".format(qFile=qFile), "a"))
    write_fp.writerow(grades)


def writeGradesBook(fileName, enPosts):
    """Write GradeBook"""

    # 新しく作った英単語帳の成績表を作成
    with open("data/grades/{fileName}Grades.csv"
              .format(fileName=fileName), "w") as csvFile:
        fieldNames = enPosts
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        writer.writeheader()


def writeQuestion(speakColor, name, enPosts, jpPosts):
    """Write question and answer"""

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
