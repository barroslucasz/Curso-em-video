valores = []
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não irei adicionar!!')
    rep = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-='*20)
    if rep == 'N':
        break
print(f'Você digitou os valores: {sorted(valores)}')

# não consegui resolver o problema da repetição de números!
# exercício feito no dia 27/06/2023

# abaixo a resolução do guanabara:

