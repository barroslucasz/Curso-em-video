num = cont = soma = med = 0
print('Digite [ 999 ] para parar.')
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    med = soma/cont
    num = int(input('Digite um número: '))
print('Você digitou {} a soma entre eles é {} e a média é {}.'.format(cont, soma, med))

