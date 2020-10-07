import pandas as pd
from numpy import mean, var, fft, diff, sign, correlate
from scipy.stats import kurtosis, skew
import csv

stringSens = "dQ dV Mag Quat FreeAcc".split()
stringAx = "w x y z".split()
stringAxi = "x y z".split()
stringFeature = "max min avg var skew kurt aut pks fpk".split()

clm = []

sport = input("sport : c/f \n")
quality = input("score : y/n \n")
time = input("total time : y/n \n")

if time == "y":
    clm.append("Time")

if quality == "y":
    clm.append("Score")

# Calcolo delle feature e scrittura sul file
if sport == "c":
    stringPath = "data2/calcio"
    fileName = 'TimeFeatures/calcio/'
    path = '/Exercise'
else:
    stringPath = "data2/futsal"
    fileName = 'TimeFeatures/futsal/'
    path = '/Exercise'

count = 0
for p in range(1, 6):
    for s in range(1, 2):
        #if p == 4:
         #   s = 1
        with open(fileName + 'P' + str(p) + path + str(s) + '.csv', 'w', newline='') as f:
            wtr = csv.writer(f)
            wtr.writerow(clm)

            auxStr = ""
            if s < 10:
                auxStr = "0"
                auxStr += str(s)
                stringPathFile = stringPath + "/p" + str(p) + "/s" + auxStr + ".txt"

                data = pd.read_csv(stringPathFile, sep="\t", header=None, index_col=False)
                for X in pd.read_csv(stringPathFile, sep="\t", header=None, chunksize=60, index_col=False,
                                     low_memory=False):
                    row = []

                    if time == "y":
                        dataRow = data.shape[0]
                        last = int(data.iloc[dataRow-1, 1])
                        first = int(data.iloc[0, 1])
                        total = (last - first) / 1000000
                        minutes = int(total / 60)
                        seconds = int(total - minutes * 60)
                        row.extend(([minutes + seconds / 100]))
                    if quality == "y":
                        row.extend([max(X[X.shape[1] - 2])])  # Score

                    if len(clm) == len(row):
                        wtr.writerow(row)
