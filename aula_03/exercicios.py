"""

    Laboratório 1

    Escrever um programa que solicite ao usuário:
    => O nome de um funcionário;
    => Seu salário.

    Se o salário for superior a R$ 5.000,00 ele terá um desconto de 10%.
    No final, apresentar:
    => O nome do funcionário;
    => O salário bruto;
    => O valor do desconto;
    => O salário líquido.

"""
# Resposta
# funcionario = input("Escreva o nome do funcionário: ")
# salario = float(input("Escrevao o salário: "))

# desconto = 0

# if salario > 5000: desconto = (salario - 5000)*0.1

# salario_liquido = salario - desconto

# print("="*50)
# print("")
# print(f"Nome do funcionario: {funcionario}")
# print(f"Salário bruto: {round(salario, 2)}")
# print(f"Desconto: {desconto:.2f}")
# print(f"Salário liquido: {format(salario_liquido, ".2f")}")





"""

    Laboratório 1

    Em um clube, o valor da entrada varia de acordo com a idade do associado.
    Os critérios são:

    => Até 17 anos - R$ 50,00;
    => Entre 18 e 59 anos - R$ 60,00;
    =. A partir de 60 anos - R$ 20,00.

    O programa deve apresentar o nome do associado e o valor do ingresso a ser pago.

"""
# Resposta
associado = "Julio" #input("Coloque o seu nome: ")
idade = int(input("Coloque sua idade: "))

# valor_ingresso = 50

# if idade > 17 and idade < 60: valor_ingresso = 60
# if idade > 59: valor_ingresso = 20


# if idade < 18: valor_ingresso = 50
# elif idade > 17 and idade < 60: valor_ingresso = 60
# else: valor_ingresso = 20

if idade < 60:
    if idade < 18: valor_ingresso = 50
    else: valor_ingresso = 60
else: valor_ingresso = 20

print(f"Associado: {associado}")
print(f"Valor do ingresso: {valor_ingresso}")

