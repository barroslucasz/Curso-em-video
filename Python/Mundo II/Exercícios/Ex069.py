print('--='*10)
print('     CADASTRE UMA PESSOA')
print('--='*10)
maior = 0
homem = 0
mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
        if resp == 'S':
            print('--=' * 10)
            print('     CADASTRE UMA PESSOA')
            print('--=' * 10)
    if resp == 'N':
        break
if maior == 1:
    print('Tivemos uma pessoa maior de idade cadastrada.')
elif maior == 0:
    print('Não temos pessoas com mais de 18 anos cadastradas.')
else:
    print(f'Temos {maior} pessoas com mais de 18 anos.')
if homem > 1:
    print(f'Ao todo temos {homem} homens cadastrados', end='')
elif homem == 0:
    print('Não temos homem cadastrado', end='')
else:
    print(f'Somente um homem cadastrado', end='')
if mulher == 1:
    print(' e uma mulher com menos de 20 anos.')
elif mulher == 0:
    print(' e nenhuma mulher com menos de 20 anos.')
elif mulher < 20 != 1 :
    print(f' e temos {mulher} mulheres com menos de 20 anos.')
else:
    print(' e nenhuma mulher com menos de 20 anos.')
