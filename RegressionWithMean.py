import csv
import pandas as pd
import numpy as np
import warnings
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, max_error, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
from numpy import mean
from scipy.stats import pearsonr
import seaborn as sns
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

sport = input("sport : c/f \n")

if sport == "c":
    stringPath = "DividedTestTrainingFile\\calcio"
    filePath = '1GroupExperiment\\Experiment1.2Calcio'
else:
    stringPath = "DividedTestTrainingFile\\futsal"
    filePath = '1GroupExperiment1.2Futsal'

P_test = []
Y_test = []

Y_Total_Mean = []
P_Total_Mean = []
"""
    File utilizzato per gli esperimenti 1.2 e 3.2
"""
for p in range(1, 6):
    """if p != 4:
        i = 0
        Y_Mean1 = []
        Y_Mean2 = []
        P_Mean1 = []
        P_Mean2 = []
        print(stringPath + "\\P" + str(p) + "\\training.csv")
        train = pd.read_csv(stringPath + "\\P" + str(p) + "\\training.csv")
        test1 = pd.read_csv(stringPath + "\\P" + str(p) + "\\test1.csv")
        test2 = pd.read_csv(stringPath + "\\P" + str(p) + "\\test2.csv")

        Y_train = train['Score']  # memorizzo la variabile dipendente per il train
        X_train = train.drop('Score', axis=1)  # memorizzo le variabili indipendenti per il train

        X_test1 = test1.drop('Score', axis=1)  # memorizzo le variabili idipendenti per il test
        Y_temp1 = test1['Score']  # memorizzo la variabile dipendente per il test

        X_test2 = test2.drop('Score', axis=1)  # memorizzo le variabili idipendenti per il test
        Y_temp2 = test2['Score']  # memorizzo la variabile dipendente per il test

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

        Y_Mean1.append(mean(Y_temp1))
        Y_Mean2.append(mean(Y_temp2))
        P_Mean1.append(mean(P_temp1))
        P_Mean2.append(mean(P_temp2))
        Y_Total_Mean.extend(Y_Mean1)
        Y_Total_Mean.extend(Y_Mean2)
        P_Total_Mean.extend(P_Mean1)
        P_Total_Mean.extend(P_Mean2)

        # esprime quanto bene il modello descrive il dataset utilizzato
        print("\nRisultati P" + str(p) + ":\n")

        # media delle differenze assolute tra previsioni e target.
        print("MAE 1 esercizio: ", mean_absolute_error(Y_Mean1, P_Mean1))
        print("MAE 2 esercizio: ", mean_absolute_error(Y_Mean2, P_Mean2))

        # media delle differenze al quadrato tra previsioni e target.
        print("MSE 1 esercizio:: ", mean_squared_error(Y_Mean1, P_Mean1))
        print("MSE 2 esercizio:: ", mean_squared_error(Y_Mean2, P_Mean2))

        # proporzione tra variabilità e correttezza dei dati del modello.
        print("R2 1 esercizio: ", r2_score(Y_Mean1, P_Mean1))
        print("R2 2 esercizio: ", r2_score(Y_Mean2, P_Mean2))

        # misura di quanto i valori stimati si discostano dai valori reali
        print("Max Error 1 esercizio:  ", max_error(Y_Mean1, P_Mean1))
        print("Max Error 2 esercizio: ", max_error(Y_Mean2, P_Mean2))

        for s in range(1, 3):
            with open(filePath + '.csv', 'a') as f:
                wtr = csv.writer(f)
                wtr.writerow(str(p))
                if s == 1:
                    wtr.writerow("E1")
                    wtr.writerow(Y_Mean1)
                    wtr.writerow(P_Mean1)
                else:
                    wtr.writerow("E2")
                    wtr.writerow(Y_Mean2)
                    wtr.writerow(P_Mean2)

    else:"""
    i = 0
    Y_Mean = []
    Y_Mean2 = []
    P_Mean = []
    P_Mean2 = []
    train = pd.read_csv(stringPath + "\\P" + str(p) + "\\training.csv")
    test = pd.read_csv(stringPath + "\\P" + str(p) + "\\test.csv")

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

    """if not mean(Y_temp) - y_int == 0:
        c = Y_temp.iloc[0]
        for x in range(0, Y_temp.shape[0]):
            if Y_temp.iloc[x] != c:
                i = x
                break

    if i != 0:
        t = i-1
        Y_Mean_1 = [mean(Y_temp[:i])]
        Y_Mean_2 = [mean(Y_temp[i+1:])]
        P_Mean_1 = [mean(P_temp[:i])]
        P_Mean_2 = [mean(P_temp[i+1:])]
        Y_Total_Mean.extend(Y_Mean_1)
        Y_Total_Mean.extend(Y_Mean_2)
        P_Total_Mean.extend(P_Mean_1)
        P_Total_Mean.extend(P_Mean_2)

        # esprime quanto bene il modello descrive il dataset utilizzato
        print("\nRisultati P" + str(p) + ":\n")

        # media delle differenze assolute tra previsioni e target.
        mae1 = mean_absolute_error(Y_Mean_1, P_Mean_1)
        mae2 = mean_absolute_error(Y_Mean_2, P_Mean_2)
        print("MAE: ", (mae1 + mae2)/2)

        # media delle differenze al quadrato tra previsioni e target.
        mse1 = mean_squared_error(Y_Mean_1, P_Mean_1)
        mse2 = mean_squared_error(Y_Mean_2, P_Mean_2)
        print("MSE: ", (mse1 + mse2)/2)

        # proporzione tra variabilità e correttezza dei dati del modello.
        r1 = r2_score(Y_Mean_1, P_Mean_1)
        r2 = r2_score(Y_Mean_2, P_Mean_2)
        print("R2: ", (r1 + r2)/2)

        # misura di quanto i valori stimati si discostano dai valori reali
        max1 = max_error(Y_Mean_1, P_Mean_1)
        max2 = max_error(Y_Mean_2, P_Mean_2)
        print("MAX ERROR:", (max1 + max2)/2)
    else:"""
    Y_Mean.append(mean(Y_temp))

    P_Mean.append(mean(P_temp))

    Y_Total_Mean.extend(Y_Mean)

    P_Total_Mean.extend(P_Mean)


    # esprime quanto bene il modello descrive il dataset utilizzato
    print("\nRisultati P" + str(p) + ":\n")

    # media delle differenze assolute tra previsioni e target.
    print("MAE 1 esercizio: ", mean_absolute_error(Y_Mean, P_Mean))

    # media delle differenze al quadrato tra previsioni e target.
    print("MSE 1 esercizio:: ", mean_squared_error(Y_Mean, P_Mean))

    # proporzione tra variabilità e correttezza dei dati del modello.
    print("R2 1 esercizio: ", r2_score(Y_Mean, P_Mean))

    # misura di quanto i valori stimati si discostano dai valori reali
    print("Max Error 1 esercizio:  ", max_error(Y_Mean, P_Mean))

    with open(filePath + '.csv', 'a') as f:
        wtr = csv.writer(f)
        wtr.writerow(str(p))
        wtr.writerow("E1")
        wtr.writerow(Y_Mean)
        wtr.writerow(P_Mean)

print("\n Totale:\n ")

print("MAE: ", mean_absolute_error(Y_Total_Mean, P_Total_Mean))
print("MSE: ", mean_squared_error(Y_Total_Mean, P_Total_Mean))
print("R2: ", r2_score(Y_Total_Mean, P_Total_Mean))
print("Errore Massimo: ", max_error(Y_Total_Mean, P_Total_Mean))
print("Correlazione tra previsti e effettivi:", pearsonr(Y_Total_Mean, P_Total_Mean)[0])



