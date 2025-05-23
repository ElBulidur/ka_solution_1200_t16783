from services.crud_bd import (
    criar_usuario, atualizar_usuario, deletar_usuario, 
    listar_usuarios, listar_usuario_pelo_id
)

from services.crud_bd import CrudCliente
from services.crud_api import CrudClienteAPI
import ipdb



# criar_usuario("Francisco", "biscoitinho", "francisco@email.com")

# usuarios = listar_usuarios()
# print(usuarios)



cliente = CrudCliente()

# ipdb.set_trace() # pare nesta linha para teste

# cliente.criar_usuario("Jackson", "boladeneve", "jackson@email.com")
# usuarios = cliente.listar_usuarios()

# print(usuarios)

api = CrudClienteAPI("https://65a8535f219bfa3718670926.mockapi.io/api_usuario")

conteudo = api.listar_usuarios()


# ipdb.set_trace() # pare nesta linha
input("Ao clicar em qualquer tecla e enter salvara no banco.")

for usuario in conteudo:
    cliente.criar_usuario(usuario['nm_usuario'], usuario['senha'], usuario['email'])