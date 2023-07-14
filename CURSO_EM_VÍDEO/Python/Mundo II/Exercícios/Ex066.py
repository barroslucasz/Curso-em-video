print('Digite um número abaixo ou digite [ 999 ] para parar o programa.')
soma = cont = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você digitou {cont} números.')
print(f'A soma é {soma}')
print('Acabou')