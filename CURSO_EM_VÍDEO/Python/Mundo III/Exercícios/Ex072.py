cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')
print('='*70)
print('DESCUBRA COMO SE ESCREVE POR EXTENSO UM NÚMERO ENTRE 0 E 20')
print('='*70)
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'O número {numero} por extenso é {cont[numero]}')
        print('='*70)
        while True:
            rep = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
            if rep == 'N':
                break
            elif rep == 'S':
                print('='*70)
                numero = int(input('Digite um número entre 0 e 20: '))
                print(f'O número {numero} por extenso é {cont[numero]}')
        break
print('--- FIM DO PROGRAMA ---')
