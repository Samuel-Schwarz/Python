# Exemplo 6 - Pedra, papel e tesoura
# Aluno: Samuel Schwarz
# Objetivo: Verificar o vencedor de uma partida de pedra, papel e tesoura

# Perguntando as jogadas
j1 = input ("Digite a jogada do jogador 1: ")
j2 = input ("Digite a jogada do jogador 2: ")

# Decisão 1: Jogador 1 ganha
if j1 == "pedra" and j2 == "tesoura" or j1 == "tesoura" and j2 == "papel" or j1 == "papel" and j2 == "pedra":
    print ("Jogador 1 venceu!")
# Decisão 2: Jogador 2 ganha
elif j2 == "pedra" and j1 == "tesoura" or j2 == "tesoura" and j1 == "papel" or j2 == "papel" and j1 == "pedra":
    print ("Jogador 2 venceu!")
# Decisão 3: Empate
elif j1 == "pedra" and j2 == "pedra" or j1 == "tesoura" and j2 == "tesoura" or j1 == "papel" and j2 == "papel":
    print ("Empate")
# Decisão 4: Jogada inválida
else:
    print ("Jogada inválida")