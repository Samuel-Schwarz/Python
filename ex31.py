# Exemplo - Tipo de triângulo
# Aluno: Samuel Schwarz
# Objetivo: Ler os três lados de um triângulo

# Perguntando os lados ao usuário
l1 = int (input ("Digite um dos lados: "))
l2 = int (input ("Digite um dos lados: "))
l3 = int (input ("Digite um dos lados: "))

# Decisão 1: Os lados não formam um triângulo
if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print ("Esses lados não formam um triângulo")
# Decisão 2: Os lados formam um triângulo
else:
    # Decisão 1: Equilátero
    if l1 == l2 and l1 == l3:
        print ("Equilátero")
    # Decisão 2: Isósceles
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print ("Isósceles")
    # Decisão 3: Escaleno
    else:
        print ("Escaleno")