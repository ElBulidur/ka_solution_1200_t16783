# BANCO DE DADOS

# CRUD (CREATE, READ, UPDATE, DELETE)
import mysql.connector


def conexao():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password= "root",
            database="kasolution"
        )

        return conn

    except mysql.connector.Error as e:
        print(f"Erro ao conectar: {e}")

