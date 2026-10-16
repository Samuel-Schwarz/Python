# Exemplo - Três números em ordem crescente
# Aluno: SAmuel Schwarz
# Objetivo: Ler três números diferentes e mostrá-los em ordem crescente

# Pedindo os números ao usuário
n1 = int (input ("Digite um número: "))
n2 = int (input ("Digite um número: "))
n3 = int (input ("Digite um número: "))

# Decisão 1: O primeiro é maior
if n1 < n2 and n3:
    p1 = n1
    # A ordem dos outros
    if n2 < n3:
        p2 = n2
        p3 = n3
    else:
        p2 = n3
        p3 = n2
# Decisão 2: O segundo é maior
elif n2 < n3 and n1:
    p1 = n2
    # A ordem dos outros
    if n1 < n3:
        p2 = n1
        p2 = n3
    else:
        p2 = n3
        p3 = n1
# Decisão 3: O terceiro é maior
else:
    p1 = n3
    # A ordem dos outros
    if n2 < n1:
        p2 = n2
        p2 = n1
    else:
        p2 = n1
        p3 = n2

print (p1, p2, p3)