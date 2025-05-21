from .curso import Curso

class CursoPresencial(Curso):
    @property
    def checkin(self):
        return self.__checkin
    
    @checkin.setter
    def checkin(self, p_checkin):
        self.__checkin = p_checkin
    
    def linha(self):
        super().linha()
        print(f"Ministrado PRESENCIAL")
