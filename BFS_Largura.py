
def dijkstra(grafo, inicio, fim):
    caminho_mais_curto = {}
    predecessor = {}
    nodo_nao_vistos = grafo
    infinito = 9999999
    caminho = []

    for nodo in nodo_nao_vistos:
        caminho_mais_curto[nodo] = infinito
    caminho_mais_curto[inicio] = 0

    while nodo_nao_vistos:
        nodo_minimo = None
        for nodo in nodo_nao_vistos:
            if nodo_minimo is None:
                nodo_minimo = nodo
            elif caminho_mais_curto[nodo] < caminho_mais_curto[nodo_minimo]:
                nodo_minimo = nodo

        for nodo_filho, peso in grafo[nodo_minimo].items():
            if peso + caminho_mais_curto[nodo_minimo] < caminho_mais_curto[nodo_filho]:
                caminho_mais_curto[nodo_filho] = peso + caminho_mais_curto[nodo_minimo]
                predecessor[nodo_filho] = nodo_minimo
        nodo_nao_vistos.pop(nodo_minimo)

    nodo_atual = fim
    while nodo_atual != inicio:
        try:
            caminho.insert(0, nodo_atual)
            nodo_atual = predecessor[nodo_atual]
        except KeyError:
            print('caminho nao achado')
            break
    caminho.insert(0, inicio)
    if caminho_mais_curto[fim] != infinito:
        lista = []
        #print('Menor distancia é:  ' + str(caminho_mais_curto[fim]))
        #print('Caminho percorrido:  ' + str(caminho))
        lista.append(caminho_mais_curto[fim])
        lista.append(caminho)
        return lista

