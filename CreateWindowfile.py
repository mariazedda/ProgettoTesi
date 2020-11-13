import pandas as pd
from numpy import mean, var, fft, diff, sign, correlate
from scipy.stats import kurtosis, skew
import csv
import warnings
from sklearn.metrics import precision_recall_fscore_support

warnings.filterwarnings('ignore')

sport = input("sport : c/f \n")

if sport == "c":
    fileName = 'Confronto/calcio/P'
else:
    fileName = 'Confronto/futsal/P'

for p in range(1, 6):
    setD = pd.read_csv(fileName + str(p) + '/window.csv')
    data = setD.Predizioni
    shapeData = data.shape
    row = int((shapeData[0]) - 2)
    setD.iloc[0, 1] = ''
    # setD.iloc[1, 1] = ''
    n = 1
    for w in range(0, row):
        window = []
        contatore = []
        window.extend(data.iloc[:3])
        metri = window.count("1000 metri")
        if metri > 1:
            setD.iloc[n, 1] = '1000 metri'
        # contatore.append(metri)
        navetta = window.count("Navetta 5x10")
        if navetta > 1:
            setD.iloc[n, 1] = 'Navetta 5x10'
        # contatore.append(navetta)
        scatto = window.count("Scatto 10m")
        if scatto > 1 or (scatto == 2 and metri == 1 and navetta == 1):
            setD.iloc[n, 1] = 'Scatto 10m'
        # contatore.append(scatto)
        salto = window.count("Triplo salto in lungo")
        if salto > 1 or (salto == 2 and metri == 1 and scatto == 1 and navetta == 1):
            setD.iloc[n, 1] = 'Triplo salto in lungo'
        data = data.drop(data.index[:1])
        n += 1

    setD = setD.drop(setD.index[:1])
    new = setD.drop(setD.index[-1:])
    new.to_csv('Confronto3/futsal/P' + str(p) + '/window.csv', index=False)
