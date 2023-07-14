lista = ('caneta', '1.00', 'lapis', '1.50', 'caderno', '5.00', 'livro', '10.00')
print('-='*30)
print(f'{"LISTA DE PREÇOS DE ITENS":^30}')
print('-='*30)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$: {lista[pos]:>7}')
print('-='*30)
#preciso estudar mais sobre centralização das impressões.