import pandas as pd
from numpy import mean, var, fft, diff, sign, correlate
from scipy.stats import kurtosis, skew
import csv

sport = input("sport : c/f \n")

if sport == "c":
    fileName = 'TesterTrainingFile/calcio/P'
    path = 'calcio'
else:
    fileName = 'TesterTrainingFile/futsal/P'
    path = 'futsal'

for p in range(1, 6):
    dataTest = pd.read_csv(fileName + str(p) + '/test.csv')
    dataTraining = pd.read_csv(fileName + str(p) + '/training.csv')
    shapeTest = dataTest.shape
    rowTest = int((shapeTest[0]) / 60)
    lastTest = shapeTest[0] - rowTest
    colTest = shapeTest[1]
    
    shapeTraining = dataTraining.shape
    rowTraining = int((shapeTraining[0]) / 60)
    lastTraining = shapeTraining[0] - rowTraining
    colTraining = shapeTraining[1]
    averageRow = []
    newRow = []
    with open('AverageTesterTrainingFile/' + path + '/P' + str(p) + '/test.csv', 'w') as fTest:
        wtr = csv.writer(fTest)
        wtr.writerow(dataTest.columns)
        for n in range(0, rowTest-1):
            for col in range(0, colTest):
                for row in range(0, 60):
                    averageRow.append(dataTest.iloc[row, col])

                newRow.append(mean(averageRow))
                averageRow = []

            dataTest = dataTest.drop(dataTest.index[:60])
            wtr.writerow(newRow)
            newRow = []

            if n == rowTest-1:
                for col in range(0, colTest):
                    for row in range(0, lastTest):
                        averageRow.append(dataTest.iloc[row, col])

                    newRow.append(mean(averageRow))
                    averageRow = []
                wtr.writerow(newRow)
                newRow = []

    with open('AverageTesterTrainingFile/' + path + '/P' + str(p) + '/training.csv', 'w') as fTraining:
        wtr = csv.writer(fTraining)
        wtr.writerow(dataTraining.columns)
        for n in range(0, rowTraining-1):
            for col in range(0, colTraining):
                for row in range(0, 60):
                    averageRow.append(dataTraining.iloc[row, col])

                newRow.append(mean(averageRow))
                averageRow = []

            dataTraining = dataTraining.drop(dataTraining.index[:60])
            wtr.writerow(newRow)
            newRow = []
            if n == rowTraining:
                for col in range(0, colTraining):
                    for row in range(0, lastTraining):
                        averageRow.append(dataTraining.iloc[row, col])

                    newRow.append(mean(averageRow))
                    averageRow = []
                wtr.writerow(newRow)
                newRow = []
