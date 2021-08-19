def vizinho_mais_proximo(lista):
    u = 0
    C = []
    #lista de vértices não visitados
    Q = [x for x in range(len(lista))]
    #adiciona o primeiro vertice a lista de vertices visitados
    C.append(0)
    Q.remove(u)

    while len(Q) != 0:
        min = float('inf')
        for i in lista[u]:
            vertice = i[0]
            peso = i[1]
            if peso <= min and vertice in Q:
                min = peso
                v = vertice
        C.append(v)
        Q.remove(v)

        u = v
    C.append(C[0])

    print(C)
