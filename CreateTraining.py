import pandas as pd
from numpy import mean, var, fft, diff, sign, correlate
from scipy.stats import kurtosis, skew
import csv


sport = input("sport : c/f \n")

if sport == "c":
    fileName = 'Confronto/calcio/P'
else:
    fileName = 'Confronto/futsal/P'

countP = 0
for p in range(1, 6):
    count = 0
    for pTrain in range(1, 6):
        if pTrain != p:
            data = pd.read_csv(fileName + str(p) + '/test.csv')
            if count == 0 or countP == 0:
                with open(fileName + str(p) + '/training.csv', 'w', newline='') as f:
                    data.to_csv(f, index=False)
                    if countP == 0:
                        countP = 1
            else:
                with open(fileName + str(p) + '/training.csv', 'a', newline='') as f:
                    data.to_csv(f, header=False, index=False)
        count += 1
