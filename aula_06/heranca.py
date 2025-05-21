from classes import curso_ead, curso_presencial
from services import utils_service as srv

curso_python_ead = curso_ead.CursoEAD()
curso_python_ead.agenda = "Hoje"
curso_python_ead.descricao = "JAVA"
curso_python_ead.carga_horaria = 50

curso_python_ead.linha()

# =========================================================================

curso_python_presencial = curso_presencial.CursoPresencial()
curso_python_presencial.checkin = True
curso_python_presencial.descricao = "JAVASCRIPT"
curso_python_presencial.carga_horaria = 20

curso_python_presencial.linha()

nome = "julio"

utils = srv.Utils()

nome_maiusculo = utils.retornar_maiusculo(nome)

print(nome_maiusculo)

