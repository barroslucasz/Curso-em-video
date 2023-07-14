from random import randint
from time import sleep

def sort(lista):
    print('Sorteando 5 números: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('FIM!')

def somapar(lista):
    soma =0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Os valores pares da lista {lista} é igual a: {soma}')


numeros = []
sort(numeros)
somapar(numeros)

# atividade realizada no dia 11dejul
