class Calc:
    def __init__(self):
        self.numero_01 = 0
        self.numero_02 = 0

        self.realizar_operacao()

    def realizar_operacao(self):
        op = input("Digite a OPERAÇÃO(+,-): ")

        if op in ("+", "-"):
            self.numero_01 = int(input("Digite o PRIMEIRO numero: "))
            self.numero_02 = int(input("Digite o SEGUNDO numero: "))

            if op =="+":
                res = self.numero_01 + self.numero_02
            else:
                res = self.numero_01 - self.numero_02

            print(f"O resultado é: {res}")
        else:
            print("Infelizmente só aceitamos duas operações: +, -")


Calc()
