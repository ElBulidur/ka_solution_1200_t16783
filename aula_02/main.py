# ESTRUTURA CONDICIONAIS

# Se nota é maior que 6.9 => APROVADO
# Se a nota é menor que 7 => REPROVADO


nota = 7.0

# if nota > 6.9:
#     print("APROVADO")
# else:
#     print("REPROVADO")


# print("APROVADO") if nota > 6.9 else print("REPROVADO")



# ====================================================
# Se nota menor 6 => REPROVADO
# Se a nota for menor 5.9 e menor 7 => RECUPERAÇÃO
# Se nota for maior que 6.9 => APROVADO


nota = 7

# USANDO ELIF
# if nota < 6:
#     print("REPROVADO")
# elif nota < 7:
#     print("RECUPERAÇÃO")
# else:
#     print("APROVADO")


# USANDO IF ANINHADO
# if nota < 7:
#     if nota < 6:
#         print("REPROVADO")
#     else:
#         print("RECUPERAÇÃO")
# else:
#     print("APROVADO")


# COLEÇÃO (MUTÁVEL ou IMUTÁVEL)
 
# LISTA
alunos = ["Julio", "Ana", "Gilberto"]
numeros = [2, 7.6, 5, 8]
dados_aluno_01 = ["Julio", 18, 89, 1.72, True]

# print(alunos)
# print(type(alunos))
# print(alunos[0])
# print(alunos[0:2])

temp = alunos[0]
alunos[0] = alunos[1]
alunos[1] = temp
# print(alunos)

# MÉTODOS(RETORNAR ou NÃO)
curso = ["Programando com Python", "8 aulas", "32 hrs"]
# print(f"BASE: {curso}")

# Append (NÃO RETORNA)
# curso.append("06 alunos") # ADICIONA O ELEMENTO NO FINAL DA LISTA

# Clear (NÃO RETORNA)
# curso.clear() # LIMPA A LISTA


# COPY (RETORNA)
# res = curso.copy() # FAZ UMA CÓPIA DA LISTA

# COUNT (RETORNA)
# res = curso.count("32 hrs") # QUANTAS VEZES O ELEMENTO REPETIU NA LISTA

# Sort (NÃO RETORNA)
# numeros.sort(reverse=True) # ordena a lista

#pop (RETORNA)
# res = curso.pop(0) # Extrair o elemento da lista

numeros = [1,5,3,7,9,3]

#remove
# res = numeros.remove(9)

# print(numeros)
# print(res)


dados_aluno_01 = ["Julio", 18, 89, 1.72, True]

# DICIONÁRIO
dados_aluno_01_dict = {
    "nome": "Julio",
    "Idade": 18,
    "Peso": 89,
    "Altura": 1.72,
    "Ativo": True,
    "Notas": [7, 8, 4.5, 9]
}

# TUPLA (IMUTÁVEL)
dados_aluno_01 = ["Julio", 18, 89, 1.72, True]
dados_aluno_02 = ("Julio", 18, 89, 1.72, True)

# print(dados_aluno_02)
dados_aluno_02[0] = "Ana"
print("=====")
# print(dados_aluno_02)


meses = ("Jan", "Fev", "")










