#FUNÇÕES (FUNCIONALIDADES)

## RETORNA e NÃO RETORNA

def boas_vindas(): #NÃO RETORNA
    print("Seja vem vindo!")

# boas_vindas()

def boas_vindas_retorna(): # RETORNA
    return "Seja vem vindo! (Retornado)"

# res = boas_vindas_retorna()
# print(res)

# TEM PARAMETROS / NÃO TEM PARAMETRO
def boas_vindas_por_horario(): #NÃO RETORNA / NÃO TEM PARAMETRO

    hora = 19

    if hora < 12:
        print("Bom dia, ")
    elif hora < 18:
        print("Boa tarde, ")
    else:
        print("Boa noite, ")

# boas_vindas_por_horario()

def boas_vindas_por_horario_parametro(hora): #NÃO RETORNA / TEM PARAMETRO

    if hora < 12:
        print("Bom dia, ")
    elif hora < 18:
        print("Boa tarde, ")
    else:
        print("Boa noite, ")


# boas_vindas_por_horario_parametro(15)

def msg_bem_vindo_usuario(nome_usuario: str):
    print(f"Seja bem vindo, {nome_usuario.capitalize()}")

# msg_bem_vindo_usuario("julio")

def valor_total_produto(valor_produto, quantidade):
    return valor_produto * quantidade



# print(f"Você comprou 21 produtos por R$ 58,00 cada. Valor total {valor_total_produto(58.00, 21)}")


# PARAMETROS OPCIONAIS
def valor_com_desconto(valor, desconto=0):
    return valor - desconto

# res = valor_com_desconto(54, 12)

# print(res)


#LISTA DE PARAMETRO
def total_lista_produtos(*args):
    total_a_pagar = 0

    for x in args:
        total_a_pagar += x

    return total_a_pagar


res = total_lista_produtos(24, 45, 75, 45, 758)

# print(f"Total a pagar: {res}")

def calcular_taxas_impostos(valor: int, **kargs: dict):
    valor_ajustado = valor
    
    if kargs.get("INSS"):
        valor_ajustado =  valor_ajustado - kargs.get("INSS")
    if kargs.get("IPVA"):
        valor_ajustado =  valor_ajustado - kargs.get("IPVA")

    print(valor_ajustado)


# calcular_taxas_impostos(5000, {"IPVA": 120, "INSS": 150})
# calcular_taxas_impostos(5000, IPVA=150, INSS=9.0)


def tratar_nome(nome: str):
    return nome.upper(), True


res = tratar_nome("julio")

# print(res)


