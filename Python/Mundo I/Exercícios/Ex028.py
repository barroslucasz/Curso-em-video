from random import randint
from time import sleep
computador = randint(0,5)
print('--==--'*20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar!')
print('--==--'*20)
print('Pensando...')
sleep(2)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
if jogador == computador:
    print('Você Acertou!! Eu tinha pensado no número {} mesmo.'.format(computador))
else:
    print('Você errou! Eu pensei em {} e você em {}'.format(computador, jogador))
    