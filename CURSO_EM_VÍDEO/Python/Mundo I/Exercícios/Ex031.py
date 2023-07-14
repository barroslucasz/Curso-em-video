viagem = int(input('Quantos km tem sua viagem? '))
preco = viagem*0.50
preco1 = viagem*0.45
if viagem <= 200:
    print('Sua viagem custará R$: {}'.format(preco))
else:
    print('Sua viagem custará R$: {}'.format(preco1))
