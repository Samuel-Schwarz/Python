# Exemplo - Calculadora
# Aluno: Samuel Schwarz
# Objetivo: Ler dois números e um operador (+, -, * ou /) e mostrar o resultado da operação

# Pedindo os números ao usuário
n1 = int (input ("Digite um número: "))
n2 = int (input ("Digite um número: "))

# Pedindo o operador
op = input ("Digite a operação (+, -, *, /): ")

# Decisão 1 e 2: Adição
if op == "+":
    print ("Resultado:", n1+n2)
else:
    # Decisão 1 e 2: Subtração
    if op == "-":
        print ("Resultado:", n1-n2)
    else:
        # Decisão 1 e 2: Multiplicação
        if op == "*":
            print ("Resultado:", n1*n2)
        else:
            # Decisão 1 e 2: Multiplicação
            if op == "/":
                # Decisão 1: O divisor é 0
                if n2 == 0:
                    print ("Erro: divisão por zero")
                # Decisão 2: O divisor não é 0
                else:
                    print ("Resultado:", n1/n2)
            # Decisão 2: Nenhuma operação
            else:
                print ("Operador inválido")