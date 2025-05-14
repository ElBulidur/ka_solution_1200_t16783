
'''
    Laboratório 2
    Suponha que em um caixa eletrônico existam cédulas disponíveis de 5, 10, 20 e 50 reais. Usando operações de
    divisão inteira e resto da divisão, escrever um programa que solicite ao usuário um valor para saque e, a partir
    deste valor, armazenar em variáveis e apresentar na tela a quantidade de cada cédula para compor o valor do
    saque.
    Obs.: Considerar neste exercício que os valores sejam sempre múltiplos de 5. Considerar também a menor
    quantidade possível de cédulas.

'''

# SOLICITAR UM VALOR PARA SAQUE
valor_para_saque = int(input("Coloque o valor que vc queira sacar (Apenas multiplo de 5): "))
# VERIFICAR SE É MULTIPLO DE 5
# print(valor_para_saque%5)

if valor_para_saque%5 == 0:
    c_50 = valor_para_saque//50 
    valor_para_saque = valor_para_saque%50 

    c_20 = valor_para_saque//20 
    valor_para_saque = valor_para_saque%20

    c_10 = valor_para_saque//10
    valor_para_saque = valor_para_saque%10

    c_5 = valor_para_saque//5
    valor_para_saque = valor_para_saque%5
    
    print(f"Você vai sacar: {c_50} cédula de 50, {c_20} cédulas de 20, \
{c_10} cédulas de 10 e {c_5} cédulas de 5 reais.")
else:
    print("O sistema só aceita multiplo de 5. Tente novamente!!!")

# VERIFICAR QTD CEDÚLAS DE 50


