cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print('Tente novamente')
    print(f'Você digitou o número {cont[numero]}')