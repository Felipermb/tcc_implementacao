from StellPlatesDataset import StellPlatesDataset

from sklearn import datasets, tree, cross_validation, metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

import random

# # Instancia a base de dados;
# dataset = StellPlatesDataset()

# # Aplicaremos a separação da base, sendo, 30% Teste e 70% Treinamento
# # para podermos calcular o fitnes
# # X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.33, random_state=42)

# # Inicia a árvore de Decisão
# clf = DecisionTreeClassifier(random_state=0)

# scores = cross_validation.cross_val_score(clf, dataset.data, dataset.target, cv=10)
# print ("Accuracy: " + str(round(100*scores.mean(), 2)) + "%")

# # Retorna o tamanho da árvore
# clf = clf.fit(dataset.data, dataset.target)
# treeObj = clf.tree_
# print (treeObj.node_count,"\n")

novo = ''
criterion = random.randint(0, 1)
splitter = random.randint(0, 1)

novo += str(criterion)+str(splitter)

max_depth_bit1 = random.randint(0, 1)
max_depth_bit2 = random.randint(0, 1)
max_depth_bit3 = random.randint(0, 1)
max_depth_bit4 = random.randint(0, 1)
max_depth_bit5 = random.randint(0, 1)
max_depth_bit6 = random.randint(0, 1)

novo += str(max_depth_bit1) + str(max_depth_bit2) + str(max_depth_bit3) + \
    str(max_depth_bit4) + str(max_depth_bit5) + str(max_depth_bit6)

min_samples_split_bit1 = random.randint(0, 1)
min_samples_split_bit2 = random.randint(0, 1)
min_samples_split_bit3 = random.randint(0, 1)
min_samples_split_bit4 = random.randint(0, 1)
min_samples_split_bit5 = random.randint(0, 1)
min_samples_split_bit6 = random.randint(0, 1)
min_samples_split_bit7 = random.randint(0, 1)
min_samples_split_bit8 = random.randint(0, 1)
min_samples_split_bit9 = random.randint(0, 1)
min_samples_split_bit10 = random.randint(0, 1)

novo += str(min_samples_split_bit1) + str(min_samples_split_bit2) + str(min_samples_split_bit3) + str(min_samples_split_bit4) + str(min_samples_split_bit5) + \
    str(min_samples_split_bit6) + str(min_samples_split_bit7) + str(min_samples_split_bit8) + \
    str(min_samples_split_bit9) + str(min_samples_split_bit10)

min_samples_leaf_bit1 = random.randint(0, 1)
min_samples_leaf_bit2 = random.randint(0, 1)
min_samples_leaf_bit3 = random.randint(0, 1)
min_samples_leaf_bit4 = random.randint(0, 1)
min_samples_leaf_bit5 = random.randint(0, 1)
min_samples_leaf_bit6 = random.randint(0, 1)
min_samples_leaf_bit7 = random.randint(0, 1)
min_samples_leaf_bit8 = random.randint(0, 1)
min_samples_leaf_bit9 = random.randint(0, 1)
min_samples_leaf_bit10 = random.randint(0, 1)

novo += str(min_samples_leaf_bit1) + str(min_samples_leaf_bit2) + str(min_samples_leaf_bit3) + str(min_samples_leaf_bit4) + str(min_samples_leaf_bit5) + \
    str(min_samples_leaf_bit6) + str(min_samples_leaf_bit7) + str(min_samples_leaf_bit8) + \
    str(min_samples_leaf_bit9) + str(min_samples_leaf_bit10)

min_weight_fraction_leaf_bit1 = random.randint(0, 1)
min_weight_fraction_leaf_bit2 = random.randint(0, 1)
min_weight_fraction_leaf_bit3 = random.randint(0, 1)

novo += str(min_weight_fraction_leaf_bit1) + \
    str(min_weight_fraction_leaf_bit2) + str(min_weight_fraction_leaf_bit3)

presort = random.randint(0, 1)

novo += str(presort)

print(len(novo))

for i in range(32):
    print(i)
