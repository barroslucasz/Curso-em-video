pessoas = []
totpessoas = []
total = 0
totmai = totmen = 0
while True:
    pessoas.append(str(input('Digite seu nome: ')))
    pessoas.append(float(input('Digite seu peso: ')))
# ---------------------------------------------------------
# solução para o maior e menor peso. (usei a resposta do guanabara)
    if len(totpessoas) == 0:
        totmai = totmen = pessoas[1]
    else:
        if pessoas[1] > totmai:
            totmai = pessoas[1]
        if pessoas[1] < totmen:
            totmen = pessoas[1]
# ---------------------------------------------------------
    totpessoas.append(pessoas[:])
    pessoas.clear()
    total += 1
    rep = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if rep == 'N':
        break
print('-='*20)
# print(totpessoas) # aqui usei só para testar se minha lista estava imprimindo corretamente.
if total == 1:
    print(f'Voce cadastrou {total} pessoa.')
else:
    print(f'Você cadastrou {total} pessoas.')

#print(f'Ao todo você cadastrou {len(totpessoas)} pessoa.') # solução do guanabara, porém 'não tem como corrigir o plural'. #euacho!!
print(f'O maior peso foi de {totmai}kg, peso de', end=' ')
# ---------------------------------------------------------
for p in totpessoas:
    if p[1] == totmai >1:
        print(f'[{p[0]}]', end='')
    elif p[1] == totmai == 0:
        print(f'') 
print('')
# ---------------------------------------------------------
print(f'O menor peso foi de {totmen}kg, peso de', end=' ')
for p in totpessoas:
    if p[1] == totmen:
        print(f'[{p[0]}]', end='')
print('')

# nao conseguir resolver o maior e o menor peso!
# exercício resolvido no dia 29/06/2023
