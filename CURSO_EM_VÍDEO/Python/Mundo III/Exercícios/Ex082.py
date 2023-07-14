valores = []
par = []
impar = []
while True:
    valores.append(int(input('Digite um valor: ')))
    rep = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-='*20)
    if rep == 'N':
        break
print(f'A lista digitada foi {valores}')
for i, v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'Os valores pares são: {par}')
print(f'Os valores impares são: {impar}')
