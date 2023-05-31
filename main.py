import pandas as pd

data = pd.read_csv('iris.csv')

print(data.target)
print(data['sepal length (cm)'])
print(data['petal length (cm)'])

