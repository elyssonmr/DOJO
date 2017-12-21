# Definição de funções
def comparar_jogada (jogador1, jogador2):
    if jogador1 == "papel" and jogador2 == "tesoura":
        print("Jogador 2 ganhou com a Tesoura!!!")
        return
    if jogador1 == "pedra" and jogador2 == "papel":
        print("Jogador 2 ganhou com o Papel!!!")
        return
    if jogador1 == "tesoura" and jogador2 == "pedra":
        print("Jogador 2 ganhou com o Pedra!!!")
        return
    if jogador1 == "papel" and jogador2 == "pedra":
        print("Jogador 1 ganhou com o papel!!!")
        return
    if jogador1 == "pedra" and jogador2 == "tesoura":
        print("Jogador 1 ganhou com a Pedra!!!")
        return
    if jogador1 == "tesoura" and jogador2 == "papel":
        print("Jogador 1 ganhou com a Tesoura!!!")
        return
    if jogador1 == "papel" and jogador2 == "papel":
        print("Empate")
        return
    if jogador1 == "pedra" and jogador2 == "pedra":
        print("Empate")
        return
    if jogador1 == "tesoura" and jogador2 == "tesoura":
        print("Empate")
        return
    print("Jogada não implementada")


## Execução do programa ##
jogador1 = input("Jogador1 informe papel, pedra ou tesoura: ")
jogador2 = input("Jogador2 informe papel, pedra ou tesoura: ")

## Compara a Jogada para saber que vencedor ##
comparar_jogada(jogador1, jogador2)
