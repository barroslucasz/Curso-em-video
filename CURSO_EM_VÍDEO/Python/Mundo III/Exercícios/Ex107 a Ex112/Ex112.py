import moedas

# programa principal
p = float(input('Digite um preço R$: '))
print(f'A metade de {p} é igual a R$: {moedas.metade(p)}')
print(f'O dobro de {p} é igual a R$: {moedas.dobro(p)}')
print(f'Aumentando 10%, temos R$: {moedas.aumentar(p, 10)}')
