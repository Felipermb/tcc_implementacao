from StellPlatesDataset import StellPlatesDataset
from AlgoritmoGenetico import AlgoritmoGenetico
from cromossomo import Cromossomo

from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.metrics import accuracy_score

class Main():
    # ######################################################
    # Instancia a base de dados;
    dataset = StellPlatesDataset()

    # Aplicaremos a separação da base, sendo, 30% Teste e 70% Treinamento
    # para podermos calcular o fitnes
    X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.33, random_state=42)

    # Inicia a árvore de Decisão
    clf = DecisionTreeClassifier(random_state=0)

    scores = cross_validation.cross_val_score(clf, dataset.data, dataset.target, cv=10)
    acuracia = round(100*scores.mean(), 2)

    # Retorna o tamanho da árvore
    clf = clf.fit(dataset.data, dataset.target)
    treeObj = clf.tree_
    size = treeObj.node_count

    print("Valor Default = Acuracia: {} | Size: {}".format(acuracia, size))
    
    # ######################################################
    
    print("\n")

    ag = AlgoritmoGenetico(X_train, X_test, y_train, y_test)
    ag.imprimirCromossomos()

    for i in range(5):
        # ag.operacaoGigante()
        ag.operacao()
    
    print("\n\n")

    ag.imprimirCromossomos()


    
