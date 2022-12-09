import pandas as pd
import seaborn as sns

#Q 1
data = pd.read_csv("Iris.csv")

#Q 2
print(data.head(10))

print(data.shape)

#Q 3
sns.displot(data= data)