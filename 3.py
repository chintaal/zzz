import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# Load data
iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names

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
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

nb = NaiveBayes()
nb.fit(X_train, y_train)
y_pred = nb.predict(X_test)

print("Accuracy:", np.mean(y_pred == y_test))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n",
      classification_report(y_test, y_pred, target_names=class_names))
