# BANCO DE DADOS

# CRUD (CREATE, READ, UPDATE, DELETE)
import mysql.connector

def conexao(msg=None):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password= "root",
            database="kasolution"
        )

        if msg:
            print("Conectado com sucesso")

        return conn

    except mysql.connector.Error as e:
        print(f"Erro ao conectar: {e}")


class DataBase:
    
    def get_conexao(self, msg=None):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password= "root",
                database="kasolution"
            )
            
            if msg:
                print("Conectado com sucesso")

            return conn

        except mysql.connector.Error as e:
            print(f"Erro ao conectar: {e}")


if __name__ == "__main__":
    # FUNÇÃO
    conexao(1)

    # CLASSE
    conn = DataBase()
    conn.get_conexao(1)