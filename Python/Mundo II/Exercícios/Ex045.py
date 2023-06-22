from random import randint
from time import sleep
print('======== VAMOS JOGAR JO KEN PO!!! ========')
print('')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogador = int(input('DIGITE SUA JOGADA: '))
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
pedra = 0
papel = 1
tesoura = 2
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!!')
sleep(1)
print('-='*15)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-='*15)
if jogador == computador:
    print('=== EMPATAMOS ===')
elif jogador == pedra and computador == tesoura:
    print('=== O JOGADOR GANHOU ===')
elif jogador == pedra and computador == papel:
    print('=== O COMPUTADOR GANHOU ===')
elif jogador == papel and computador == pedra:
    print('=== O JOGADOR GANHOU ===')
elif jogador == papel and computador == tesoura:
    print('=== O COMPUTADOR GANHOU ===')
elif jogador == tesoura and computador == papel:
    print('=== O JOGADOR GANHOU ===')
elif jogador == tesoura and computador == pedra:
    print('=== O COMPUTADOR GANHOU ===')
else:
    'OPÇÃO INVÁLIDA.'
