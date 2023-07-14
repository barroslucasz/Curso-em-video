'''palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM')
for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for vogais in p:
        if vogais in 'AEIOU':
            print(vogais, end=' ')'''

# esse foi a resolução do guanabara abaixo irei fazer a minha resolução incluindo um input.

print('-='*20)
print('DETECTOR DE VOGAIS')
print('-='*20)
while True:
    palavras = str(input('Digite uma Palavra: ')).strip().upper()
    print(f'Na palavra {palavras} temos as vogais: ', end='')
    for vogais in palavras:
        if vogais in 'AEIOU':
            print(vogais, end=' ')
    while True:
        rep = str(input('\nDeseja continuar? [S/N] ')).strip().upper()[0]
        if rep == 'N':
            break
        elif rep == 'S':
            print('='*70)
            palavras = str(input('Digite uma Palavra: ')).strip().upper()
            print(f'Na palavra {palavras} temos as vogais: ', end=' ')
            for vogais in palavras:
                if vogais in 'AEIOU':
                    print(vogais, end=' ')
    break
print('----- FIM DO PROGRAMA -----')

# está aula aprendi no dia 25/06/2023!!