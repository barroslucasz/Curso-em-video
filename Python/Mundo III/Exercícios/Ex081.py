valores = []
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    rep = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-='*20)
    if rep == 'N':
        break
print(f'Você digitou {len(valores)} elementos')
print(f'Os valores na ordem decrescente são: {sorted(valores, reverse=True)}')
if 5 in valores:
    print(f'O número 5 faz parte da lista')
else:
    print('O número 5 não foi digitado.')

# exercício resolvido com ajuda de outras atividades, mas feita sozinho por mim.
# exercício feito no dia 28/06/2023.
