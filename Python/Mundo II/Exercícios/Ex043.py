peso = float(input('Qual é seu peso em ( kg ): '))
altura = float(input('Qual é sua altura em ( m ): '))
imc = peso / altura ** 2
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('VOCÊ ESTÁ EM: ABAIXO DO PESO!')
elif imc > 18.5 and imc <= 25:
    print('VOCÊ ESTÁ EM: PESO IDEAL!')
elif imc >= 25 and imc <= 30:
    print('VOCÊ ESTÁ EM: SOBREPESO!')
elif imc >= 30 and imc <= 40:
    print('VOCÊ ESTÁ EM: OBESIDADE!')
elif imc >= 41:
    print('VOCÊ ESTÁ EM: OBESIDADE MÓRBIDA!')
