num = cont = soma = 0
print('Digite [ 999 ] para parar.')
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, soma))
