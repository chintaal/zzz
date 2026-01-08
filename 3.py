import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

print("="*50)
print("Naive Bayes Classifier")
print("="*50)

# Load data
iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names
print(f"✓ Dataset loaded: {X.shape[0]} samples")
print(f"  Classes: {', '.join(class_names)}")

class NaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.mean = np.array([X[y == c].mean(axis=0) for c in self.classes])
        self.var = np.array([X[y == c].var(axis=0) for c in self.classes])
        self.priors = np.array([X[y == c].shape[0] / len(y) for c in self.classes])

    def predict(self, X):
        return np.array([self._predict(x) for x in X])

    def _predict(self, x):
        posteriors = []
        for i in range(len(self.classes)):
            prior = np.log(self.priors[i])
            likelihood = np.sum(np.log(self._pdf(i, x)))
            posteriors.append(prior + likelihood)
        return self.classes[np.argmax(posteriors)]

    def _pdf(self, class_idx, x):
        mean = self.mean[class_idx]
        var = self.var[class_idx]
        return np.exp(-(x - mean)**2 / (2 * var)) / np.sqrt(2 * np.pi * var)

# Train & Test
test_size = float(input("\nEnter test split ratio (default 0.3): ") or 0.3)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=1
)
print(f"✓ Split: {len(X_train)} training, {len(X_test)} test samples")

nb = NaiveBayes()
print("\n→ Training Naive Bayes classifier...")
nb.fit(X_train, y_train)
print("✓ Training complete")
print(f"  Computed priors: {nb.priors}")

print(f"\n→ Making predictions on {len(X_test)} test samples...")
y_pred = nb.predict(X_test)
print("✓ Predictions complete\n")

accuracy = np.mean(y_pred == y_test)
print(f"📊 Results:")
print(f"  Accuracy: {accuracy:.2%}")
print(f"\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))
