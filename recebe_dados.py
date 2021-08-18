def recebe_dados(nome, rep):
    arquivo = open(nome, 'r')
    linha = arquivo.readline()
    listaVA = linha.split(' ')
    num_vertice = int(listaVA[0])
    num_aresta = int(listaVA[1])
    G = representacao(rep, arquivo, num_vertice, num_aresta)

    arquivo.close()

    return num_vertice, num_aresta, G


def representacao(isMatriz, arquivo, num_vertice, num_aresta):
    if isMatriz == 1:
        matAdj = [[0 for i in range(num_vertice)] for i in range(num_vertice)]
        for j in range(num_aresta):
            linha = arquivo.readline()
            linha = linha.split(' ')
            origem = int(linha[0])
            destino = int(linha[1])
            peso = float(linha[2])
            matAdj[origem][destino] = peso
            matAdj[destino][origem] = peso
        return matAdj
    else:
        listaAdj = [[] for i in range(num_vertice)]
        for j in range(num_aresta):
            linha = arquivo.readline()
            linha = linha.split(' ')
            origem = int(linha[0])
            destino = int(linha[1])
            peso = float(linha[2])
            listaAdj[origem].append((destino, peso))
            listaAdj[destino].append((origem, peso))
        return listaAdj
