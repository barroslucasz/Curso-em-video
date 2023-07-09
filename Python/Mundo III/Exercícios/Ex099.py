def maior(*num):
    cont = maior = 0
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nO maior valor informado foi {maior}')

# prog a partir dq

maior(0,2,3,5,6,7,8,1)
maior(2,45,6,2,87,13,55)

# atividade feita no dia 9dejul