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
    stringPath = "TestTrainingFile/calcio"
else:
    stringPath = "TestTrainingFile/futsal"

P_test = []
Y_test = []
res = []

for p in range(1, 6):
    train = pd.read_csv(stringPath + "/P" + str(p) + "/training.csv")
    test1 = pd.read_csv(stringPath + "/P" + str(p) + "/test1.csv")
    test2 = pd.read_csv(stringPath + "/P" + str(p) + "/test2.csv")

    Y_train = train['Score']  # memorizzo la variabile dipendente per il train
    X_train = train.drop('Score', axis=1)  # memorizzo le variabili indipendenti per il train

    X_test1 = test1.drop('Score', axis=1)  # memorizzo le variabili idipendenti per il test
    Y_temp1 = test1['Score']  # memorizzo la variabile dipendente per il test
    X_test2 = test2.drop('Score', axis=1)  # memorizzo le variabili idipendenti per il test
    Y_temp2 = test2['Score']

    Y_test.extend(Y_temp1)
    Y_test.extend(Y_temp2)

    # standardizzo le variabili dipendenti di train e di test
    ss = StandardScaler()
    X_train_std = ss.fit_transform(X_train)
    X_test_std1 = ss.transform(X_test1)
    X_test_std2 = ss.transform(X_test2)

    # imposto il modello
    model = LinearRegression()

    # Addestro il classificatore con i dati di training
    model.fit(X_train_std, Y_train)

    # Predizione sui dati di test
    P_temp1 = model.predict(X_test_std1)
    P_temp2 = model.predict(X_test_std2)

    P_test.extend(P_temp1)
    P_test.extend(P_temp2)

    # esprime quanto bene il modello descrive il dataset utilizzato
    print("\nRisultati P" + str(p) + ":\n")

    # media delle differenze assolute tra previsioni e target.
    print("MAE: Es 1", mean_absolute_error(Y_temp1, P_temp1))
    print("MAE: Es 2", mean_absolute_error(Y_temp2, P_temp2))

     # media delle differenze al quadrato tra previsioni e target.
    print("MSE Es 1: ", mean_squared_error(Y_temp1, P_temp1))
    print("MSE Es 2: ", mean_squared_error(Y_temp2, P_temp2))

    # proporzione tra variabilità e correttezza dei dati del modello.
    print("R2 Es1: ", r2_score(Y_temp1, P_temp1))
    print("R2 Es2: ", r2_score(Y_temp2, P_temp2))

    # misura di quanto i valori stimati si discostano dai valori reali
    print("MAXERROR Es 1: ", max_error(Y_temp1, P_temp1))
    print("MAXERROR Es 2: ", max_error(Y_temp2, P_temp2))

print("\n Totale:\n ")

print("MAE: ", mean_absolute_error(Y_test, P_test))
print("MSE: ", mean_squared_error(Y_test, P_test))
print("R2: ", r2_score(Y_test, P_test))
print("Errore Massimo: ", max_error(Y_test, P_test))
print("Correlazione tra previsti e effettivi:", pearsonr(Y_test, P_test)[0])

with open('1GroupExperiment/Experiment1.3Calcio.csv', 'a') as f:
    wtr = csv.writer(f)
    wtr.writerow(Y_test)
    wtr.writerow(P_test)

