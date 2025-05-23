
from aula_08.database.db import conexao, DataBase
# CRUD (CREATE, READ, UPDATE, DELETE)

## nome, senha, email

# CREATE
def criar_usuario(usuario, senha, email):

    # sql
    sql = "INSERT INTO tb_usuario (nm_usuario, senha, email) VALUES (%s, %s, %s)"

    # conexão
    conn = conexao()

    # Cursor
    cursor = conn.cursor()

    # Executar o sql
    cursor.execute(sql, [usuario, senha, email])


    # COMMITAR
    conn.commit()

    # Fechar conexão
    conn.close()

    print("Usuario criado com sucesso.")

# UPDATE
def atualizar_usuario(cd_usuario, usuario, senha, email):

    # sql
    sql = "UPDATE tb_usuario SET nm_usuario=%s, senha=%s, email=%s WHERE cd_usuario=%s"
    cd_usuario = 2
    valores = [usuario, senha, email, cd_usuario]

    # conexao
    conn = conexao()

    # Cursor
    cursor = conn.cursor()

    # Executar sql
    cursor.execute(sql, valores)

    if cursor.rowcount:
        # commitar
        conn.commit()
        conn.close()
        print("Usuário atualizado com sucesso!!!")
    else:
        conn.close()
        print("Não foi possível entcontre este usuario.")

# DELETE
def deletar_usuario(cd_usuario):

    # sql
    sql = "DELETE FROM tb_usuario WHERE cd_usuario=%s"

    # conexão
    conn = conexao()

    # Curso
    cursor = conn.cursor()

    # Executar sql
    cursor.execute(sql, [cd_usuario])

    if cursor.rowcount:
        # commitar
        conn.commit()
        conn.close()
        print("Usuario deletado com sucesso.")
    else:
        conn.close()
        print("Não foi possível entcontre este usuario.")

#READ
def listar_usuarios():

    # sql
    sql = "SELECT * FROM tb_usuario"

    # Conexão
    conn = conexao()

    # Curso
    cursor = conn.cursor()

    # Executar sql
    cursor.execute(sql)

    usuarios = []


    for linha in cursor:
        usuarios.append(linha)

    return usuarios

    # Fechar a conexão
    conn.close()

def listar_usuario_pelo_id(cd_usuario):
    # sql
    sql = "SELECT * FROM tb_usuario WHERE cd_usuario=%s"

    # Conexão
    conn = conexao()

    #Cursor
    cursor = conn.cursor()

    # executar sql
    cursor.execute(sql, [cd_usuario])

    registro = cursor.fetchone()

    if registro:
        return registro
    else:
        print("Não foi possível entcontre este usuario.")

    conn.close()


class CrudCliente(DataBase):
    def __init__(self):
        self.conn = None

    def commit_close(self):
       # COMMITAR
        self.conn.commit()

        # Fechar conexão
        self.conn.close()
     
    # CREATE
    def criar_usuario(self, usuario, senha, email):

        # sql
        sql = "INSERT INTO tb_usuario (nm_usuario, senha, email) VALUES (%s, %s, %s)"

        self.conn = self.get_conexao()

        # Cursor
        cursor = self.conn.cursor()

        # Executar o sql
        cursor.execute(sql, [usuario, senha, email])
        
        # Registrar
        self.commit_close()

        print("Usuario criado com sucesso.")

    # UPDATE
    def atualizar_usuario(self, cd_usuario, usuario, senha, email):

        # sql
        sql = "UPDATE tb_usuario SET nm_usuario=%s, senha=%s, email=%s WHERE cd_usuario=%s"
        cd_usuario = 2
        valores = [usuario, senha, email, cd_usuario]

        # conexao
        self.conn = self.get_conexao()

        # Cursor
        cursor = self.conn.cursor()

        # Executar sql
        cursor.execute(sql, valores)

        if cursor.rowcount:
            # Registrar
            self.commit_close()
            print("Usuário atualizado com sucesso!!!")
        else:
            self.conn.close()
            print("Não foi possível entcontre este usuario.")

    # DELETE
    def deletar_usuario(self, cd_usuario):

        # sql
        sql = "DELETE FROM tb_usuario WHERE cd_usuario=%s"

        # conexão
        self.conn = self.get_conexao()

        # Curso
        cursor = self.conn.cursor()

        # Executar sql
        cursor.execute(sql, [cd_usuario])

        if cursor.rowcount:
            # Registrar
            self.commit_close()
            print("Usuario deletado com sucesso.")
        else:
            self.conn.close()
            print("Não foi possível entcontre este usuario.")

    #READ
    def listar_usuarios(self):

        # sql
        sql = "SELECT * FROM tb_usuario"

        # Conexão
        self.conn = self.get_conexao()

        # Curso
        cursor = self.conn.cursor()

        # Executar sql
        cursor.execute(sql)

        usuarios = []


        for linha in cursor:
            usuarios.append(linha)
            
        # Fechar a conexão
        self.conn.close()

        return usuarios


    def listar_usuario_pelo_id(self, cd_usuario):
        # sql
        sql = "SELECT * FROM tb_usuario WHERE cd_usuario=%s"

        # Conexão
        self.conn = self.get_conexao()

        #Cursor
        cursor = self.conn.cursor()

        # executar sql
        cursor.execute(sql, [cd_usuario])

        registro = cursor.fetchone()

        if registro:
            return registro
        else:
            print("Não foi possível entcontre este usuario.")

        self.conn.close()
