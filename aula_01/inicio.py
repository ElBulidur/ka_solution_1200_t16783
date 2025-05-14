# Comentário de uma linha.
# Outra linha

"""
    comentário
    em bloco
"""

'''
comentario em bloco
'''


# camelCase ou snack_case

# julioPereira => CamelCase
# julio_pereira => snack_case

# VARIÁVEIS

x = 45 # Variável inteira (int)
nome = "Julio" # Variável texto (string)
sobrenome = 'Pereira' # Variável texto (string)
altura = 7.2 #Variável real (float)
acabou = True # Variável boleana (bool)
compara = x > 20 # Variavel boleana (bool)

# print('====== VARIÁVEIS ==========')
# print('')

# print('x = ', x, ', tipo = ', type(x))
# print('nome = ', nome.upper(), ', tipo = ', type(nome))
# print('altura = ', altura, ', tipo = ', type(altura))
# print('acabou = ', acabou, ', tipo = ', type(acabou))
# print('compara = ', compara, ', tipo = ', type(compara))


# ATRIBUIÇÕES

x = 29

#multipla
v1 = v2 = v3 = 230

#sequencial
v1, v2, v3 = 230, 25, 4

username, password = "elbulidur", "bolaquadrada"



# OPERADORES
x = 100
y = 9

# MATEMÁTICOS (+, -, *, /)
soma = x + y
sub = x - y
div = x /  # Divisão real
mult = x * y

z = x % y # resto da divisão
w = x // y # divisão inteira


# print(div)
# print(z)
# print(w)
# print(9*11)

# RELACIONAIS (>, <, <=, >=, ==, !=)
x = 100
y = 9

x_e_maior_y = x > y
x_e_menor_y = x < y
x_e_igual_a_y = x == y
x_e_diferente_a_y = x != y


# LÓGICOS (and, or, not)
x = 100
y = 50

expressao_01 = x > y and x == 100
expressao_02 = x < y or x == 100
expressao_03 = not x < y

# print(expressao_03)

# SAÍDA DE DADOS e ENTRADA DE DADOS
print("======== CALCULADORA ==========")

try:
    numero_01 = float(input("Digite um número: ")) #castear
    numero_02 = float(input("Digite o segundo número: "))
    
    resultado = numero_01 + numero_02

    print("A soma dos números são: ", resultado)
except NameError:
    print("Erro de nome")
except ValueError as msg:
    print(f"erro de VALOR!!! Mensagem de erro: {msg}")

