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
    stringPath = "TesterTrainingFile\\calcio"
    fileName = "featuresCalcioNormalized.csv"
else:
    stringPath = "TesterTrainingFile\\futsal"
    fileName = "featuresFutsalNormalized.csv"

P_test = []
Y_test = []
Y_Total_Mean = []
P_Total_Mean = []
res = []
"""
    File utilizzato per gli esperimenti 1.2 e 3.2
"""
for p in range(1, 6):
    i = 0
    Y_Mean = []
    P_Mean = []
    train = pd.read_csv(stringPath + "\\P" + str(p) + "\\training.csv")
    test = pd.read_csv(stringPath + "\\P" + str(p) + "\\test.csv")

    Y_train = train['Score']  # memorizzo la variabile dipendente per il train
    X_train = train.drop('Score', axis=1)  # memorizzo le variabili indipendenti per il train
    
    X_test = test.drop('Score', axis=1)  # memorizzo le variabili idipendenti per il test
    Y_temp = test['Score']  # memorizzo la variabile dipendente per il test

    Y_test.extend(Y_temp)
    """data = pd.read_csv(fileName)
Y = data["Score"]
X = data.drop('Score', axis=1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, shuffle=False)"""


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
    y_int = mean(Y_temp).astype(int)

    if not mean(Y_temp) - y_int == 0:
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
    else:
        Y_Mean.append(mean(Y_temp))
        P_Mean.append(mean(P_temp))
        Y_Total_Mean.extend(Y_Mean)
        P_Total_Mean.extend(P_Mean)

        # esprime quanto bene il modello descrive il dataset utilizzato
        print("\nRisultati P" + str(p) + ":\n")

        # media delle differenze assolute tra previsioni e target.
        print("MAE: ", mean_absolute_error(Y_Mean, P_Mean))

        # media delle differenze al quadrato tra previsioni e target.
        print("MSE: ", mean_squared_error(Y_Mean, P_Mean))

        # proporzione tra variabilità e correttezza dei dati del modello.
        print("R2: ", r2_score(Y_Mean, P_Mean))

        # misura di quanto i valori stimati si discostano dai valori reali
        print("Max Error: ", max_error(Y_Mean, P_Mean))


print("\n Totale:\n ")

print("MAE: ", mean_absolute_error(Y_Total_Mean, P_Total_Mean))
print("MSE: ", mean_squared_error(Y_Total_Mean, P_Total_Mean))
print("R2: ", r2_score(Y_Total_Mean, P_Total_Mean))
print("Errore Massimo: ", max_error(Y_Total_Mean, P_Total_Mean))
print("Correlazione tra previsti e effettivi:", pearsonr(Y_Total_Mean, P_Total_Mean)[0])

# grafico:
"""with open('2GroupExperiment\\Experiment3Futsal.csv', 'a') as f:
    wtr = csv.writer(f)
    wtr.writerow(Y_Total_Mean)
    wtr.writerow(P_Total_Mean)"""

"""# grafico dei residui: residui in ordinate e valori di X nelle ascisse
res = np.array(Y_test) - np.array(P_test)
snp.scatterplot(x=Y_test, y=res)
ptl.show()"""

"""data = pd.read_csv(fileName)
Y = data["Score"]
X = data.drop('Score', axis=1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, shuffle=False)"""
