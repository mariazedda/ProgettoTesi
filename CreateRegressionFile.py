import pandas as pd
import csv


sport = input("sport : c/f \n")

if sport == "c":
    fileName = 'Features/calcio/P'
    path = 'calcio'
else:
    fileName = 'Features/futsal/P'
    path = 'futsal'

countP = 0
for p in range(1, 6):
    count = 0
    for pTrain in range(1, 6):
        if pTrain == p:
            data = pd.read_csv(fileName + str(p) + '/features.csv')
            data.to_csv('TestTrainingFile/' + path + '/P' + str(p) + '/test.csv', index=False)
        else:
            data = pd.read_csv(fileName + str(pTrain) + '/features.csv')
            if count == 0 or countP == 0:
                with open('TestTrainingFile/' + path + '/P' + str(p) + '/training.csv', 'w', newline='') as f:
                    data.to_csv(f, index=False)
                    if countP == 0:
                        countP = 1
            else:
                with open('TestTrainingFile/' + path + '/P' + str(p) + '/training.csv', 'a', newline='') as f:
                    data.to_csv(f, header=False, index=False)

            count += 1
