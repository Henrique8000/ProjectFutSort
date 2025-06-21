"""
Sorteador de time de 5 pessoas (tirando goleiros) para 4 times

Estrutura dos times:
2-Bons
2-Medios
1-Ruim

Mudanças futuras:
-Programa pode gerar um modelo de tabela csv para o usuário preencher com o nome das pessoas que iram jogar e a
categoria de habilidade. O usuário dara de entrada no programa o arquivo csv que fará o tratamento dos dados para
realizar o sorteio.

-Modularizar mais o código

-Classe "Partida"?
"""

from random import choice


def main():
    lista_participantes = lista_de_jogadores()
    sorteio_de_times(lista_participantes)


def lista_de_jogadores():
    #Implementar com sets?
    jogadores_bons = ["Tavares", "Theo", "Zion", "Mario Gama", "Leonardo Miyashiro", "joao Rosario", "Kaue", "Kaiky"]
    jogadores_medios = ["J", "Perchi", "Luis", "Fabio", "Murilo", "Juan"]
    jogadores_ruins = ["Henrique", "Francisco", "Pedro Soares", "Vh", "Leo Vboas"]

    lista_com_todos = [jogadores_bons, jogadores_medios, jogadores_ruins]
    return lista_com_todos


def sorteio_de_times(lista_com_todos):
    nomes_ja_sorteados = set()

    lista_todos0 = lista_com_todos[0]
    lista_todos1 = lista_com_todos[1]
    lista_todos2 = lista_com_todos[2]

    n_time = 0
    indice = 0

    for k in range(4):

        l_times = []

        if len(lista_todos0) == 0:
            l_times.append("VAGA-VAZIA")

        else:
            for jb in range(2):
                jogador_sorteado = choice(lista_todos0)

                while jogador_sorteado in nomes_ja_sorteados:
                    jogador_sorteado = choice(lista_todos0)

                del lista_todos0[lista_todos0.index(jogador_sorteado)]  #só aceita inteiro
                nomes_ja_sorteados.add(jogador_sorteado)
                l_times.append(jogador_sorteado)

        if len(lista_todos1) == 0:
            l_times.append("VAGA-VAZIA")

        else:
            for jm in range(2):
                jogador_sorteado = choice(lista_todos1)

                while jogador_sorteado in nomes_ja_sorteados:
                    jogador_sorteado = choice(lista_todos1)

                del lista_todos1[lista_todos1.index(jogador_sorteado)]
                nomes_ja_sorteados.add(jogador_sorteado)
                l_times.append(jogador_sorteado)

        if len(lista_todos2) == 0:
            l_times.append("VAGA-VAZIA")

        else:
            for jr in range(1):
                jogador_sorteado = choice(lista_todos2)

                while jogador_sorteado in nomes_ja_sorteados:
                    jogador_sorteado = choice(lista_todos2)

                del lista_todos2[lista_todos2.index(jogador_sorteado)]
                nomes_ja_sorteados.add(jogador_sorteado)
                l_times.append(jogador_sorteado)

        n_time += 1
        indice += 1
        print(f"Time {n_time}: {l_times}")

    #print(f"\n{nomes_ja_sorteados}")


main()
