# Exemplo - Ano bissexto
# Aluno: Samuel Schwarz
# Objetivo: Ler um ano e informar se ele é bissexto

# Pergunta o ano ao usuário
ano = int (input ("Digite um ano: "))

# Decisão 1: O ano é bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ("Bissexto")
# Decisão 2: O ano não é bissexto
else:
    print ("Não é bissexto")