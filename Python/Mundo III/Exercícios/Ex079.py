valor = []
while True:
    for cont in range(1):
        valor.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso!')
    rep = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-='*15)
    if rep == 'N':
        break
    elif rep == 'S':
        print('Valor adicionado com sucesso!')
        print('-='*15)
print(f'Você digitou os valores: {sorted(valor)}')

# não consegui resolver o problema da repetição de números!
# exercício feito no dia 27/06/2023

# abaixo a resolução do guanabara:

