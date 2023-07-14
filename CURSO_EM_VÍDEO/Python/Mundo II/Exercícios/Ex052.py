num = int(input('Digite um Número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
#print('\n\033[mO número {} foi divisivel {} vezes.'.format(num, total))
if total == 2:
    print('\n\033[mESTE NÚMERO É PRIMO!')
else:
    print('\n\033[mESTE NÚMERO NÃO É PRIMO!')
