import csv
import pandas as pd
import numpy as np
import statsmodels.api as sm
import warnings
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, max_error, mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
warnings.filterwarnings('ignore')

sport = input("sport : c/f \n")

if sport == "c":
    stringPath = "TesterTrainingFile/calcio"
    fileName = "featuresCalcioNormalized.csv"
else:
    stringPath = "TesterTrainingFile/futsal"
    fileName = "featureFutsalNormalized.csv"

P_test = []
Y_test = []

for p in range(1, 6):
    train = pd.read_csv(stringPath + "/P" + str(p) + "/training.csv", index_col=0)
    test = pd.read_csv(stringPath + "/P" + str(p) + "/test.csv", index_col=0)

    Y_train = train['Score']  # memorizzo la variabile dipendente per il train
    X_train = train.drop('Score', axis=1)  # memorizzo le variabili indipendenti per il train
    
    X_test = test.drop('Score', axis=1)  # memorizzo le variabili idipendenti per il test
    Y_temp = test['Score']  # memorizzo la variabile dipendente per il test

    Y_test.extend(Y_temp)
    """data = pd.read_csv(fileName)
    Y = data["Score"]
    X = data.drop('Score', axis=1)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, shuffle=False)"""

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
    # print("Risultati:\n")

    # media delle differenze assolute tra previsioni e target.
    print("MAE: ", mean_absolute_error(Y_temp, P_temp))

    # proporzione tra variabilità e correttezza dei dati del modello.
    print("R2 test: ", r2_score(Y_temp, P_temp))

    # media delle differenze al quadrato tra previsioni e target.
    print("MSE: ", mean_squared_error(Y_temp, P_temp))

print("\n Totale:\n ")

print("MAE: ", mean_absolute_error(Y_test, P_test))
print("R2 test: ", r2_score(Y_test, P_test))
print("MSE: ", mean_squared_error(Y_test, P_test))







