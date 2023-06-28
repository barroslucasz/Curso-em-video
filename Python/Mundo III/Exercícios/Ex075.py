num = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')), int(input('Digite o 3º número: ')), int(input('Digite o 4º número: ')))
print(f'Você digitou os números: {num}')
if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vezes')
else:
    print('O número 9 não foi digitado.')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(num.)+1}')
else:
    print('O número 3 não foi digitado.')
for n in num:
    if n % 2 == 0:
        print(f'Os números pares digitados foram: {n}', end=' ')
    else:
        print('Nenhum número PAR foi digitado.', end=' ')

# não consegui resolver o problema da repetição do resultado dos números pares.