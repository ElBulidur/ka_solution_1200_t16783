# CRUD (CREATE, READ, UPDATE, DELETE)
import requests
import json


endpoint = "https://65a8535f219bfa3718670926.mockapi.io/api_usuario"


usuario = {
    "nm_usuario": "MANOELA",
    "senha": "DSFDUDF54",
    "email": "julio.pereira@email.com"
}

#  CREATE
def criar_usuario_api(usuario):

    resposta = requests.post(url=endpoint, data=usuario)

    if resposta.status_code == 201:
        print("Usuário criado com sucesso.")

dados_atualizar = {
    "nm_usuario": "carlos atualizado",
    "senha": "DSFDUDF54",
    "email": "novo_email@email.com"
}

# UPDATE
def atualizar_usuario_api(cd_usuario, dados_atualizar):

    url_atualizar = f"{endpoint}/{cd_usuario}"

    resposta = requests.put(url=url_atualizar, data=dados_atualizar)

    print("Usuario Atualizado com sucesso.")


# DELETE
def deletar_usuario_api(cd_usuario):

    url_deletar = f"{endpoint}/{cd_usuario}"

    resposta = requests.delete(url=url_deletar)

    if resposta.status_code == 200:
        print("Usuario deletado com sucesso.")
    elif resposta.status_code == 404:
        print("Usuario não encontrado.")

# READ
def listar_usuarios():
    resposta = requests.get(url=endpoint)

    conteudo = json.loads(resposta.content)

    return conteudo


class CrudClienteAPI:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    #  CREATE
    def criar_usuario_api(self, usuario):

        resposta = requests.post(url=self.endpoint, data=usuario)

        if resposta.status_code == 201:
            print("Usuário criado com sucesso.")

    # UPDATE
    def atualizar_usuario_api(self, cd_usuario, dados_atualizar):

        url_atualizar = f"{self.endpoint}/{cd_usuario}"

        resposta = requests.put(url=url_atualizar, data=dados_atualizar)

        print("Usuario Atualizado com sucesso.")

        return resposta.content

    # DELETE
    def deletar_usuario_api(self, cd_usuario):

        url_deletar = f"{self.endpoint}/{cd_usuario}"

        resposta = requests.delete(url=url_deletar)

        if resposta.status_code == 200:
            print("Usuario deletado com sucesso.")
        elif resposta.status_code == 404:
            print("Usuario não encontrado.")

    # READ
    def listar_usuarios(self):
        resposta = requests.get(url=self.endpoint)

        conteudo = json.loads(resposta.content)

        return conteudo




