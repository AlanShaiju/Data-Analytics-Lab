import numpy as np
import pandas as pd
class TreeNode:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value
def entropy(y):
    classes, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    return -np.sum(probabilities * np.log2(probabilities + 1e-10))
def information_gain(X, y, feature, threshold):
    left_mask = X[:, feature] < threshold
    right_mask = ~left_mask
    left_entropy = entropy(y[left_mask])
    right_entropy = entropy(y[right_mask])
    left_weight = sum(left_mask) / len(y)
    right_weight = sum(right_mask) / len(y)
    return entropy(y) - (left_weight * left_entropy + right_weight * right_entropy)
def find_best_split(X, y):
    best_gain = 0
    best_feature = None
    best_threshold = None
    for feature in range(X.shape[1]):
        thresholds = np.unique(X[:, feature])
        for threshold in thresholds:
            gain = information_gain(X, y, feature, threshold)
            if gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_threshold = threshold
    return best_feature, best_threshold
def build_tree(X, y, depth=0, max_depth=None):
    if depth == max_depth or len(set(y)) == 1:
        return TreeNode(value=np.argmax(np.bincount(y)))
    feature, threshold = find_best_split(X, y)
    if feature is None:
        return TreeNode(value=np.argmax(np.bincount(y)))
    left_mask = X[:, feature] < threshold
    right_mask = ~left_mask
    left_subtree = build_tree(X[left_mask], y[left_mask], depth + 1, max_depth)
    right_subtree = build_tree(X[right_mask], y[right_mask], depth + 1, max_depth)
    return TreeNode(feature=feature, threshold=threshold, left=left_subtree, right=right_subtree)
def predict_sample(tree, sample):
    if tree.value is not None:
        return tree.value
    if sample[tree.feature] < tree.threshold:
        return predict_sample(tree.left, sample)
    else:
        return predict_sample(tree.right, sample)
def predict(tree, X):
    return [predict_sample(tree, sample) for sample in X]
def main():
    file_path = 'C:/Users/Alan Shaiju/Python Codes/Data Analytics/dataset.csv'
    df = pd.read_csv(file_path)
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    tree = build_tree(X, y, max_depth=11)
    test = []
    print("Enter test data:")
    for i in range(X.shape[1]):
        feature_value = float(input(f"Enter feature {i + 1} for the test data: "))
        test.append(feature_value)
    test = np.array([test])
    predictions = predict(tree, test)
    print("Predictions:", predictions)
main()