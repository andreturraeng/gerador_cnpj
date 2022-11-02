from random import randint
from time import sleep


def formatar_cnpj(fmt):
    cnpj_formatado = f'{fmt[:2]}.{fmt[2:5]}.{fmt[5:8]}/{fmt[8:12]}-{fmt[12:15]}'
    return cnpj_formatado


def titulo(texto, n=40):
    print('-' * n)
    print(f'{texto:^{n}}')
    print('-' * n)


def gerador_cnpj():
    # Gerando os 12 prmeiros dígitos
    lista_cnpj = [randint(0, 9) for n in range(8)]
    for n in range(4):
        if n < 3:
            lista_cnpj.append(0)
        else:
            lista_cnpj.append(1)

    # Descobrir e adicionar o primeiro digito
    lista_verificadora1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    lista_resultado1 = [a * b for a, b in zip(lista_verificadora1, lista_cnpj)]
    soma1 = sum(lista_resultado1)
    if soma1 % 11 < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - (soma1 % 11)
    lista_cnpj.append(primeiro_digito)

    # Descobrir e adicionar o segundo digito
    lista_verificadora2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    lista_resultado2 = [a * int(b) for a, b in zip(lista_verificadora2, lista_cnpj)]
    soma2 = sum(lista_resultado2)
    if soma2 % 11 < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - (soma2 % 11)
    lista_cnpj.append(segundo_digito)

    # Convertendo lista em uma string
    lista_cnpj = [str(a) for a in lista_cnpj]
    cnpj = ''.join(lista_cnpj)

    return cnpj


# PROGRAMA PRINCIPAL
titulo('GERADOR DE CNPJ', 50)
qtd = int(input('Digite quantos CNPJs deseja gerar: '))
print('Aguarde enquanto geramos ' + ('o CNPJ...' if qtd == 1 else 'os CNPJs...'))
sleep(2)
print()
for n in range(qtd):
    print(formatar_cnpj(gerador_cnpj()))
    sleep(0.5)
print('\nFim!')
