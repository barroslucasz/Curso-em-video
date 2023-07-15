from utilidadescev import moeda
from utilidadescev import dado

# programa principal

p = dado.leiadinheiro('Digite o preço R$: ')
moeda.resumo(p, 10)


'''print(f'A metade de {moedas.moeda(p)} é igual a {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moeda(p)} é igual a {moedas.dobro(p, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(p, 13, True)}')
'''