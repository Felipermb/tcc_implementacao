from cromossomo import Cromossomo
import random

class AlgoritmoGenetico():

    cromossomos = []

    def __init__(self):
        self.inicializarPopulacao()
        self.ordenarLista()

    def addCromossomo(self, individuo):
        self.cromossomos.append(individuo)

    def inicializarPopulacao(self):
        # Inicia a população com 20 cromossomos
        for i in range(0, 20):

            criterion = random.randint(0, 1)
            splitter = random.randint(0, 1)
            max_depth = random.randint(0, 50)
            min_samples_split = random.randint(1, 1000)
            min_samples_leaf = random.randint(1, 1000)
            min_weight_fraction_leaf = random.randint(0, 5)
            presort = random.randint(0, 1)

            # Organiza a variavel Max Depth
            if (max_depth < 10):
                stringMD = '0'+str(max_depth)
            else:
                stringMD = str(max_depth)

            # Organiza a varivel Min Samples Split
            if (min_samples_split < 10):
                stringMSS = '000'+str(min_samples_split)
            elif (min_samples_split < 100):
                stringMSS = '00'+str(min_samples_split)
            elif (min_samples_split < 1000):
                stringMSS = '0'+str(min_samples_split)
            else:
                stringMSS = '1000'

            # Organiza a variavel Min Samples Leaf
            if (min_samples_leaf < 10):
                stringMSL = '000'+str(min_samples_leaf)
            elif (min_samples_leaf < 100):
                stringMSL = '00'+str(min_samples_leaf)
            elif (min_samples_leaf < 1000):
                stringMSL = '0'+str(min_samples_leaf)
            else:
                stringMSL = '1000'
            
            # monta o cromossomo a partir dos valores aleatorios gerados
            ind = str(criterion) + str(splitter) + stringMD + stringMSS + stringMSL + str(min_weight_fraction_leaf) + str(presort)
            self.addCromossomo(Cromossomo(ind))

    def ordenarLista(self):
        # Ordena a lista pelo fitness (key = lambda cromossomo: cromossomo.fitness)
        listaOrdenada = sorted(self.cromossomos, key = lambda cromossomo: cromossomo.fitness, reverse = True)
        self.cromossomos = listaOrdenada
    
    def imprimirCromossomos(self):
        for i in range(0, len(self.cromossomos)):
            print ('Individuo: {} - Fitness: {}'.format(self.cromossomos[i].individuo, self.cromossomos[i].fitness))
    
    def operacao(self):
        # Seleciona os primeiros cromossomos, pois eles estão com o melhor fitness
        rand1 = random.randint(0, 19)
        rand2 = random.randint(0, 19)

        pai1 = self.cromossomos[rand1]
        pai2 = self.cromossomos[rand2]   

        # Realiza Crossover entre o Pai 1 e  o Pai 2
        individuofilho1 = pai1.individuo[0] + pai2.individuo[1] + pai1.individuo[2:4] + pai2.individuo[4:8] + pai1.individuo[8:12] + pai1.individuo[12] + pai2.individuo[13]
        individuofilho2 = pai2.individuo[0] + pai1.individuo[1] + pai2.individuo[2:4] + pai1.individuo[4:8] + pai2.individuo[8:12] + pai2.individuo[12] + pai1.individuo[13]

        individuofilho3 = pai1.individuo[0:8] + pai2.individuo[8:]
        individuofilho4 = pai2.individuo[0:8] + pai1.individuo[8:]

        individuofilho4 = self.mutacao(individuofilho4)

        filho1 = Cromossomo(individuofilho1)
        filho2 = Cromossomo(individuofilho2)
        filho3 = Cromossomo(individuofilho3)
        filho4 = Cromossomo(individuofilho4)

        self.cromossomos.append(filho1)
        self.cromossomos.append(filho2)
        self.cromossomos.append(filho3)
        self.cromossomos.append(filho4)
        self.ordenarLista()

        # Remove os dois ultimos 
        self.cromossomos = self.cromossomos[:-4]

    def mutacao(self, individuo):

        # i = random.randint(0,4)
        m = int(individuo[0])
        if( m == 0 ):
            list1 = list(individuo)
            list1[0] = '1'
            str1 = ''.join(list1)
            individuo = str1
        else:
            list1 = list(individuo)
            list1[0] = '0'
            str1 = ''.join(list1)
            individuo = str1

        m = int(individuo[1])
        if(m == 0):
            list1 = list(individuo)
            list1[1] = '1'
            str1 = ''.join(list1)
            individuo = str1
        else:
            list1 = list(individuo)
            list1[1] = '0'
            str1 = ''.join(list1)
            individuo = str1


        m = int(individuo[13])   
        if( m == 0 ):
            list1 = list(individuo)
            list1[13] = '1'
            str1 = ''.join(list1)
            individuo = str1
        else:
            list1 = list(individuo)
            list1[13] = '0'
            str1 = ''.join(list1)
            individuo = str1

        return individuo
