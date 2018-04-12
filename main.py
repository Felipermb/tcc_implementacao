from StellPlatesDataset import StellPlatesDataset
from AlgoritmoGenetico import AlgoritmoGenetico
from cromossomo import Cromossomo

from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation

class Main():
    ######################################################
    # recupera o fitness da arvore default
    stell_plates = StellPlatesDataset()
    clf = DecisionTreeClassifier()
    scores = cross_validation.cross_val_score(clf, stell_plates.data, stell_plates.target, cv=10, scoring='accuracy')
    acuracia = round(100*scores.mean(), 2)
    clf = clf.fit(stell_plates.data, stell_plates.target)
    treeObj = clf.tree_
    tamanho = treeObj.node_count

    arvore_default_fitness = (1/tamanho) + acuracia
    ######################################################
    
    ag = AlgoritmoGenetico()
    ag.imprimirCromossomos()

    for i in range(100):
        ag.operacao()
    
    print ("\n\n")

    ag.imprimirCromossomos()
