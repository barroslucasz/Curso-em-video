valor = []
while True:
    valores = int(input('Digite um valor: '))
    if valor not in valor:
        valor.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado!')
    rep = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-='*15)
    if rep == 'N':
        break
    elif rep == 'S':
        print('-='*15)
print(f'Você digitou os valores: {sorted(valor)}')

# não consegui resolver o problema da repetição de números!
# exercício feito no dia 27/06/2023

# abaixo a resolução do guanabara:

