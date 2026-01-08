import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

print("="*50)
print("Logistic Regression - Binary Classification")
print("="*50)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression(X, y, lr=0.001, iterations=200):
    weights = np.zeros(X.shape[1])
    print(f"\n→ Training with learning rate={lr}, iterations={iterations}")
    for i in range(iterations):
        z = X @ weights
        h = sigmoid(z)
        gradient = X.T @ (h - y) / y.size
        weights -= lr * gradient
        if (i+1) % 50 == 0:
            loss = -np.mean(y * np.log(h + 1e-8) + (1-y) * np.log(1-h + 1e-8))
            print(f"  Iteration {i+1}/{iterations}, Loss: {loss:.4f}")
    print("✓ Training complete")
    return weights

# Data
iris = load_iris()
X = iris.data[:, :2]
y = (iris.target != 0).astype(int)
print(f"✓ Dataset loaded: {X.shape[0]} samples (binary classification)")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=9
)
print(f"✓ Split: {len(X_train)} training, {len(X_test)} test samples")

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print("✓ Features standardized")

lr = float(input("\nEnter learning rate (default 0.001): ") or 0.001)
iterations = int(input("Enter number of iterations (default 200): ") or 200)

weights = logistic_regression(X_train, y_train, lr, iterations)
y_pred = sigmoid(X_test @ weights) > 0.5

accuracy = np.mean(y_pred == y_test)
print(f"\n📊 Results:")
print(f"  Test Accuracy: {accuracy:.2%}")
print(f"  Learned weights: {weights}")
