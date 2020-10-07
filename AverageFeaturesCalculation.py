import pandas as pd
from numpy import mean, var, fft, diff, sign, correlate
from scipy.stats import kurtosis, skew
import csv

sport = input("sport : c/f \n")

if sport == "c":
    fileName = 'MeanFeatures/calcio/P'
    path = 'calcio'
else:
    fileName = 'MeanFeatures/futsal/P'
    path = 'futsal'

for p in range(1, 6):

    """dataTest1 = pd.read_csv(fileName + str(p) + '/test1.csv')
    
    dataTest2 = pd.read_csv(fileName + str(p) + '/test2.csv')"""
    dataTest = pd.read_csv(fileName + str(p) + '/test.csv')
    dataTraining = pd.read_csv(fileName + str(p) + '/training.csv')
    shapeTest = dataTest.shape
    # shapeTest2 = dataTest2.shape
    rowTest = int((shapeTest[0]) / 60)
    # rowTest2 = int((shapeTest2[0]) / 60)
    lastTest = shapeTest[0] - rowTest * 60
    # lastTest2 = shapeTest2[0] - rowTest2 * 60
    colTest = shapeTest[1]
    
    shapeTraining = dataTraining.shape

    rowTraining = int((shapeTraining[0]) / 60)
    lastTraining = shapeTraining[0] - rowTraining * 60

    colTraining = shapeTraining[1]
    averageRow = []
    newRow = []
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
    with open('TimedFeatures/' + path + '/P' + str(p) + '/test.csv', 'w',
              newline='') as fTest:
        wtr = csv.writer(fTest)
        wtr.writerow(dataTest.columns)
        for n in range(0, rowTest):
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

    with open('TimedFeatures/' + path + '/P' + str(p) + '/training.csv', 'w', newline='') as fTraining:
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
            if n == rowTraining-1:
                for col in range(0, colTraining):
                    for row in range(0, lastTraining):
                        averageRow.append(dataTraining.iloc[row, col])

                    newRow.append(mean(averageRow))
                    averageRow = []

                wtr.writerow(newRow)
                newRow = []
