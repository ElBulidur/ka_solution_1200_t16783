
class Curso:

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, p_descricao):
        self.__descricao = p_descricao

    @property
    def carga_horaria(self):
        return self.__carga_horaria
    
    @carga_horaria.setter
    def carga_horaria(self, p_horario):
        self.__carga_horaria = p_horario

    def linha(self):
        print(f"Curso {self.descricao}, com duraçao de {self.carga_horaria} horas.")
