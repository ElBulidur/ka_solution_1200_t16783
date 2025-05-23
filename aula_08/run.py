import unittest

def somar_dois_numeros(numero_01, numero_02):
    return numero_01 + numero_02 + 5


# assert somar_dois_numeros(10, 5) == 15, "O valor esperado é 15."
# print("Função esta ok.")

class TestesUnitarios(unittest.TestCase):

    def testar_somar(self):
        self.assertEqual(somar_dois_numeros(10, 5), 15, "O valor esperado é 15.")

if __name__ == "__main__":
    unittest.main()