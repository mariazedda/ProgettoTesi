import pandas as pd
from numpy import mean, var, fft, diff, sign, correlate
from scipy.stats import kurtosis, skew
import csv

sport = input("sport : c/f \n")

if sport == "c":
    fileName = 'DividedTestTrainingFile/calcio/P'
    pathFileName = 'AverageDivideTesterTrainingFile/calcio/P'
    path = 'calcio'
else:
    fileName = 'DividedTestTrainingFile/futsal/P'
    pathFileName = 'AverageDivideTesterTrainingFile/futsal/P'
    path = 'futsal'

for p in range(1, 6):
    dataTestTime = pd.read_csv(fileName + str(p) + '/test.csv')
    #dataTest2 = pd.read_csv(fileName + str(p) + '/test2.csv')
    dataTrainingTime = pd.read_csv(fileName + str(p) + '/training.csv')
    shapeTestTime = dataTestTime.shape
    minutesTest = int((shapeTestTime[0]) / 60)
    secondsTest = shapeTestTime[0] - minutesTest * 60

    shapeTrainingTime = dataTrainingTime.shape

    minutesTraining = int((shapeTrainingTime[0]) / 60)
    secondTraining = shapeTrainingTime[0] - minutesTraining * 60
    dataTest = pd.read_csv(pathFileName + str(p) + '/test.csv')
    #dataTest2 = pd.read_csv(fileName + str(p) + '/test2.csv')
    dataTraining = pd.read_csv(pathFileName + str(p) + '/training.csv')


    """for s in range(1, 3):
        if s == 1:
            rowTest = rowTest1
            colTest = colTest1
            dataTest = dataTest1
            lastTest = lastTest1
        else:
            rowTest = rowTest2
            colTest = colTest2
            dataTest = dataTest2
            lastTest = lastTest2"""

    # with open('AverageDivideTesterTrainingFile/' + path + '/P' + str(p) + '/test' + str(s) + '.csv', 'w') as fTest:
    with open('AverageDivideTesterTrainingFile/' + path + '/P' + str(p) + '/test' + '.csv', 'w',
              newline='') as fTest:
        wtr = csv.writer(fTest)
        newColumn = dataTest.columns
        newColumn.append("TotalTime")
        wtr.writerow(newColumn)
        for n in range(0, rowTest):
            for col in range(0, colTest):
                for row in range(0, 60):
                    averageRow.append(dataTest.iloc[row, col])

                newRow.append(mean(averageRow))
                averageRow = []

            dataTest = dataTest.drop(dataTest.index[:60])
            wtr.writerow(newRow)
            newRow = []
            if n == rowTest - 1:
                for col in range(0, colTest):
                    for row in range(0, lastTest):
                        averageRow.append(dataTest.iloc[row, col])

                    newRow.append(mean(averageRow))
                    averageRow = []
                wtr.writerow(newRow)
                newRow = []

    with open('AverageDivideTesterTrainingFile/' + path + '/P' + str(p) + '/training.csv', 'w',
              newline='') as fTraining:
        wtr = csv.writer(fTraining)
        wtr.writerow(dataTraining.columns)
        for n in range(0, rowTraining):
            for col in range(0, colTraining):
                for row in range(0, 60):
                    averageRow.append(dataTraining.iloc[row, col])

                newRow.append(mean(averageRow))
                averageRow = []

            dataTraining = dataTraining.drop(dataTraining.index[:60])
            wtr.writerow(newRow)
            newRow = []
            if n == rowTraining - 1:
                for col in range(0, colTraining):
                    for row in range(0, lastTraining):
                        averageRow.append(dataTraining.iloc[row, col])

                    newRow.append(mean(averageRow))
                    averageRow = []

                wtr.writerow(newRow)
                newRow = []