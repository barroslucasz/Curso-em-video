from random import randint

'''CPF = [randint(0,8),randint(0,8),randint(0,8),randint(0,8),randint(0,8),randint(0,8),randint(0,8),randint(0,8),]'''

CPF = 108357944

D1 = 10*1 + 9*0 + 8*8 + 7*3 + 6*5 + 5*7 + 4*9 + 3*4 + 2*4

resto_divisao1 = D1 % 11
primeiro_digito = 11-resto_divisao1

if resto_divisao1 == 0 :
    print(0)
elif resto_divisao1 == 1:
    print(0)
else:
    print(11 - resto_divisao1)

D2 = 10*0 + 9*8 + 8*3 + 7*5 + 6*7 + 5*9 + 4*4 + 3*4 + 2*4

resto_divisao2 = D2 % 11
segundo_digito = 11 - resto_divisao2


if resto_divisao2 == 0:
    print(0)
elif resto_divisao2 == 1:
    print(0)
else:
    resto2 = resto_divisao2


print(CPF)