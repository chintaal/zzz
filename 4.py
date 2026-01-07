import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression(X, y, lr=0.001, iterations=200):
    weights = np.zeros(X.shape[1])
    for _ in range(iterations):
        z = X @ weights
        h = sigmoid(z)
        gradient = X.T @ (h - y) / y.size
        weights -= lr * gradient
    return weights

# Data
iris = load_iris()
X = iris.data[:, :2]
y = (iris.target != 0).astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=9
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

weights = logistic_regression(X_train, y_train)
y_pred = sigmoid(X_test @ weights) > 0.5

print("Accuracy:", np.mean(y_pred == y_test))
