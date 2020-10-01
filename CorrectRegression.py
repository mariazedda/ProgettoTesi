import csv
import pandas as pd
import numpy as np
import warnings
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, max_error, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from numpy import mean
from scipy.stats import pearsonr
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

sport = input("sport : c/f \n")

if sport == "c":
    stringPath = "TesterTrainingFile/calcio"
    fileName = "featuresCalcioNormalized.csv"
else:
    stringPath = "TesterTrainingFile/futsal"
    fileName = "featuresFutsalNormalized.csv"

"""data = pd.read_csv(fileName)
dataCorrelation = data.corr()
testColumn = dataCorrelation.shape[1]

datasetShape = dataCorrelation.shape

# dataCorrelation = dataCorrelation.Score
dataCorrelation = dataCorrelation.Score

rowSet = datasetShape[0]
colSet = datasetShape[1]
with open('DatasetCorrectFutsal.csv', 'w', newline='') as f:
    wtr = csv.writer(f)
    for row in range(0, rowSet-1):
        c = dataCorrelation.iloc[row]
        if c > 0.3:
            wtr.writerow(dataCorrelation.index[[row]])
"""
P_test = []
Y_test = []

for p in range(1, 6):
    train = pd.read_csv(stringPath + "/P" + str(p) + "/training.csv", index_col=0)
    test = pd.read_csv(stringPath + "/P" + str(p) + "/test.csv", index_col=0)
    
    Y_train = train['Score']  # memorizzo la variabile dipendente per il train
    X_train = train[["dQ-x-var", "dQ-x-aut1", "dQ-x-pks3", "dV-1-aut5", "dV-2-avg",
                     "dV-2-var", "dV-2-aut1", "dV-2-aut5", "dV-2-pks1", "Mag-x-max",
                     "Mag-x-min", "Mag-x-avg", "Mag-y-aut4", "Mag-z-max", "Mag-z-min",
                     "Mag-z-avg", "FreeAcc-x-var", "FreeAcc-x-aut1", "FreeAcc-x-aut5",
                     "FreeAcc-x-pks1", "FreeAcc-y-var", "FreeAcc-y-aut1", "FreeAcc-z-var",
                     "FreeAcc-z-aut1", "FreeAcc-z-aut3", "FreeAcc-z-aut5"]]  # memorizzo le variabili indipendenti per il train

    X_test = test[["dQ-x-var", "dQ-x-aut1", "dQ-x-pks3", "dV-1-aut5", "dV-2-avg",
                     "dV-2-var", "dV-2-aut1", "dV-2-aut5", "dV-2-pks1", "Mag-x-max",
                     "Mag-x-min", "Mag-x-avg", "Mag-y-aut4", "Mag-z-max", "Mag-z-min",
                     "Mag-z-avg", "FreeAcc-x-var", "FreeAcc-x-aut1", "FreeAcc-x-aut5",
                     "FreeAcc-x-pks1", "FreeAcc-y-var", "FreeAcc-y-aut1", "FreeAcc-z-var",
                     "FreeAcc-z-aut1", "FreeAcc-z-aut3", "FreeAcc-z-aut5"]]  # memorizzo le variabili idipendenti per il test
    Y_temp = test['Score']  # memorizzo la variabile dipendente per il test

    Y_test.extend(Y_temp)

    # standardizzo le variabili dipendenti di train e di test
    ss = StandardScaler()
    X_train_std = ss.fit_transform(X_train)
    X_test_std = ss.transform(X_test)

    # imposto il modello
    model = LinearRegression()

    # Addestro il classificatore con i dati di training
    model.fit(X_train_std, Y_train)
    # Predizione sui dati di test
    P_temp = model.predict(X_test_std)

    P_test.extend(P_temp)

    print("\nRisultati P" + str(p) + ":\n")

    # media delle differenze assolute tra previsioni e target.
    print("MAE: ", mean_absolute_error(Y_temp, P_temp))

    # media delle differenze al quadrato tra previsioni e target.
    print("MSE: ", mean_squared_error(Y_temp, P_temp))

    # proporzione tra variabilità e correttezza dei dati del modello.
    print("R2 test: ", r2_score(Y_temp, P_temp))

    # misura di quanto i valori stimati si discostano dai valori reali
    print("Max Error: ", max_error(Y_temp, P_temp))

print("\n Totale:\n ")

print("MAE: ", mean_absolute_error(Y_test, P_test))
print("MSE: ", mean_squared_error(Y_test, P_test))
print("R2 test: ", r2_score(Y_test, P_test))
print("Errore Massimo: ", max_error(Y_test, P_test))
print("Correlazione tra previsti e effettivi:", pearsonr(Y_test, P_test)[0])
with open('Experiment4Futsal.csv', 'a') as f:
    wtr = csv.writer(f)
    wtr.writerow(Y_test)
    wtr.writerow(P_test)
"""sns.heatmap(data.corr(), xticklabels=data.columns, yticklabels=data.columns)
plt.show()"""

