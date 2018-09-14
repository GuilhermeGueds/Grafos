

#grafo = {'0': ['1','2'], '2': ['5', '6'], '3': [], '4':[], '5':[], '6':['7'],'7':[] }
grafo = {'a': {'b': 5, 'c': 4}, 'b': {'a': 5, 'c': 6, 'd': 8}, 'c': {'b': 6, 'd': 4}, 'd': {'b':8,'c':4} }





def DFS_Profundidade(grafo,inicio,fim):

    pilha = []
    visitado = []





DFS_Profundidade(grafo,'0','7')