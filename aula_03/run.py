# LISTA
lista = ["Julio", 18, 89, 1.72, True]

# TUPLA
tupla = ("Julio", 18, 89, 1.72, True)

# DICIONÁRIO
dicionario = {
    "nome": "Julio",
    "Idade": 18,
    "Peso": 89,
    "Altura": 1.72,
    "Ativo": True,
    "Notas": [7, 8, 4.5, 9]
}


# range()

dados_aluno = {}


# 0 => Nome: "julio"
# for i in range(len(lista)):
#     if i == 0:
#         dados_aluno["Nome"]= lista[i]
#     elif i == 1:
#         dados_aluno["Idade"]= lista[i]


# print(dados_aluno)

# print(len(lista))


dicionario = {
    "nome": "Julio",
    "Idade": 18,
    "Peso": 89,
    "Altura": 1.72,
    "Ativo": True,
    "Notas": [7, 8, 4.5, 9]
}

# INSERT INTO DICIONARIO (COL1, COL2, COL3) VALUES (VAL1, VAL2,VAL3)

sql = "INSERT INTO DICIONARIO ("


for x in dicionario.keys():
    if x == "Notas":
        sql = f"{sql}{x})  values ("
    else:
        sql = f"{sql}{x}, "

    # break

for x in dicionario.values():

    if x == list(dicionario.values())[-1]:
        sql = f"{sql}{str(x)})"
    else:
        sql = f"{sql}{x}, "

# print(sql)


sql1 = "INSERT INTO DICIONARIO "


colunas = "("
valores = "("

for x, y in dicionario.items():
    if x == "Notas":
        colunas = f"{colunas}{x})"
        valores = f"{valores}{y})"

        sql1 = f"{sql1}{colunas} values {valores}"
    else:
        colunas = f"{colunas}{x}, "
        valores = f"{valores}{y}, "

# print(sql1)


cliente = "julio cezar pereira"

nome_ajustado = ""


for nome in cliente.split(" "): 
    nome_ajustado =  f"{nome_ajustado} {nome.capitalize()}"
    

# print(nome_ajustado)


# WHILE

# x = 0 

# while x < 2:
#     print("Entrou!!!")
#     x = x + 1



# saque = int(input("Digite ovalor de saque(Somente multiplos de 5): "))


# while saque%5 != 0:
#     saque = int(input("Ops, deu ruim! Repita o valor ou coloque 0 para sair do programa: "))

#     if saque == 0:
#         break

# if saque == 0:
#     print("Até mais!!!")
# else:
#     print("continua o programa!!!")


from random import randint

tentativa = 0
numero_da_sorte = randint(1, 5)
numero = 0

while numero == 0:
    numero_usuario = int(input("Advinhe o número: "))

    if numero_usuario != numero_da_sorte:
        tentativa += 1
        print("Errou, tente de novo.")
    else:
        print("Acertouuuu!!!")
        numero = 1

    




