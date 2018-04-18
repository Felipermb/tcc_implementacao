from StellPlatesDataset import StellPlatesDataset
from AlgoritmoGenetico import AlgoritmoGenetico
from cromossomo import Cromossomo

from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.metrics import accuracy_score

class Main():
    ######################################################
    # Inicia o dataset
    stell_plates = StellPlatesDataset()

    # Aplicaremos a separação da base, sendo, 30% Teste e 70% Treinamento
    # para podermos calcular o fitnes
    X_train, X_test, y_train, y_test = train_test_split(stell_plates.data, stell_plates.target, test_size=0.3)

    # Inicia a árvore de Decisão
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    y_predict = clf.predict(X_test)
    acuracia = accuracy_score(y_test, y_predict)
    acuracia = acuracia * 100
    size = clf.tree_.node_count

    print("Valor Default = Acuracia: {} | Size: {}".format(acuracia, size))
    ######################################################
    
    print("\n")

    ag = AlgoritmoGenetico(X_train, X_test, y_train, y_test)
    ag.imprimirCromossomos()

    for i in range(5000):
        # ag.operacaoGigante()
        ag.operacao()
    
    print("\n\n")

    ag.imprimirCromossomos()


    
