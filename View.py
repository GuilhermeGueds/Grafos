from random import randint
from Grafo import Grafo
import time


def menu():
    entrada = 0
    while entrada < 1 or entrada >= 10 :
        entrada = int(input ("\n1 - inserir Vertice\n"
                          "2 - Inserir Aresta\n"
                          "3 - Remover Vertice\n"
                          "4 - Remover Aresta\n"
                          "5 - Verifica se Vertices são adjacentes\n"
                          "6 - Retorna elemento armazenado na aresta\n"
                          "7 - Retorna elemento armazenado no Vertice\n"
                          "8 - Retorna referencia para os 2 vertices finais da aresta\n"
                          "9 - Criar grafico\n"
                          "X - sair             -> "))
    return entrada


def Demonstracao1():

    grafo = Grafo()

    grafo.inserirVertice('A')
    grafo.inserirVertice('B')
    grafo.inserirVertice('C')
    grafo.inserirVertice('D')
    grafo.inserirVertice('E')
    grafo.inserirVertice('F')
    grafo.inserirVertice('G')
    grafo.inserirVertice('H')
    grafo.inserirVertice('I')
    grafo.inserirVertice('J')
    grafo.inserirVertice('K')
    grafo.inserirVertice('L')
    grafo.inserirVertice('M')
    grafo.inserirVertice('N')

    grafo.inseririAresta('A','B',randint(0,100))
    grafo.inseririAresta('B','C',randint(0,100))
    grafo.inseririAresta('C','D',randint(0,100))
    grafo.inseririAresta('D','E',randint(0,100))
    grafo.inseririAresta('E','F',randint(0,100))
    grafo.inseririAresta('F','G',randint(0,100))
    grafo.inseririAresta('G','H',randint(0,100))
    grafo.inseririAresta('H','I',randint(0,100))
    grafo.inseririAresta('I','J',randint(0,100))
    grafo.inseririAresta('J','K',randint(0,100))
    grafo.inseririAresta('K','L',randint(0,100))
    grafo.inseririAresta('L','M',randint(0,100))
    grafo.inseririAresta('M','N',randint(0,100))
    grafo.inseririAresta('N','A',randint(0,100))
    grafo.inseririAresta('A','L',randint(0,100))
    grafo.inseririAresta('C','F',randint(0,100))
    grafo.inseririAresta('F','J',randint(0,100))
    grafo.inseririAresta('E','N',randint(0,100))
    grafo.inseririAresta('H','L',randint(0,100))
    grafo.inseririAresta('I','M',randint(0,100))
    grafo.inseririAresta('D','L',randint(0,100))

    grafo.mostrarGrafo()
    time.sleep(2)
    grafo.BFS_Largura('A','G')


x = Demonstracao1()
