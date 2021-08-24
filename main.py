import recebe_dados
import algoritmos_construtivos
import algoritmo_refinamento
import time

if __name__ == '__main__':
    dados = recebe_dados.recebe_dados('teste.txt', 1)
    G = dados[2]
    tInit = time.time()
    S = algoritmos_construtivos.vizinho_mais_proximo_matriz(G)
    custo = algoritmo_refinamento.calcula_custo_matriz(S, G)
    tAnd = time.time() - tInit
    #rota = algoritmo_refinamento.twoOpt_matriz(S, G, (20 - tAnd), custo)
    rota = algoritmo_refinamento.troca_matriz(S, G, (20 - tAnd), custo)
    print('%.2f ' %rota[1])
    print(rota[0])