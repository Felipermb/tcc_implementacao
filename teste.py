from StellPlatesDataset import StellPlatesDataset
from sklearn import datasets, tree, cross_validation, metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

stell_plates = StellPlatesDataset()
# iris = datasets.load_iris()
wine = datasets.load_breast_cancer()

# clf = DecisionTreeClassifier(min_samples_split=1000)

# X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3)


# scores = cross_validation.cross_val_score(
#     clf, wine.data, wine.target, cv=10, scoring='accuracy')
# # print ("Cross-validated scores: ", scores)

# print ("Accuracy: " + str(round(100*scores.mean(), 2)) + "%")

# clf = clf.fit(wine.data, wine.target)

# # # Calcula a acuracia da fase de teste
# # print (clf.score(X_test,y_test) * 100)
# # # Retorna o tamanho da árvore
# treeObj = clf.tree_
# print (treeObj.node_count,"\n")


# X_train, X_test, y_train, y_test = train_test_split(
#     stell_plates.data, stell_plates.target, test_size=0.3)

# clf2 = DecisionTreeClassifier()
# clf2 = clf2.fit(X_train, y_train)

# y_predict = clf2.predict(X_test)
# ac = accuracy_score(y_test, y_predict)
# print ("Acuracia: ",ac)
# # Calcula a acuracia da fase de teste
# print (clf2.score(X_test,y_test) * 100)

# treeObj = clf2.tree_
# print (treeObj.node_count)
teste = ['1','23','4','5','6','7']
for ind in teste:
    print(ind)
    if(ind == '4'):
        print("entrou")
        break
