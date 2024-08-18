import pandas as pd
data = pd.read_csv("Lesson_2/titanic.csv")
print(data.head())
print(data.info())
print(data.shape)
print(data[["Name", "Age"]])
col = data[["Name", "Age"]]
