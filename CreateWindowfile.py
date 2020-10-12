import pandas as pd
from numpy import mean, var, fft, diff, sign, correlate
from scipy.stats import kurtosis, skew
import csv
import warnings
from sklearn.metrics import precision_recall_fscore_support

warnings.filterwarnings('ignore')

sport = input("sport : c/f \n")

if sport == "c":
    fileName = 'ConfrontoCalcio.csv'
    path = 'ConfrontoCalcioMod'
else:
    fileName = 'ConfrontoFutsal.csv'
    path = 'ConfrontoFutsalMod'

set = pd.read_csv(fileName)
data = set.Predizioni
shapeData = data.shape
row = int((shapeData[0]) - 8)
set.iloc[0, 1] = ''
set.iloc[1, 1] = ''
n = 2
for w in range(0, row):
    window = []
    contatore = []
    window.extend(data.iloc[:5])
    metri = window.count("1000 metri")
    contatore.append(metri)
    navetta = window.count("Navetta 5x10")
    contatore.append(navetta)
    scatto = window.count("Scatto 30m")
    contatore.append(scatto)
    salto = window.count("Triplo salto in lungo")
    contatore.append(salto)
    max = contatore[0]
    for i in range(0, 4):
        if contatore[i] > max:
            max = contatore[i]
    for i in range(1, 5):
        if metri == max:
            set.iloc[n, 1] = '1000 metri'
        elif navetta == max:
            set.iloc[n, 1] = 'Navetta 10x5'
        elif scatto == max:
            set.iloc[n, 1] = 'Scatto 30m'
        else:
            set.iloc[n, 1] = 'Triplo salto in lungo'
    data = data.drop(data.index[:1])
    n += 1

set = set.drop(set.index[:2])
new = set.drop(set.index[-2:])
new.to_csv(path + '.csv', index=False)

