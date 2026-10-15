# Exemplo - Divisão segura
# Aluno: Samuel Schwarz
# Objetivo: Fazer uma divisão, bloqueando o número 0

# Pede ao usuário que defina os valores da divisão
dividendo = float (input ("Digite o dividendo: "))
divisor = float (input ("Digite o divisor: "))

# Realiza a divisão
resultado = dividendo / divisor

# Decisão 1: Se o divisor for 0
if divisor == 0:
    print ("Erro: não existe divisão por 0")
# Decisão 2: Se o divisor for diferente de 0
else:
    print ("Resultado: ", resultado)