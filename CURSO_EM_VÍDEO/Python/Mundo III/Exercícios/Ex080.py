'''valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    for c in sorted(valores):
        print(f'Foi adicionado na posição {c}!')
print(f'Os valores digitados em ordem foram: {sorted(valores)}')'''

# não consegui resolver o problema de imprimir onde os valores estavam sendo alocado.
# esqueci que não podia usar o sorted!
# solução do guanabara abaixo:

lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista!')
                break
            pos += 1
print('-='*20)
print(f'Os valores digitados em ordem foram: {lista}')