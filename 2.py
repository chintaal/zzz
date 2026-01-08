import numpy as np
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

print("="*50)
print("K-Nearest Neighbors Classifier")
print("="*50)

# Load data
iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names
print(f"✓ Dataset loaded: {X.shape[0]} samples")
print(f"  Classes: {', '.join(class_names)}")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)
print(f"✓ Split: {len(X_train)} training, {len(X_test)} test samples")

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        return np.array([self._predict(x) for x in X])

    def _predict(self, x):
        distances = [np.linalg.norm(x - x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_labels = [self.y_train[i] for i in k_indices]
        return Counter(k_labels).most_common(1)[0][0]

# Train & Test
k_value = int(input("\nEnter k value (number of neighbors, default 3): ") or 3)
knn = KNN(k=k_value)
print(f"\n→ Training KNN with k={k_value}...")
knn.fit(X_train, y_train)
print("✓ Training complete")

print(f"\n→ Making predictions on {len(X_test)} test samples...")
y_pred = knn.predict(X_test)
print("✓ Predictions complete\n")

accuracy = np.mean(y_pred == y_test)
print(f"📊 Results:")
print(f"  Accuracy: {accuracy:.2%}")
print(f"\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))
