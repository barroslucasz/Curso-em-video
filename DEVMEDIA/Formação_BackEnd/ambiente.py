nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
média = (nota_1 + nota_2) / 2
while True:
    if média >= 7:
        print('Aprovado!')
    else:
        print('Reprovado!')
    continuar = str(input('Deseja continuar? [S/N]')).upper()

