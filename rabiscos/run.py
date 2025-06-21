from random import choice


def main():
    l_geral = ["JG", "Henrique", "Dudu", "Gunther", "k10",
               "Mais preto", "Gustavo", "Murilo", "Igor", "Big",
               "Maia", "Luigi", "Saif", "Ghidini", "amg + preto"]

    ja_escolhido = []
    cont = 0

    for k in range(3):

        l_time = []
        for i in range(5):
            jogador: str = choice(l_geral)

            while jogador in ja_escolhido:
                jogador = choice(l_geral)

            ja_escolhido.append(jogador)
            l_time.append(jogador)
        cont += 1

        print(f"Time {cont} = {l_time}")


if __name__ == "__main__":
    main()
