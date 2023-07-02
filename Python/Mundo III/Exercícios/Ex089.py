nome = []
nt1 = []
nt2 = []
while True:
    nome.append(str(input('Nome: ')))
    nt1.append(float(input('Nota1: ')))
    nt2.append(float(input('Nota2: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        print('-='*20)
        break
print(nome, nt1, nt2)