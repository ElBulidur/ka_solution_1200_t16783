from .curso import Curso

class CursoEAD(Curso):
    @property
    def agenda(self):
        return self.__agenda
    
    @agenda.setter
    def agenda(self, p_agenda):
        self.__agenda = p_agenda

    def linha(self):
        print(f"Curso {self.descricao}, com duraçao de {self.carga_horaria} horas. Ministrado em EAD")