from StellPlatesDataset import StellPlatesDataset
from sklearn import datasets, tree, cross_validation, metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# stell_plates = StellPlatesDataset()
# # iris = datasets.load_iris()
# # wine = datasets.load_wine()

# clf = DecisionTreeClassifier()

# X_train, X_test, y_train, y_test = train_test_split (stell_plates.data, stell_plates.target)


# scores = cross_validation.cross_val_score(clf, stell_plates.data, stell_plates.target, cv=10, scoring='accuracy')
# # print ("Cross-validated scores: ", scores)

# print ("Accuracy: " + str(round(100*scores.mean(), 2)) + "%")


# clf = clf.fit(stell_plates.data, stell_plates.target)

# # # Calcula a acuracia da fase de teste
# # print (clf.score(X_test,y_test) * 100)
# # # Retorna o tamanho da árvore
# treeObj = clf.tree_
# print (treeObj.node_count)

a = [1,2,3,4,5]

print (a[2:4])
