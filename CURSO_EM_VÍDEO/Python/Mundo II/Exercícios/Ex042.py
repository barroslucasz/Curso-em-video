print('-**-'*10)
print('ANALISADOR DE TRIÂNGULOS')
print('-**-'*10)
c1 = float(input('Por favor informe o primeiro segmento: '))
c2 = float(input('Por favor informe o segundo segmento: '))
c3 = float(input('Por favor informe o terceiro segmento: '))
if c1 < c2 + c3 and c2 < c1 + c3 and r3 < c1 + c2:
    print('os segmentos formam um tipo de triangulo ', end='')
    if c1 == c2 == c3:
        print('EQUILÁTERO.')
    elif c1 != c2 != c3 != c1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não podem formar um TRIÂNGULO.')
    