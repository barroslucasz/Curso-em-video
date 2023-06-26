num = [2, 5, 9, 1]
num[2] = 3 # troca determinado elemento
num.append(7) # adiciona elemento no fim
num.sort() # organiza em ordem
num.insert(2, 0) # insere elemento no lugar do outro
num.pop() # remove o ultimo elemento
num.remove(0) # elimina o primeiro elemento encontrado
print(num)
print(f'Essa lista tem {len(num)} elementos')
print('')

valores = []
valores.append(1)
valores.append(2)
valores.append(3)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Fim.')
print('')

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('')

a = [1,2,3,4]
b = a[:] # usando o dois pontos a lista B cria apenas uma cópia da lista A e não uma associação.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('Fim.')    
