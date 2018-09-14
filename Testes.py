from Grafo import Grafo
grafo = {'a': {'b': 5, 'c': 4}, 'b': {'a': 5, 'c': 6, 'd': 8}, 'c': {'b': 6, 'd': 4}, 'd': {'b':8,'c':4} }

x = Grafo()

x.inserirVertice('a')
x.inserirVertice('b')
x.inserirVertice('c')
x.inserirVertice('d')

x.inseririAresta('a','b',5)
x.inseririAresta('a','c',4)
x.inseririAresta('b','c',5)
x.inseririAresta('b','d',5)

print(x.montarLista())