import csv
import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

from data import grades


def lineGraph(qFile):
    """ Show Line Graph to user """

    currectAnswerRate = qFile["correctAnswerRate"]
    # 正解率と間違った単語の列を削除
    del qFile["correctAnswerRate"]
    del qFile["wrongWord"]

    # testDate(日付)をday1~n に変換
    testDate = np.array(qFile["testDate"])
    dayCount = []
    for i in range(len(testDate)):
        day = str(i + 1) + "times"
        dayCount.append(day)

    # 日付の列を削除
    del qFile["testDate"]

    # できた単語の数を計算
    currectWordSumList = []
    qFile = np.array(qFile)
    for i in range(qFile.shape[0]):
        sum = 0
        for j in range(qFile.shape[1]):
            # 1行づつvalueをまとめる
            sum += qFile[i, j]
        currectWordSumList.append(sum)

    # y軸にできた単語数
    y = currectAnswerRate
    # x軸にテスト行った回数
    X = dayCount

    # なん
    for day, cWord, in zip(dayCount, currectWordSumList):
        print("\n{line}".format(line="-" * 60))
        print("\n\n{day} - {cWord}問正解 / {allWord}問中\n"
              .format(day=day, cWord=cWord, allWord=qFile.shape[1]))

    # 折れ線グラフをplot
    plt.plot(X, y)
    plt.xlabel("Day")
    plt.ylabel("Currect Answer Rate")
    plt.ylim(0, 105)
    plt.title("Correct Words Line Graph")
    plt.grid(True)
    plt.show()


def barGraph(qFile):
    """ Show bar graph to user """
    y = qFile.sum()
    x = qFile.columns

    plt.bar(x, y)
    plt.xlabel("Words")
    plt.ylabel("Currect words / All words")
    plt.title("Currect Words Bar Graph (all={sum})".format(sum=qFile.shape[0]))
    plt.ylim(0, qFile.shape[0] + 1)
    plt.grid(True)
    plt.show()


def gradesGraphView(qFile):
    """ Show bar graph and line graph to user"""

    # qFileをDataFrameに変換
    os.chdir("/Users/miyazonoeiji/projects/python/englishQandA/data/grades")
    qFile = qFile.rstrip(".csv") + "Grades.csv"
    qFile = pd.read_csv(qFile)

    # 折れ線グラフを表示
    lineGraph(qFile)

    # 棒グラフを表示
    barGraph(qFile)
