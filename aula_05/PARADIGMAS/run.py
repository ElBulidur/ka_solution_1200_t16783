# PROCEDURAL

total = 0
numero_01 = 15
numero_02 = 42

total = numero_01 + numero_02
total_02 = numero_01 + 23

# print(f"PROCEDURAL: {total}")

# FUNCIONAL

total = lambda x,y: x + y
total = lambda x: x + 23

# print(f"FUNCIONAL: {total(15,42)}")

# OOP (ABSTRAÇÃO - OBJETO[ATRIBUTOS, METODOS])

# ABSTRAÇÃO
class Total:
    def __init__(self):
        self.numero_01 = 0
        self.numero_02 = 0
        self.total = 0

    def soma_numeros(self):
        self.total = self.numero_01 + self.numero_02


# print(f"CLASSE: {Total}")

# print(f"OBJETO: {Total()}")

# print(f"ATRIBUTO: {Total().numero_01}")

total = Total()
total.numero_01 = 15
total.numero_02 = 45
total.soma_numeros()

print(total.total)

total_02 = Total()
total_02.numero_01 = 15
total_02.numero_02 = 23
total_02.soma_numeros()


