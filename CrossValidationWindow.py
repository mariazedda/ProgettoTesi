import csv

import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, accuracy_score
import warnings
from sklearn.linear_model import RidgeClassifier

warnings.filterwarnings('ignore')

sport = input("sport : c/f \n")
# Load the Diabetes dataset

if sport == "c":
    stringPath = "Confronto/calcio/P"
    classi = ["1000 metri", "Navetta 10x5", "Scatto 30m", "Triplo salto in lungo"]

else:
    stringPath = "Confronto/futsal/P"
    classi = ["1000 metri", "Navetta 5x10", "Scatto 10m", "Triplo salto in lungo"]

p_test = []
y_test = []
w_test = []
w_pred = []
w_mod = []
count = 0
for p in range(1, 6):
    train = pd.read_csv(stringPath + str(p) + '/training.csv')
    test = pd.read_csv(stringPath + str(p) + '/test.csv')

    y = test.Reali

    y_temp = test.PredizioniFinestra

    y_test.extend(y)
    p_test.extend(y_temp)
    model = RidgeClassifier(random_state=None)

    acc_test = accuracy_score(y, y_temp)

    print("\nP" + str(p) + " :")
    print("\nAccuracy")
    print(f'Test {acc_test}')

    # Predizioni con il classificatore addestrato con dati di training
    arr = precision_recall_fscore_support(y, y_temp, average='weighted')
    print("\nPrecision: ", arr[0], "\nRecall: ", arr[1], "\nF-1:", arr[2])

print("\n Totale: ")

arr = precision_recall_fscore_support(y_test, p_test, average='weighted')
print("\n\nPrecision: ", arr[0], "\nRecall: ", arr[1], "\nF-1:", arr[2])

"""# Confusion Matrix
C = confusion_matrix(p_test, y_test)
df_cm = pd.DataFrame(C, classi, classi)
sns.set(font_scale=1.4)
graphic = sns.heatmap(df_cm, annot=True, annot_kws={"size": 16}, cmap="YlGnBu", fmt='g')
plt.show()"""