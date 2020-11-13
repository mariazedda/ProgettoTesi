import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, accuracy_score
import warnings
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import matthews_corrcoef
warnings.filterwarnings('ignore')

sport = input("sport : c/f \n")

if sport == "c":
    stringPath = "ConfrontoMod/calcio/P"
    classi = ["1000 metri", "Navetta 10x5", "Scatto 30m", "Triplo salto in lungo"]

else:
    stringPath = "ConfrontoMod/futsal/P"
    classi = ["1000 metri", "Navetta 5x10", "Scatto 10m", "Triplo salto in lungo"]

p_test = []
y_test = []

for p in range(1, 6):

    data = pd.read_csv(stringPath + str(p) + '/window.csv')

    y_temp = data.Reali

    p_temp = data.PredizioniFinestra

    y_test.extend(y_temp)
    p_test.extend(p_temp)

    model = RidgeClassifier(random_state=None)

    acc_test = accuracy_score(y_temp, p_temp)

    print("\nP" + str(p) + " :")
    print("\nAccuracy")
    print(f'Test {acc_test}')

    # Predizioni con il classificatore addestrato con dati di training
    arr = precision_recall_fscore_support(y_temp, p_temp, average='weighted')
    print("\nPrecision: ", arr[0], "\nRecall: ", arr[1], "\nF-1:", arr[2])

print("\n Totale: ")

arr = precision_recall_fscore_support(y_test, p_test, average='weighted')
print("\n\nPrecision: ", arr[0], "\nRecall: ", arr[1], "\nF-1:", arr[2])
print(matthews_corrcoef(y_test, p_test))
# Confusion Matrix
C = confusion_matrix(p_test, y_test)
df_cm = pd.DataFrame(C, classi, classi)
sns.set(font_scale=1.4)
graphic = sns.heatmap(df_cm, annot=True, annot_kws={"size": 16}, cmap="YlGnBu", fmt='g')
plt.show()
