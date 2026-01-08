import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

print("="*50)
print("K-Means Clustering on Iris Dataset")
print("="*50)

# Load dataset
iris = load_iris()
X = iris.data
print(f"✓ Dataset loaded: {X.shape[0]} samples, {X.shape[1]} features")

def kmeans(X, k, iterations=100):
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]
    print(f"\n→ Starting K-Means with {k} clusters...")
    for i in range(iterations):
        distances = np.linalg.norm(X[:, None] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        new_centroids = np.array([X[labels == j].mean(axis=0) for j in range(k)])
        if np.allclose(centroids, new_centroids):
            print(f"✓ Converged after {i+1} iterations")
            break
        centroids = new_centroids
        if (i+1) % 20 == 0:
            print(f"  Iteration {i+1}/{iterations}...")
    return centroids, labels

# Run K-Means
k = int(input("\nEnter number of clusters (default 3): ") or 3)
centroids, labels = kmeans(X, k)

# Display cluster sizes
for i in range(k):
    count = np.sum(labels == i)
    print(f"  Cluster {i+1}: {count} samples")

# Plot
colors = ['r', 'g', 'b']
for i in range(k):
    plt.scatter(X[labels == i, 0], X[labels == i, 1],
                c=colors[i], label=f'Cluster {i+1}')
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', c='black', label='Centroids')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('K-Means Clustering on Iris Dataset')
plt.legend()
plt.show()
