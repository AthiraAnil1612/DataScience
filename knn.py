import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score


dataset = pd.read_csv('Iris.csv')
if 'Id' in dataset.columns:
    dataset = dataset.drop('Id', axis=1)

X = dataset.iloc[:, :-1].values  # All columns except the last
Y = dataset.iloc[:, -1].values   # Last column (Species)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)


classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)


print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy Score: ", accuracy_score(y_test, y_pred))


df = pd.DataFrame({'Real Values': y_test, 'Predicted Values': y_pred})
print("\nComparison:\n", df)


new_test_point = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction = classifier.predict(new_test_point)
print(f"\nPredicted class for new data point: {prediction[0]}")
