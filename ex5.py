# Exemplo - Minutos em horas
# Aluno: Samuel Schwarz
# Objetivo: Traduzir uma quantidade de minutos para horas

# Pede uma quanidade de tempo em minutos para o usuário
tempo = int (input ("Escreva uma quantidade de minutos: "))

# Calcula a quantidade de horas e minutos restantes
horas = tempo // 60
minutos = tempo % 60

# Informa o resultado aousuário
print (horas, "horas e", minutos, "minutos")

