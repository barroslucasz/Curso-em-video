print('-='*10)
print('    Loja Barros')
print('-='*10)
total = 0
totmil = 0
menor = 0
cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
        print('-='*15)
    if resp == 'N':
        break
print('FIM')
print(f'O total de compras foi de ${total:.2f}')
if totmil == 0:
    print('Não temos nenhum produto custando mais de $ 1000,00')
elif totmil == 1:
    print('Temos um produto custando mais de 1000,00')
else:
    print(f'Temos {totmil} produtos custando mais de $ 1000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
