num1 = 0
num2 = 0
num3 = 0
lista1 = []
lista2 = []
lista3 = []
for c in range(0,3):
    num1 = int(input(f'Digite um valor para [ 0, {c} ]: '))
    lista1.append(num1)
for c in range(0,3):
    num2 = int(input(f'Digite um valor para [ 1, {c} ]: '))
    lista2.append(num2)
for c in range(0,3):
    num3 = int(input(f'Digite um valor para [ 2, {c} ]: '))
    lista3.append(num3)
print('-='*30)
print(f'[ {lista1[0]:^5} ] [ {lista1[1]:^5} ] [ {lista1[2]:^5} ]')
print(f'[ {lista2[0]:^5} ] [ {lista2[1]:^5} ] [ {lista2[2]:^5} ]')
print(f'[ {lista3[0]:^5} ] [ {lista3[1]:^5} ] [ {lista3[2]:^5} ]')
print()
print()

# resolvi está atividade sozinho.
# atividade realizada no dia 30/06/2023
# abaixo segue a resolução do guanabara.

print('-=-=-= Resolução do Guanabara: -=-=-=')
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
    