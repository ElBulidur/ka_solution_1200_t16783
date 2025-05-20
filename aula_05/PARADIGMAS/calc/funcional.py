print("="*50)
print("")

pegar_numero = lambda x: int(input(f"Digite o numero 0{x}: "))

op = input("Digite a OPERAÇÃO(+,-): ")

if op in ("+", "-"):
    res = pegar_numero(1) + pegar_numero(2) if op == "+" else pegar_numero(1) - pegar_numero(2)

    print(f"O resultador é: {res}")
else:
    print("Infelizmente só aceitamos duas operações: +, -")






