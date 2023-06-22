print('============ LOJAS BARROS ============')
print('')
print('SELECIONE UMA FORMA DE PAGAMENTO:')
print('[ 1 ] À VISTA DINHEIRO/PIX')
print('[ 2 ] À VISTA NO CARTÃO')
print('[ 3 ] 2X NO CARTÃO')
print('[ 4 ] 3x OU MAIS NO CARTÃO')
opcao = int(input('DIGITE SUA OPÇÂO: '))
if opcao == 1:
    compras = float(input('VALOR DAS COMPRAS R$: '))
    op1 = compras - (compras * 10 / 100)
    print('Sua compra de R$: {:.2f} vai custar R$: {:.2f} com desconto de 10%.'.format(compras, op1))
elif opcao == 2:
    compras = float(input('VALOR DAS COMPRAS R$: '))
    op2 = compras - (compras * 5 / 100)
    print('Sua compra de R$: {:.2f} vai custar R$: {:.2f} com desconto de 5%.'.format(compras, op2))
elif opcao == 3:
    compras = float(input('VALOR DAS COMPRAS R$: '))
    op3 = compras
    print('Sua compra de R$: {} será parcelada em 2x de R$: {:.2f} sem juros.'.format(compras, op3 / 2))
elif opcao == 4:
    compras = float(input('VALOR DAS COMPRAS R$: '))
    op4 = compras + (compras * 20 / 100)
    parcelas = int(input('QUANTIDADE DE PARCELAS: '))
    print('Sua compra será parcelada em {}x de R$: {:.2f} totalizando R$: {:.2f} no final.'.format(parcelas, op4/parcelas, op4))
else:
    print('OPÇÃO INVÁLIDA')