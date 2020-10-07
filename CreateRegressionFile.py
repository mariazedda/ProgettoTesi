import pandas as pd
from numpy import mean, var, fft, diff, sign, correlate
from scipy.stats import kurtosis, skew
import csv


sport = input("sport : c/f \n")

if sport == "c":
    fileName = 'Features/calcio/P'
    path = 'calcio'
else:
    fileName = 'Features/futsal/P'
    path = 'futsal'

countP = 0
for p in range(1, 6):
    if p != 4:
        count = 0
        for pTrain in range(1, 6):
            if pTrain == p:
                for s in range(1, 3):
                    data = pd.read_csv(fileName + str(p) + '/Exercise' + str(s) + '.csv')
                    data.to_csv('TestTrainingFile/' + path + '/P' + str(p) + '/test' + str(s) + '.csv',
                                index=False)
            else:
                if pTrain != 4:
                    for s in range(1, 3):
                        data = pd.read_csv(fileName + str(pTrain) + '/Exercise' + str(s) + '.csv')
                        if count == 0 or countP == 0:
                            with open('TestTrainingFile/' + path + '/P' + str(p) + '/training.csv', 'w', newline='') as f:
                                data.to_csv(f, index=False)
                                if countP == 0:
                                    countP = 1
                        else:
                            with open('TestTrainingFile/' + path + '/P' + str(p) + '/training.csv', 'a', newline='') as f:
                                data.to_csv(f, header=False, index=False)

                        count += 1
                else:
                    data = pd.read_csv(fileName + str(pTrain) + '/Exercise1' + ".csv")
                    if count == 0 or countP == 0:
                        with open('TestTrainingFile/' + path + '/P' + str(p) + '/training.csv', 'w',
                                  newline='') as f:
                            data.to_csv(f, index=False)
                            if countP == 0:
                                countP = 1
                    else:
                        with open('TestTrainingFile/' + path + '/P' + str(p) + '/training.csv', 'a',
                                  newline='') as f:
                            data.to_csv(f, header=False, index=False)
                    count += 1
    else:
        count = 0
        for pTrain in range(1, 6):
            if pTrain == p:
                data = pd.read_csv(fileName + str(p) + '/Exercise1' + ".csv")
                data.to_csv('TestTrainingFile/' + path + '/P' + str(p) + '/test' + '.csv', index=False)
            else:
                data = pd.read_csv(fileName + str(pTrain) + '/Exercise1' + ".csv")
                if count == 0 or countP == 0:
                    with open('TestTrainingFile/' + path + '/P' + str(p) + '/training.csv', 'w',
                              newline='') as f:
                        data.to_csv(f, index=False)
                        if countP == 0:
                            countP = 1
                else:
                    with open('TestTrainingFile/' + path + '/P' + str(p) + '/training.csv', 'a',
                              newline='') as f:
                        data.to_csv(f, header=False, index=False)
            count += 1
