import recebe_dados
import algoritmos_construtivos

if __name__ == '__main__':
    dados = recebe_dados.recebe_dados('teste.txt', 2)
    G = dados[2]
    algoritmos_construtivos.vizinho_mais_proximo(G)