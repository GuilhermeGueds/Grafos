import ctypes
import sys


class Nodo():

    '''Construtor'''
    def __init__(self, elemento):
        self.__vertice = elemento.upper()
        self.__adjacentes = []

    '''seta o elemento do vertice'''
    def setVertice(self, elemento):
        self.__vertice = elemento.upper()

    '''retorna o vertice'''
    def getVertice(self):
        return self.__vertice

    def removeVertice(self):
        del self

    ''' seta na lista de adjacentes outro nodo e o seu peso'''
    def setAdjacentes(self, nodo, valor):
        self.__adjacentes.append({0:ctypes.cast( id(nodo), ctypes.py_object ).value, 1:valor})

    '''retorna uma adjacente do nodo 1 parametro é posiçao em que ele se encontra na listao 2º parametro é o elemto ou o peso '''
    def getAdjacentes(self, posicao, elemento):
        return self.__adjacentes[posicao].get(elemento)

    '''remove um adjacente da lista de nodo'''
    def removeAdjacentes(self, nodo, peso):
        for i in range(len(self.__adjacentes)):
            if nodo == self.getAdjacentes(i-1,0) and peso == self.getAdjacentes(i-1,1):
                self.__adjacentes.pop(i-1)

    '''remove um adjacente da lista de nodo'''
    def removeAdjacentes(self, nodo):
        for i in range(len(self.__adjacentes)):
            if nodo == self.getAdjacentes(i - 1, 0) :
                self.__adjacentes.pop(i - 1)

    '''retorna a quantidade de adjacentes que um nodo possui'''
    def quantidadeDeadjacentes(self):
        return len(self.__adjacentes)

    '''Mostra todas as adjaacentes de um nodo'''
    def mostrarTodosAdjacentes(self):
        print(self.getVertice(),"", end="")
        for i in range(len(self.__adjacentes)):
            print( "[", self.getAdjacentes(i,0), "-", self.getAdjacentes(i,1),"]","",end="")

    def pegarListaDeAdjacentes(self):
        lista = {}
        for i in range(len(self.__adjacentes)):
            lista[ self.getAdjacentes(i, 0)] = self.getAdjacentes(i, 1)
        return lista

'''a = Nodo('A')
b = Nodo('B')
c = Nodo('C')
d = Nodo('D')
e = Nodo('E')
f = Nodo('F')


a.setAdjacentes('B',10)
a.setAdjacentes('C',20)

a.mostrarTodosAdjacentes()

print("\n",a.pegarListaDeAdjacentes())

print("")
#print(b.quantidadeDeadjacentes())
#print(x.getAdjacentes(0,0))

#a.mostrarTodosAdjacentes()
#print(x.getAdjacentes)'''
