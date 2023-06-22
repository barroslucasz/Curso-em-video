radar = int(input('Sua velocidade foi: '))
if radar > 80:
    print('Você foi multado por excesso de velocidade')
    print('O valor da sua multa é: {}'.format((radar-80)*7))
else:
    print('Tenha um bom dia, dirija com segurança.')
    