
print("="*50)
print("")

numero_01 = int(input("Digite o PRIMEIRO numero: "))
numero_02 = int(input("Digite o SEGUNDO numero: "))

op = input("Digite a OPERAÇÃO(+,-): ")

res = 0

if op == "+":
    res = numero_01 + numero_02
elif op == "-":
    res = numero_01 - numero_02
else:
    print("Infelizmente só aceitamos duas operações: +, -")

if op in ["+", "-"]:
    print(f"O resultado da operação {op} é: {res}")