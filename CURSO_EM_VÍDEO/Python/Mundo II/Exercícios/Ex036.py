casa = int(input('Valor da casa: R$: '))
salario = int(input('Salário do comprador: R$: '))
anos = int(input('Anos de financiamento: '))
financiamento = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$: {}, com um salário de R$: {} em {} anos a parcela será de R$: {:.2f}'.format(casa, salario, anos, financiamento))
if financiamento <= minimo:
    print('COMPRA APROVADA')
else:
    print('COMPRA NEGADA')
