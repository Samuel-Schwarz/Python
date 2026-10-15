# Exemplo - Positivo, negativo ou zero
# Aluno: Samuel Schwarz
# Objetivo: Verifica qual das opções o número é

# Pergunta o número pro usuário
numero = float (input ("Digite um número: "))

# Decisão 1: Se o número for positivo
if numero > 0:
    print ("Número positivo")
# Decisão 2: Se o número for negativo
elif numero < 0:
    print ("Número negativo")
# Decisão 3: Se o número for 0
else:
    print ("O número é 0")