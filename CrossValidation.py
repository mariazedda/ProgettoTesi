import csv

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, accuracy_score
import seaborn as sns
import warnings
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import RidgeClassifier

warnings.filterwarnings('ignore')

sport = input("sport : c/f \n")
# Load the Diabetes dataset

if sport == "c":
    stringPath = "TestTrainingFile/calcio"
    path = "calcio"
    classi = ["1000 metri", "Navetta 10x5", "Scatto 30m", "Triplo salto in lungo"]

else:
    stringPath = "TestTrainingFile/futsal"
    path = "futsal"
    classi = ["1000 metri", "Navetta 5x10", "Scatto 10m", "Triplo salto in lungo"]

p_test = []
y_test = []
count = 0
for p in range(1, 6):
    w_test = []
    w_pred = []
    w_mod = []

    train = pd.read_csv(stringPath + "/P" + str(p) + "/training.csv")
    test = pd.read_csv(stringPath + "/P" + str(p) + "/test.csv")

    y = train.Activity
    X = train.drop('Activity', axis=1)

    X_test = test.drop('Activity', axis=1)

    y_temp = test.Activity

    w_test.append("Reali")
    y_test.extend(y_temp)
    w_test.extend(y_temp)
    # fit a model (Random Forest)
    # model = DecisionTreeClassifier(random_state=None)
    # model = RandomForestClassifier(random_state=None)
    # model = GaussianNB()
    # model = SVC(random_state=None)
    model = RidgeClassifier(random_state=None)

    # Addestro il classificatore con i dati di training
    model.fit(X, y)

    # Predizione sui dati di test
    p_temp = model.predict(X_test)

    w_pred.append("Predizioni")
    w_mod.append("PredizioniFinestra")
    p_test.extend(p_temp)
    w_pred.extend(p_temp)
    w_mod.extend(p_temp)

    print("\nP" + str(p) + " :")

    # Calcolo della accuratezza
    acc_test = accuracy_score(y_temp, p_temp)
    print("\nAccuracy")
    print(f'Test {acc_test}')

    # Predizioni con il classificatore addestrato con dati di training
    arr = precision_recall_fscore_support(y_temp, p_temp, average='weighted')
    print("\nPrecision: ", arr[0], "\nRecall: ", arr[1], "\nF-1:", arr[2])

    """with open('Confronto/' + path + '/P' + str(p) + '/test.csv', 'w') as f:
        wtr = csv.writer(f)
        wtr.writerow(w_pred)
        wtr.writerow(w_mod)
        wtr.writerow(w_test)

    pd.read_csv('Confronto/' + path + '/P' + str(p) + '/test.csv',
                header=None).T.to_csv('Confronto/' + path + '/P' + str(p) + '/test.csv', header=False, index=False)
    """

print("\n Totale: ")

arr = precision_recall_fscore_support(y_test, p_test, average='weighted')
print("\n\nPrecision: ", arr[0], "\nRecall: ", arr[1], "\nF-1:", arr[2])



"""# Confusion Matrix
C = confusion_matrix(p_test, y_test)
df_cm = pd.DataFrame(C, classi, classi)
sns.set(font_scale=1.4)
graphic = sns.heatmap(df_cm, annot=True, annot_kws={"size": 16}, cmap="YlGnBu", fmt='g')
plt.show()"""
