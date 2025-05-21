"""
    Laboratório 1

    Tomar como base o cálculo do Imposto de Renda Pessoa Física. O acesso para este cálculo pode ser realizado
    através do link: https://www27.receita.fazenda.gov.br/simulador-irpf/
    Escrever uma função que receba como parâmetro o valor da base de cálculo do salário, e retorne o imposto de
    renda correspondente.
    Sugestão: Usar tuplas para armazenar as faixas de valores.

"""

# LOOP DE REPETIÇÃO
# ENTRADA/ SAIDA DE DADOS
# VARIÁVEIS

def calcular_irpf(salario):
    imposto = 0.0
    taxas = (0, 7.5, 15, 22.5, 27.5)
    valores = (0, 2428.80, 2826.65, 3751.05, 4664.68)
    base_para_calculo = salario - 607.20

    for i in range(4, -1, -1):
        if base_para_calculo > valores[i]:
            imposto += (base_para_calculo - valores[i]) * taxas[i] /100
            base_para_calculo = valores[i]


    print(f"Para o salário de R$ {salario}, terá que pagar o imposto de R$ {round(imposto, 2)}")

salario = float(input("Coloque o salário para o calculo: "))


calcular_irpf(salario)

    





