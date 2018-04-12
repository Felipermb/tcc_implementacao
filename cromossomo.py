# Criado por Felipe Reis para usar na base de dados Stell_Plates
# Disponível em <https://www.openml.org/d/40982>

# Exemplo de Cromossomo
# 01351000100020
# 0 1 35 1000 1000 2 0

# criterion                 :  0 = 'gini' ||  1 = 'entropy'
# splitter                  :  0 = 'best' ||  1 = 'random'
# max_depth                 :  0 =  None  || [1 -> 50] (int)
# min_samples_split         : [1 -> 1000] (int)
# min_samples_leaf          : [1 -> 1000] (int)
# min_weight_fraction_leaf  : [0 -> 0.5] = (0 -> 5) * 0.1
# presort                   :  0 = True || 1 = False

from StellPlatesDataset import StellPlatesDataset
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets, cross_validation


class Cromossomo():
    individuo = ""
    fitness = 0
    acuracia = 0
    size = 0

    # Contrutor, seta o cromossomo individuo e calcula seu fitness
    def __init__(self, individuo):
        self.individuo = individuo
        self.calcularFitness()

    # Função para calcular o fitness do cromossomo
    #
    # A proposta de otimização é:
    # Obter maior valor de Acurácia e/ou Diminuir o tamanho da árvore final gerada
    def calcularFitness(self):
        stell_plates = StellPlatesDataset()  # Carrega o dataset a ser usado nos testes

        # Carrega o algoritmo de ML que será utilizado (No caso, árvore de decisão = DecisionTreeClassifier() )
        # AQUI, nós passaremos os parâmetros, pois é aqui que usamos o Cromossomo, para poder testa-lo e obter calcular seu fitnes
        cri = self.getCriterion()
        spl = self.getSplitter()
        max_d = self.getMax_depth()
        min_ss = self.getMin_samples_split()
        min_sl = self.getMin_samples_leaf()
        min_wfleaf = self.getMin_weight_fraction_leaf()
        pre = self.getPresort()

        clf = DecisionTreeClassifier(criterion=cri, splitter=spl, max_depth=max_d, min_samples_split=min_ss,
                                     min_samples_leaf=min_sl, min_weight_fraction_leaf=min_wfleaf, presort=pre)

        # Aplicaremos Cross Validation com fold = 10 para podermos calcular o fitness
        scores = cross_validation.cross_val_score(
            clf, stell_plates.data, stell_plates.target, cv=10, scoring='accuracy')

        self.acuracia = round(100*scores.mean())

        # Chama a função fit e realiza a montagem da árvore
        clf = clf.fit(stell_plates.data, stell_plates.target)

        # Retorna o tamanho da árvore
        treeObj = clf.tree_
        self.size = treeObj.node_count

        # como queremos diminuir a profundidade da árvore e aumentar a acuracia
        # usaremos 1/size para podermos com valor de aumento nos dois parâmetros dsa nossa função de calculo de fitness
        self.fitness = (1/self.size) + self.acuracia

    #######################################
    # Váriaveis do cromossomo

    def getCriterion(self):
        if(self.individuo[0] == '0'):
            return 'gini'
        else:
            return 'entropy'

    def getSplitter(self):
        if(self.individuo[1] == '0'):
            return 'best'
        else:
            return 'random'

    def getMax_depth(self):
        m = self.individuo[2] + self.individuo[3]
        m = int(m)
        if(m == 0):
            return None
        else:
            return m

    def getMin_samples_split(self):
        m = self.individuo[4] + self.individuo[5] + self.individuo[6] + self.individuo[7]
        return int(m)

    def getMin_samples_leaf(self):
        m = self.individuo[8] + self.individuo[9] + self.individuo[10] + self.individuo[11]
        return int(m)

    def getMin_weight_fraction_leaf(self):
        numero = self.individuo[12] 
        # Calcula o intervalo de 0 -> 0.5 | tendo seu limite inteiro (0 -> 5) * 0.1
        c = int(numero) * 0.1
        return c

    def getPresort(self):
        if(self.individuo[13] == '0'):
            return True
        else:
            return False
