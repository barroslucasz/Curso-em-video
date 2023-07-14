print('='*31)
print('      10 TERMOS DE UMA PA')
print('='*31)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + ( 10 - 1 ) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='→ ')
print('Acabou!')
