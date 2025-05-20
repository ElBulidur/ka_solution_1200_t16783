"""
    Laboratório 01

    Este programa representa um jogo para adivinhar números. Os passos ssão apresentados a seguir, com um 
    exemplo de uso:

        => O programa produz um número aleatório inteiro entre 1 e 100 (suponha: 49);
        => O programa pede para o usuário: "Informe um valor entre 0 e 100": 60;
        => Como o número informado é maior que o produzido, o programe pede: "Informe um valor entre 0 e 59" : 20;
        => Como o número informado é menor que o produzido, o programa pede: "Informe um valor entre 21 e 59";
        => No final, o programa apresenta o número de tentativas.

    Observação: se o usuário fornece um valor fora da faixa solicitada, conta como tentativa.

"""

# MÓDULOS
# LOOP DE REPETIÇÃO
# ENTRADA E SAÍDA DE DADOS
# OPERADORES


from random import randint as rdi

numero = rdi(1, 100)
tentativas = 0
minimo, maximo = 1, 100

while True:
    tentativas += 1
    numero_usuario = int(input(f"Informe um valor entre {minimo} e {maximo}: "))

    if numero_usuario < minimo or numero_usuario > maximo: 
        continue

    if numero_usuario < numero: 
        minimo = numero_usuario + 1
    elif numero_usuario > numero: 
        maximo = numero_usuario - 1
    else: 
        break

print(f"Parabens! O numero sorteado foi o {numero}")
print(f"Voce acertou em {tentativas} tentativas.")


from random import randint

def lab01():
    num_aleatorio = randint(1, 100)
    num = 0
    
    tentativas = 0
    min = 1
    max = 100
    while num != num_aleatorio:
        num = int(input(f'Informe um número entre {min} e {max}: '))
       
        if not (num > max or num < min):
            if num > num_aleatorio: max = num - 1
            else: min = num + 1
        tentativas += 1
    print(f'\nVocê venceu!!')
    print(f'Número de tentativas: {tentativas}')

if __name__ == '__main__':
    lab01()