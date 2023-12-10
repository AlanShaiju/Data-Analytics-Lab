import numpy as np
import pandas as pd
class TreeNode:
    def __init__(self, gini, num_samples, num_samples_per_class, predicted_class):
        self.gini = gini
        self.num_samples = num_samples
        self.num_samples_per_class = num_samples_per_class
        self.predicted_class = predicted_class
        self.feature_index = 0
        self.threshold = 0
        self.left = None
        self.right = None
def gini_impurity(y):
    m = len(y)
    if m == 0:
        return 0
    num_samples_per_class = [sum(y == c) for c in set(y)]
    probability = [n / m for n in num_samples_per_class]
    return 1 - sum(p ** 2 for p in probability)
def find_best_split(X, y):
    m, n = X.shape
    if m <= 1:
        return None, None
    num_parent = [sum(y == c) for c in set(y)]
    best_gini = 1.0 - sum((num / m) ** 2 for num in num_parent)
    best_idx, best_thr = None, None
    for idx in range(n):
        thresholds, classes = zip(*sorted(zip(X[:, idx], y)))
        num_left = [0] * len(set(y))
        num_right = num_parent.copy()
        for i, c in enumerate(classes[:-1]):
            num_left[c] += 1
            num_right[c] -= 1
            #gini_left = 1.0 - sum((num_left[x] / i) ** 2 if i != 0 else 0 for x in range(len(set(y))))
            gini_left = 1.0 - sum((num_left[x] / (i + 1)) ** 2 for x in range(len(set(y))))
            gini_right = 1.0 - sum(
                (num_right[x] / (m - i)) ** 2 for x in range(len(set(y)))
            )
            gini = (i * gini_left + (m - i) * gini_right) / m
            if thresholds[i] == thresholds[i - 1]:
                continue
            if gini < best_gini:
                best_gini = gini
                best_idx = idx
                best_thr = (thresholds[i] + thresholds[i - 1]) / 2
    return best_idx, best_thr
def build_tree(X, y, depth=0, max_depth=None):
    num_samples_per_class = [sum(y == i) for i in range(2)]
    predicted_class = max(zip(num_samples_per_class, range(2)))[1]
    node = TreeNode(
        gini=gini_impurity(y),
        num_samples=len(y),
        num_samples_per_class=num_samples_per_class,
        predicted_class=predicted_class,
    )
    if depth < max_depth:
        idx, thr = find_best_split(X, y)
        if idx is not None:
            indices_left = X[:, idx] < thr
            X_left, y_left = X[indices_left], y[indices_left]
            X_right, y_right = X[~indices_left], y[~indices_left]
            node.feature_index = idx
            node.threshold = thr
            node.left = build_tree(X_left, y_left, depth + 1, max_depth)
            node.right = build_tree(X_right, y_right, depth + 1, max_depth)
    return node
def predict_sample(tree, sample):
    while tree.left:
        if sample[tree.feature_index] < tree.threshold:
            tree = tree.left
        else:
            tree = tree.right
    return tree.predicted_class
def predict(tree, X):
    return [predict_sample(tree, sample) for sample in X]
def main():
    file_path = 'C:/Users/Alan Shaiju/Python Codes/Data Analytics/dataset.csv'
    df = pd.read_csv(file_path)
    X = df.iloc[:, :-1].values  # Features
    y = df.iloc[:, -1].values   # Labels
    tree = build_tree(X, y, max_depth=11)
    print(tree)
    test = []
    print("Enter test data")
    for i in range(X.shape[1]):
        feature_value = float(input(f"Enter feature {i + 1} for the test data: "))
        test.append(feature_value)
    test = np.array([test])
    predictions = predict(tree, test)
    print("Predictions:", predictions)
main()