print('-**-'*10)
print('ANALISADOR DE TRIÂNGULOS')
print('-**-'*10)
c1 = float(input('por favor informe o primeiro segmento:'))
c2 = float(input('por favor informe o segundo segmento:'))
c3 = float(input('por favor informe o terceiro segmento:'))
if c1 + c2 > c3:
    print('os segmentos formam um triangulo!')
else:
    print('os segmentos não formam um triangulo.')
