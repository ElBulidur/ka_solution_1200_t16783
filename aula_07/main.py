# PERSINTENCIA

# try:
#     int("assdio")
# except Exception as e:
#     log = open("logs.log", "w")
#     log.write(f"Erro: {e}")
#     log.close()


alunos = ["Julio", "Marques", "Carlos", "Ana"]

# arquivo = open("alunos.txt", "w")

# arquivo.write("ALUNOS\n")
# for aluno in alunos:
#     arquivo.write(f"{aluno}\n")

# arquivo.close()

# LEITURA

arq = open("alunos.txt", "r")

# print( arq.read() ) # Ler o arquivo
# print( arq.read(-1) ) # Ler os caracteres
# print( arq.readable() ) # Verifica se pode ser lido.
# print( arq.readline() ) # Ler a primeira linha.
# print( arq.readlines() ) # Ler a primeira linha.

arq.close()
