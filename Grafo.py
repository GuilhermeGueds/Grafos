from Nodo import Nodo
from BFS_Largura import dijkstra
from graphviz import Graph
from random import randint

class Grafo():

    __vertice = []
    __aresta = []


    '''============================================  Vertices  ========================================================='''

    '''Insere vertice no grafo '''

    def inserirVertice(self, nodo):
        if not self.existeVertice(nodo):
            self.__vertice.append(Nodo(nodo))
        else:
            print("ja existe")

    def removerVertice(self, nodo):
        x = self.pegaVertice(nodo)
        if self.existeVertice(nodo):
            self.__removerArestas(nodo)  # Remove todas as arestas que contem o elemento
            x.removeVertice()  # Deveria apagar todas as referencias do elemento
            self.removeVerticeDoGrafico(nodo)
            self.__vertice.pop(self.pegaPosicaoVertice(nodo))  # apaga o vertice da lista de vertice

    '''Pega a posição que o vertice se encontra na lista'''

    def pegaPosicaoVertice(self, elemento):
        if self.existeVertice(elemento):
            for i in range(len(self.__vertice)):
                if (elemento == self.__vertice[i].getVertice()):
                    return i

    ''' Pega endereço de memoria de uma vertice do grafo'''

    def pegaVertice(self, nodo):
        if self.existeVertice(nodo):
            for i in range(len(self.__vertice)):
                if (nodo.upper() == self.__vertice[i].getVertice()):
                    return self.__vertice[i]  # .getVertice()

    '''Pega endereço de memoria de uma vertice do grafo'''
    '''def pegaElementoVertice(self, posicao):
        for i in range(len(self.__vertice)):
            return self.__vertice[posicao].getVertice()'''

    '''Verifica se a vertice existe'''
    def existeVertice(self, nodo):
        valida = False
        for i in range(len(self.__vertice)):
            if (nodo.upper() == self.__vertice[i].getVertice()):
                valida = True
                return True
        if valida == False:
            return False

    '''Mostra todos os vertices do grafo'''

    def mostrarTodosOsVertices(self):
        for i in range(len(self.__vertice)):
            print(self.__vertice[i].getVertice())

    def quantidadeDeVertice(self):
        return len(self.__vertice)

    '''===========================================   Areastas   ====================================================='''

    ''' insere uma aresta no grafo passando os dois pontos e o peso da aresta'''
    def inseririAresta(self, nodo1, nodo2, peso):
        if self.existeVertice(nodo1.upper()) and self.existeVertice(nodo2.upper()) and not self.arestaJaExiste(nodo1,nodo2,peso):
            self.__aresta.append({0 : nodo1.upper(), 1 : nodo2.upper(), 2 : peso})
            self.__inserirAdjacentes(nodo1,nodo2,peso)
        elif(not self.existeVertice(nodo1)):
            print('Vertice ', nodo1, " Não Existe")
        elif (not self.existeVertice(nodo1)):
            print('Vertice ', nodo2, " Não Existe")

    ''' remove aresta do grafo passando os 2 pontos e o peso pois pode haver 2 arestas com o mesmo ponto com pesos diferentes'''
    def removerAresta(self,nodo1,nodo2,peso):
        if self.existeVertice(nodo1.upper()) and self.existeVertice(nodo2.upper()) and  self.arestaJaExiste(nodo1,nodo2,peso):
            self.__aresta.pop(self.__pegaPosicaoDaAresta(nodo1, nodo2, peso))
            self.__removerAdjacentes(nodo1, nodo2, peso)
        elif(not self.existeVertice(nodo1)):
            print('Vertice ', nodo1, " Não Existe")
        elif (not self.existeVertice(nodo1)):
            print('Vertice ', nodo2, " Não Existe")

    '''Funcção especial para remover todas as arestas na qual o nodo foi excluido e exclui as referencias de adjacentes tambem'''
    def __removerArestas(self, nodo):
        z =[]
        if self.existeVertice(nodo.upper()):
            for i in range(len(self.__aresta)):
                if(self.__aresta[i].get(0) != nodo and self.__aresta[i].get(1) != nodo ):
                    z.append({0 : self.__aresta[i].get(0), 1 : self.__aresta[i].get(1), 2 : self.__aresta[i].get(2)})

            for j in range(len(self.__vertice)):
                x = self.__vertice[j]
                x.removeAdjacentes(nodo)
        self.__aresta = z

    ''' retorna uma aresta'''
    def pegaAresta(self,nodo1, nodo2, peso):
        if self.arestaJaExiste(nodo1,nodo2,peso) == True or self.arestaJaExiste(nodo2,nodo1,peso) == True:
            for i in range(len(self.__aresta)):
                if  self.__aresta[i].get(0) == nodo1 and self.__aresta[i].get(1) == nodo2 and self.__aresta[i].get(2) == peso:
                    return self.__aresta[i]
        else:
            print("Essa aresta não existe")

    '''Mostra todas as arestas do grafo'''
    def mostrarTodasAresta(self):
        for i in range(len(self.__aresta)):
            print("[",self.__aresta[i].get(0),"<-------->", self.__aresta[i].get(1),"]", self.__aresta[i].get(2) )


    '''Verifica se uma aresta ja existe no grafico'''
    def arestaJaExiste(self,nodo1,nodo2,peso):
        existe = False
        for i in range(len(self.__aresta)):
            if nodo1 == nodo2 or self.__aresta[i].get(0) == nodo1 and  self.__aresta[i].get(1) == nodo2 and  self.__aresta[i].get(2) == peso:
             existe = True
        return existe

    ''' Retorna a posiçao em que a aresta se encontra na lista de Arestas'''
    def __pegaPosicaoDaAresta(self, nodo1,nodo2,peso):
        if self.arestaJaExiste(nodo1,nodo2,peso) == True or self.arestaJaExiste(nodo2,nodo1,peso) == True:
            for i in range(len(self.__aresta)):
                if  self.__aresta[i].get(0) == nodo1 and self.__aresta[i].get(1) == nodo2 and self.__aresta[i].get(2) == peso:
                    return i


    def __pegaPosicaoDaAresta(self, nodo):
            for i in range(len(self.__aresta)):
                if  self.__aresta[i].get(0) == nodo or self.__aresta[i].get(1) == nodo:
                    return i
    '''==========================================   Adjacentes  ========================================================'''

    '''Insere adjacentes nos nodos passado por parametro '''
    def __inserirAdjacentes(self,nodo1,nodo2, peso):
        if self.existeVertice(nodo1) and self.existeVertice(nodo2):
            x = self.pegaVertice(nodo1)
            y = self.pegaVertice(nodo2)
            x.setAdjacentes(nodo2, peso)
            y.setAdjacentes(nodo1, peso)
        elif (not self.existeVertice(nodo1.upper())):
            print('Vertice ', nodo1, " Não Existe")
        elif (not self.existeVertice(nodo2.upper())):
            print('Vertice ', nodo2, " Não Existe")

    '''remove adjacentes dos nodos passado por parametro'''
    def __removerAdjacentes(self, nodo1, nodo2, peso):
        if self.existeVertice(nodo1) and self.existeVertice(nodo2):
            x = self.pegaVertice(nodo1)
            y = self.pegaVertice(nodo2)
            x.removeAdjacentes(nodo2, peso)
            y.removeAdjacentes(nodo1, peso)
        elif (not self.existeVertice(nodo1.upper())):
            print('Vertice ', nodo1, " Não Existe")
        elif (not self.existeVertice(nodo2.upper())):
            print('Vertice ', nodo2, " Não Existe")

    '''Mostra todas as adjacentes de um determinado Nodo'''
    def mostrarAdjacente(self,nodo):
        if self.existeVertice(nodo):
            x = self.pegaVertice(nodo)
            print(x.mostrarTodosAdjacentes())
        else:
            print('Vertice',"[",nodo,"]", "Não Existe")

    '''================================================   Graficos   ==================================================='''

    def mostrarGrafo(self):
        dot = Graph(filename='.\Imagens\Grafo', engine='sfdp', format='png', strict=True)
        dot.attr('node', shape='circle', color='lightblue', style='filled')
        dot.attr(bgcolor='white', label='Grafo', fontcolor='Black')
        for i in range(len(self.__vertice)):
            for j in range(self.__vertice[i].quantidadeDeadjacentes()):

                dot.edge(self.__vertice[i].getVertice(), self.__vertice[i].getAdjacentes( j, 0), label= str (self.__vertice[i].getAdjacentes( j, 1)))
        dot.view()


    def montarLista(self):
        lista = {}
        for i in range(self.quantidadeDeVertice()):
            lista[self.__vertice[i].getVertice()] = self.__vertice[i].pegarListaDeAdjacentes()

        return lista


    def BFS_Largura(self, inicio, fim):

        lista = dijkstra(self.montarLista(), inicio, fim)
        mensagem =    ("Menor distancia entre "  + str(lista[1][0])  + " e " + str(lista[1][len(lista[1])-1]) + " é : " + str(lista[0]))
        dot = Graph(filename='.\Imagens\Grafo', engine='sfdp', format='png', strict=True,)
        dot.attr('node', shape='circle', color='lightblue', style='filled')
        dot.attr(bgcolor='white', label= mensagem, fontcolor='Black')
        for i in range(len(self.__vertice)):
            for j in range(self.__vertice[i].quantidadeDeadjacentes()):
                dot.edge(self.__vertice[i].getVertice(), self.__vertice[i].getAdjacentes(j, 0),
                         label=str(self.__vertice[i].getAdjacentes(j, 1)))

        for i in range(len(lista[1])):
            if lista[1][i] != inicio and  lista[1][i] != fim:
                dot.node(lista[1][i] , color='gold')
            elif lista[1][i] == inicio:
                dot.node(lista[1][i], color='green')
            elif lista[1][i] == fim:
                dot.node(lista[1][i], color='green')
        for i in range(len(lista[1])-1):
            dot.edge( lista[1][i], lista[1][i+1],color='red')
        dot.view()



