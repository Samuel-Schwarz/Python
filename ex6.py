# Exemplo - Compra na cantina
# Aluno: Samuel Schwarz
# Objetivo: Calcular o preço total e o troco de uma Compra

# Pede para o usuário o preço do produto
preco = float (input ("Digite o preço do produto: "))

# Pede para o usuário a quantidade de produtos comprados
quantidade = int (input ("Digite a quantidade: "))

# Calcula o valor total
valor_total = preco * quantidade

# Pede para o usuário o valor pago
valor_pago = float (input ("Digite o valor pago: "))

# Calcula o troco
troco = valor_pago - valor_total

# Informa os dados ao usuário
print ("Valor total: ", valor_total)
print ("Valor pago: ", valor_pago)
print ("Troco: ", troco)