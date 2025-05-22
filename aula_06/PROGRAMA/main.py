
def start():
    tela = input("Qual tela você quer acessar? ")

    if tela == "usuario":
        from views.usuario_view import UsuarioView

    
if __name__ == "__main__":
    start()