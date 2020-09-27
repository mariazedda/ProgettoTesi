import pandas as pd
from numpy import mean, var, fft, diff, sign, correlate
from scipy.stats import kurtosis, skew
import csv


sport = input("sport : c/f \n")

if sport == "c":
    fileName = 'featuresCalcioNormalizedP'
    path = 'calcio'
else:
    fileName = 'featuresFutsalNormalizedP'
    path = 'futsal'

countP = 0
for p in range(1, 6):
    count = 0
    for pTrain in range(1, 6):
        if pTrain == p:
            data = pd.read_csv(fileName + str(p) + ".csv")
            data.to_csv('TesterTrainingFile/' + path + '/P' + str(p) + '/test.csv', index=False)
        else:
            data = pd.read_csv(fileName + str(pTrain) + ".csv")
            if count == 0 or countP == 0:
                with open('TesterTrainingFile/' + path + '/P' + str(p) + '/training.csv', 'w', newline='') as f:
                    data.to_csv(f, header=True, index=False)
                    if countP == 0:
                        countP = 1
            else:
                with open('TesterTrainingFile/' + path + '/P' + str(p) + '/training.csv', 'a') as f:
                    data.to_csv(f, header=False, index=False)
        count += 1
