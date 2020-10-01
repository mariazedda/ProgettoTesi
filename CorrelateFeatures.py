import csv
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

sport = input("sport : c/f \n")

if sport == "c":
    fileName = "featuresCalcioNormalized.csv"
    path = 'Calcio'
else:
    fileName = "featuresFutsalNormalized.csv"
    path = 'Futsal'

data = pd.read_csv(fileName)
dataCorrelation = data.corr()
datasetShape = dataCorrelation.shape

dataCorrelation = dataCorrelation.Score

rowSet = datasetShape[0]
colSet = datasetShape[1]
with open('DatasetCorrect' + path + '.csv', 'w', newline='') as f:
    wtr = csv.writer(f)
    for row in range(0, rowSet-1):
        c = dataCorrelation.iloc[row]
        if c > 0.7:
            wtr.writerow(dataCorrelation.index[[row]])
