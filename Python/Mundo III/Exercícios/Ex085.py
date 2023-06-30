valores = 0
par = []
impar = []
for cont in range(1,8):
    valores = int(input(f'Digite o {cont}º valor: '))
    if valores % 2 == 0:
        par.append(valores)
    else:
        impar.append(valores)
print('-='*20)
print(f'Os valores pares digitados foram: {sorted(par)}')
print(f'Os valores ímpares digitados foram: {sorted(impar)}')

# consegui resolver esta atividade desse jeito acima, mas na resolução do guanabara tem uma lista dentro de outra lista.
# atividade realizada no dia 30/06/2023
# abaixo a resolução do guanabara:

print('')
print('-=-=-=RESOLUÇÃO DO GUANABARA:-=-=-=')
print('')
num = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*20)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
