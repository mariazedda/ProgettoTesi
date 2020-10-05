import csv

import pandas as pd
import warnings
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, max_error, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.stats import pearsonr

warnings.filterwarnings('ignore')

sport = input("sport : c/f \n")

if sport == "c":
    stringPath = "AverageTesterTrainingFile/calcio"
else:
    stringPath = "AverageTesterTrainingFile/futsal"

P_test = []
Y_test = []
res = []

for p in range(1, 6):
    train = pd.read_csv(stringPath + "/P" + str(p) + "/training.csv")
    test = pd.read_csv(stringPath + "/P" + str(p) + "/test.csv")

    Y_train = train['Score']  # memorizzo la variabile dipendente per il train
    X_train = train.drop('Score', axis=1)  # memorizzo le variabili indipendenti per il train

    X_test = test.drop('Score', axis=1)  # memorizzo le variabili idipendenti per il test
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

    # esprime quanto bene il modello descrive il dataset utilizzato
    print("\nRisultati P" + str(p) + ":\n")

    # media delle differenze assolute tra previsioni e target.
    print("MAE: ", mean_absolute_error(Y_temp, P_temp))

     # media delle differenze al quadrato tra previsioni e target.
    print("MSE: ", mean_squared_error(Y_temp, P_temp))

    # proporzione tra variabilità e correttezza dei dati del modello.
    print("R2: ", r2_score(Y_temp, P_temp))

    # misura di quanto i valori stimati si discostano dai valori reali
    print("MAXERROR: ", max_error(Y_temp, P_temp))

print("\n Totale:\n ")

print("MAE: ", mean_absolute_error(Y_test, P_test))
print("MSE: ", mean_squared_error(Y_test, P_test))
print("R2: ", r2_score(Y_test, P_test))
print("Errore Massimo: ", max_error(Y_test, P_test))
print("Correlazione tra previsti e effettivi:", pearsonr(Y_test, P_test)[0])

with open('1GroupExperiment\\Experiment2.2Futsal.csv', 'a') as f:
    wtr = csv.writer(f)
    wtr.writerow(Y_test)
    wtr.writerow(P_test)

