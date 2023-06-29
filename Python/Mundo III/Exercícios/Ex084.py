pessoas = []
totpessoas = []
total = 0
totmai = totmen = 0
while True:
    pessoas.append(str(input('Digite seu nome: ')))
    pessoas.append(int(input('Digite seu peso: ')))
    totpessoas.append(pessoas[:])
    total += 1
    rep = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if rep == 'N':
        break
print(totpessoas)
print(pessoas)
if total == 1:
    print(f'Voce cadastrou {total} pessoa.')
else:
    print(f'Você cadastrou {total} pessoas.')

# nao conseguir resolver o maior e o menor peso!
