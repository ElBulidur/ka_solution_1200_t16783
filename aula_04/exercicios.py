"""
    Laboratório 1
    Criar um programa que utilize uma estrutura de repetição for. Nesta estrutura, o usuário deverá fornecer 5 nomes
    a serem adicionados em uma lista. No final, apresentar os nomes em ordem crescente.
    
    => O que vai aplicar neste exercício:
        - list
        - Input()
        - for
        - print()

"""

# lista_produtos = list()

# for x in range(5):
#     produto = input(f"Digite o {x+1}º produto: ")
#     lista_produtos.append(produto)

# lista_produtos.sort()

# for produto in lista_produtos:
#     print(produto)


# frutas = [input(f"Digite a {x+1}ª fruta: ") for x in range(3)]

# frutas.sort()

# print(frutas)

"""

    Laboratório 2
    Neste laboratório, uma lista de 100 números será criada de forma aleatória, ou seja, os elementos serão números
    aleatórios.
    Escrever o programa de forma a exibir E adicionar em uma lista, apenas os valores gerados que sejam maiores que
    10.

        => O que vai aplicar neste exercício:
            - random (from random import randint)
            - list
            - for
            - print()

"""
from random import randint as rdi

lista_numeros = []

# for x in range(10000):
#     numero = rdi(1, 100)
#     if numero > 10:
#         # print(f"Maior de 10: {numero}")
#         lista_numeros.append(numero)

# FOR ANINHADO
# lista_numeros = [ y for y in [rdi(1, 100) for x in range(1, 100)] if y >10 ]


# print(f"Foram gerados {len(lista_numeros)} numeros maiores que 10: {lista_numeros}")



