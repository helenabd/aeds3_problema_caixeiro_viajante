
import time
import random

def calcula_custo_lista(S, listaAdj):
    custo = 0
    for i in range(len(S) - 1):
        u = S[i]
        v = S[i + 1]

        for j in listaAdj[u]:
            if v == j[0]:
                custo += j[1]

    return custo

def calcula_custo_matriz(S, matrizAdj):
    custo = 0
    for i in range(len(S) - 1):
        u = S[i]
        v = S[i + 1]
        custo += matrizAdj[u][v]

    return custo


def troca_lista(S, listaAdj, tempoDisponivel):
    s = time.time()
    cont = 0

    random.seed()

    while tempoDisponivel > 0:

        inicio = time.time()

        i1 = random.randint(1, len(S) - 2)
        i2 = random.randint(1, len(S) - 2)

        if i1 != i2:

            Sc = S.copy()

            Sc[i1], Sc[i2] = Sc[i2], Sc[i1]

            if calcula_custo_lista(Sc, listaAdj) < calcula_custo_lista(S, listaAdj):
                S = Sc

        fim = time.time()

        tempoDisponivel -= (fim - inicio)

        #Adicionar um contador para comparar a implementação usando lista e matriz de adj
        cont += 1

    e = time.time()

    tempo = e - s
    custo = calcula_custo_lista(S, listaAdj)

    return S, custo

def troca_matriz(S, matrizAdj, tempoDisponivel, custo):
    cont = 0

    random.seed()

    while tempoDisponivel > 0:

        inicio = time.time()

        index1 = random.randint(1, len(S) - 2)
        index2 = random.randint(1, len(S) - 2)

        if index1 != index2:
            if index1 > index2:
                index1, index2 = index2, index1

            Sc = S.copy()

            i = S[index1]
            j = S[index2]
            ant1 = S[index1-1]
            prox1 = S[index1+1]
            ant2 = S[index2-1]
            prox2 = S[index2+1]

            Sc[index1], Sc[index2] = Sc[index2], Sc[index1]

            if (index2 - index1) == 1:
                custo_troca = custo - matrizAdj[ant1][i] - matrizAdj[j][prox2] \
                              + matrizAdj[ant1][j] + matrizAdj[i][prox2]
            else:
                custo_troca = custo - matrizAdj[ant1][i] - matrizAdj[i][prox1] - matrizAdj[j][prox2] - matrizAdj[ant2][j] \
                          + matrizAdj[ant1][j] + matrizAdj[j][prox1] + matrizAdj[ant2][i] + matrizAdj[i][prox2]

            if custo_troca < custo:
                S = Sc.copy()
                custo = custo_troca

            cont += 1

        fim = time.time()
        tempoDisponivel -= (fim - inicio)

    return S, custo, cont


def twoOpt_matriz(S, matrizAdj, tempoDisponivel, custo):
    cont = 0

    random.seed()

    while tempoDisponivel > 0:

        inicio = time.time()

        i1 = random.randint(1, len(S) - 2)
        i2 = random.randint(1, len(S) - 2)

        if i1 != i2:
            if i1 > i2:
                i1, i2 = i2, i1

            Sc = S.copy()

            i = S[i1]
            j = S[i2]
            ant = S[i1-1]
            prox = S[i2+1]

            L = []
            for x in range(i1, (i2+1), +1):
                L.append(Sc[x])
            reverso = list(reversed(L))

            L = []
            for x in range(0, i1, +1):
                L.append(Sc[x])
            for x in range(len(reverso)):
                L.append(reverso[x])
            for x in range((i2+1), (len(Sc)), +1):
                L.append(Sc[x])

            custo_troca = custo - matrizAdj[ant][i] - matrizAdj[j][prox] + matrizAdj[ant][j] + matrizAdj[i][prox]

            if custo_troca < custo:
                S = L.copy()
                custo = custo_troca

        fim = time.time()
        tempoDisponivel -= (fim - inicio)

        #Adicionar um contador para comparar a implementação usando lista e matriz de adj
        cont += 1

    return S, custo, cont