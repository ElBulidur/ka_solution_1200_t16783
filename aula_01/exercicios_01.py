'''
    Laboratório 1
    Escrever um programa em Python que solicite informações de três pessoas, como nome, idade, peso e altura.
    Apresentar na tela estas informações de modo que permaneçam alinhados verticalmente. Usar a formatação
    de interpolação.

'''

# print("===== PEGANDO DADOS DA PESSOA 01 =============")
# nome_01, idade_01 = input("Excreva o nome 01: "), input("Excreva a idade 01: ")
# peso_01, altura_01 = input("Excreva o peso 01: "), input("Excreva a altura 01: ")
pessoa_01 = [
    input("Excreva o nome 01: "), input("Excreva a idade 01: "),
    input("Excreva o peso 01: "), input("Excreva a altura 01: ")
]
print("")

print("===== PEGANDO DADOS DA PESSOA 02 ==========")
nome_02, idade_02 = input("Excreva o nome 02: "), input("Excreva a idade 02: ")
peso_02, altura_02 = input("Excreva o peso 02: "), input("Excreva a altura 02: ")
print("")
print("A"*50)
print("")
print("RESPOSTA")
print("")
print(f"Pessoa 01 => nome: {pessoa_01[0].capitalize()}, idade: {pessoa_01[1]} anos, peso: {pessoa_01[2]}kl e altura: {pessoa_01[3]}")
print(f"Pessoa 02 => nome: {nome_02}, idade: {idade_02} anos, peso: {peso_02}kl e altura: {altura_02}")
