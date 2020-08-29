def menu():
    opcao = "9"
    while (opcao != 1 or opcao != 2):
        print("Bem-vindo ao jogo do NIM! Escolha:\n")
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato 2\n")

    if opcao == '1':
        print("Você escolheu uma partida isolada")
        return "1"
    else:
        print("Voce escolheu um campeonato!")
        return "2"



rodada = 1
print("**** Rodada ", rodada, "****")


n = 0
print("Quantas peças? ") # 3

m = 0
print("Limite de peças por jogada? ") 1



print("Computador começa!")



print("O computador tirou uma peça.")

print("Agora restam 2 peças no tabuleiro.")



Quantas peças você vai tirar? 2



Oops! Jogada inválida! Tente de novo.



Quantas peças você vai tirar? 1



Você tirou uma peça.

Agora resta apenas uma peça no tabuleiro.



O computador tirou uma peça.

Fim do jogo! O computador ganhou!



**** Rodada 2 ****



Quantas peças? 3

Limite de peças por jogada? 2



Voce começa!



Quantas peças você vai tirar? 2

Voce tirou 2 peças.

Agora resta apenas uma peça no tabuleiro.



O computador tirou uma peça.

Fim do jogo! O computador ganhou!



**** Rodada 3 ****



Quantas peças? 4

Limite de peças por jogada? 3



Voce começa!



Quantas peças você vai tirar? 2

Voce tirou 2 peças.

Agora restam 2 peças no tabuleiro.



O computador tirou 2 peças.

Fim do jogo! O computador ganhou!



**** Final do campeonato! ****



Placar: Você 0 X 3 Computador


O programa deve implementar:

def computador_escolhe_jogada(n, m):
    jogada = 0
    return jogada

jogada_computador = computador_escolhe_jogada(n, m)


def jogada_usuario(n, m):
    jogada = 0
    return jogada

jogada_usuario = usuario_escolhe_jogada(n, m)


    partida()

     que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.

Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no tabuleiro e qual é o máximo de peças a retirar em cada jogada.
