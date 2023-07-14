import moedas

# programa principal
p = float(input('Digite um preço R$: '))
print(f'A metade de {moedas.moeda(p)} é igual a {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é igual a {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando 10%, temos R$: {moedas.moeda(moedas.aumentar(p, 10))}')
