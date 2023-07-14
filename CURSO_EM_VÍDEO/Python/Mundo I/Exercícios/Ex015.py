dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados:'))
tdias = dias*60
kmr = km*0.15
print('O total a pagar é R${:.2f}'.format(tdias+kmr))
