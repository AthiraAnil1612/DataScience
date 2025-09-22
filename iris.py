import matplotlib.pyplot as plt
import seabron as sns
import pandas as pd
iris=pd.read_csv("iris.csv")
print("shape of data set :",iris.shape)
print("First five rows")
print("*********************")
print("last five rows")
print(iris.tail())
print("size of the dataset:",iris.size)
print("number of samples available for each variety")
print(iris["variety"].value_counts())
print("description of the data set")
print(iris.describe())
sns.pairplot(iris,hue="variety", kind="scatter",diag_kind="hist")
plt.style.use("dark_background")
sns.displot(iris.sepal_length,bins=10, color="g")
plt.title("Distribution of Sepal Length", fontsize=10, color="white")
plt.show()
