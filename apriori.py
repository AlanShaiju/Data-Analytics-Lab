import csv
from itertools import combinations

file_path = 'C:/Users/Alan Shaiju/Python Codes/Data Analytics/apriori.csv'

# Read transactions from CSV
transactions = []
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    transactions = [list(row) for row in reader]

def apriori(transactions, min_support):
    # Calculate frequent items of size 1
    C1 = {}
    for transaction in transactions:
        for item in transaction:
            if item in C1:
                C1[item] += 1
            else:
                C1[item] = 1
    L1 = {key: value for key, value in C1.items() if value/len(transactions) >= min_support}
    L = [L1]
    k = 2
    while len(L[k-2]) > 0:
        Ck = {}
        for transaction in transactions:
            combos = combinations(transaction, k)
            for combo in combos:
                if combo in Ck:
                    Ck[combo] += 1
                else:
                    Ck[combo] = 1
        Lk = {key: value for key, value in Ck.items() if value/len(transactions) >= min_support}
        L.append(Lk)
        k += 1
    return [item for sublist in L for item in sublist.keys()]


def association_rules(frequent_itemsets, transactions, min_confidence):
    rules = []
    for itemset in frequent_itemsets:
        for i in range(1, len(itemset)):
            antecedents = [x for x in combinations(itemset, i)]
            for antecedent in antecedents:
                consequent = tuple([item for item in itemset if item not in antecedent])
                antecedent_support = sum([1 for transaction in transactions if set(antecedent).issubset(set(transaction))])
                both_support = sum([1 for transaction in transactions if set(antecedent + consequent).issubset(set(transaction))])
                try:
                    confidence = both_support / antecedent_support
                    if confidence >= min_confidence:
                        rules.append((antecedent, consequent))
                except ZeroDivisionError:
                    pass  # Handle division by zero error by skipping the rule
    return rules

# Get frequent itemsets
min_support = 2/len(transactions)
frequent_itemsets = apriori(transactions, min_support)
print(frequent_itemsets)
# Generate association rules
min_confidence = 0.75
rules = association_rules(frequent_itemsets, transactions, min_confidence)

# Print rules
for rule in rules:
    print(f"{rule[0]} => {rule[1]}")