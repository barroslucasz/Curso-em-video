num1 = 0
num2 = 0
num3 = 0
lista1 = []
lista2 = []
lista3 = []
par = maior = soma = 0
for c in range(0,3):
    num1 = int(input(f'Digite um valor para [ 0, {c} ]: '))
    lista1.append(num1)
    if num1 % 2 == 0:
        par += num1
for c in range(0,3):
    num2 = int(input(f'Digite um valor para [ 1, {c} ]: '))
    lista2.append(num2)
    if num2 % 2 == 0:
        par += num2
for c in range(0,3):
    num3 = int(input(f'Digite um valor para [ 2, {c} ]: '))
    lista3.append(num3)
    if num3 % 2 == 0:
        par += num3
print('-='*20)
print(f'[ {lista1[0]:^5} ] [ {lista1[1]:^5} ] [ {lista1[2]:^5} ]')
print(f'[ {lista2[0]:^5} ] [ {lista2[1]:^5} ] [ {lista2[2]:^5} ]')
print(f'[ {lista3[0]:^5} ] [ {lista3[1]:^5} ] [ {lista3[2]:^5} ]')
print('-='*20)
print(f'A soma dos números pares é: {par}')
print(f'A soma da terceira coluna é: {lista1[2]+lista2[2]+lista3[2]}')
print(f'O maior valor da segunda linha é: {max(lista2)}')
# exercício realizado por mim!
# atividade feita no dia 01/07/2023