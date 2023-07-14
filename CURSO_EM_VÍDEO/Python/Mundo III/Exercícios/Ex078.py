'''valor = [input('Digite um valor para posição 0: '), input('Digite um valor para posição 1: '), input('Digite um valor para posição 2: '),
          input('Digite um valor para posição 3: '), input('Digite um valor para posição 4: ')]
print(f'Você digitou os valores {valor}')
for c, v in enumerate(valor):
    print(f'O maior valor digitado foi {max(valor)} na posição {c}!')
#print(f'O maior valor digitado foi {max(valor)} nas posições {}')
#print(f'O menor valor digitado foi {min(valor)} nas posições ')'''

# abaixo foi a resolução do guanabara

valor = []
mai = 0
men = 0
for c in range(0 , 5):
    valor.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        mai = men = valor[c]
    else:
        if valor[c] > mai:
            mai = valor[c]
        if valor[c] < men:
            men = valor[c]
print('-='*20)
print(f'Você digitou os valores{valor}')
print(f'O maior valor digitado foi {mai} na posição ', end='')
for i, v in enumerate(valor):
    if v == mai:
        print(f'{i}')
print(f'O menor valor digitado foi {men} na posição ', end='')
for i, v in enumerate(valor):
    if v == men:
        print(f'{i}')

# Esta aula aprendi no dia 27/06/2023