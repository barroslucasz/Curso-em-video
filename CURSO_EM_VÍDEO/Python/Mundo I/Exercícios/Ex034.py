from time import sleep
salario = float(input('Digite o seu salário para calcularmos o valor com o reajuste:'))
print('Calculando...')
sleep(2)
if salario <=1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Seu salário de {:.2f} passará a ser {:.2f}'.format(salario, novo))
