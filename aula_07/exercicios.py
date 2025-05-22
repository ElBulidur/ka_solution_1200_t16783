"""
    Laboratório 1

    Escrever uma classe chamada Pessoa. Esta classe deve ter as propriedades:
        => Nome;
        => Idade;
        => Peso;
        => Altura.

    Definir também os seguintes métodos:
        => getDados(): usado para retornar os dados da pessoa;
        => setDados(): usado para atribuir todos os dados da pessoa;
        => get_csv(): usado para retornar os dados da pessoa separados por ponto-e-vírgula (;) com o propósito
        de gerar um arquivo no formato CSV (o arquivo não será contemplado neste exercício).

    Incluir também um construtor capaz de receber valores para todas as propriedades, porém sendo apenas o nome
    da pessoa obrigatório.
"""

class Pessoa:
    def  __init__(self, nome, idade=0, peso=None, altura=None):
        self.set_dados(nome, idade, peso, altura)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if len(nome) > 0:
            self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, p_altura):
        self.__altura = p_altura

    def get_dados(self):
        return f"Nome: {self.nome}, idade: {self.idade}, \
            peso: {"Não informado" if self.peso == None else self.peso}, \
                altura {"Não informado" if self.altura == None else self.altura}"
    
    def set_dados(self, nome: str, idade:int, peso:int, altura:float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

        return True
    
    def get_csv(self):
        return f"{self.nome};{self.idade};{self.peso};{self.altura}"
    
    def get_csv_02(self):
        return ';'.join(str(dado) for dado in self.get_dados())
    
julio = Pessoa("Julio")

# julio.set_dados()

# julio.nome = "Julio"
