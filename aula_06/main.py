# ENCAPSULAMENTO

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo   # PRIVADO

        # saldo => PUBLICO
        # _saldo => PROTEGIDO
        #  __saldo => PRIVADO

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False
    
    def ver_saldo(self):
        return self.__saldo


conta_julio = ContaBancaria("Julio Pereira", 580000)

conta_julio.sacar(3000)

# print( conta_julio.ver_saldo() )

# print(conta_julio._ContaBancaria__saldo)



class Automovel:
    
    # Marca
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, p_marca: str):
        if len(p_marca) == 0:
            raise ValueError("A marca foi fornecida incorretamente.")
        
        self.__marca = p_marca


    

    # Modelo
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, p_modelo: str):
        if len(p_modelo) == 0:
            raise ValueError("A modelo foi fornecido incorretamente.")
        
        self.__modelo = p_modelo.upper()

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, p_ano: int):
        if p_ano < 1960:
            raise ValueError("Este veículo é muito antigo.")
        self.__ano = p_ano

    def get_linha(self):
        linha = f" Carro: {self.marca}, modelo: {self.modelo}, ano: {self.ano}"
        print(linha)


    # ano


carro_01 = Automovel()

carro_01.marca = "Citroen"
carro_01.modelo = "C3"
carro_01.ano = 2025

print(carro_01.marca)

carro_01.get_linha()