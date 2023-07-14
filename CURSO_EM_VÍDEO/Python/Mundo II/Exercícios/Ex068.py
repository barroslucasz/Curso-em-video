from random import randint
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-=' * 20)
print('Pensei em um número...')
while True:
    computador = randint(0, 10)
    jogador = int(input('Agora digite o seu número: '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e eu pensei em {computador} totalizando {total}', end='')
    print(' que é PAR.' if total % 2 == 0 else ' que é ÍMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce ganhou!')
        else:
            print('Você perdeu!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('voce venceu')
        else:
            print('Você Perdeu!')
            break
    print('Pensei em um número...')
print('-=-=GAME OVER=-=-')