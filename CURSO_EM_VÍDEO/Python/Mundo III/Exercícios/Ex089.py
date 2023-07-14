ficha = []
while True:
    nome = str(input('Nome: '))
    nt1 = float(input('Nota1: '))
    nt2 = float(input('Nota2: '))
    media = (nt1 + nt2) / 2
    ficha.append([nome, [nt1, nt2], media])
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        print('-='*20)
        break

print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-='*20)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-='*20)
    opc = int(input('Quais notas deseja visualizar: [999 P/interromper] '))
    if opc == 999:
        print('-='*20)
        break
    if opc <= len(ficha) -1:
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('>>> Obrigado!! <<<')
# muito fácil de resolver porém foi cópia da resolução do guanabara!
# atividade iniciada a resolução em 02/07/2023 e finalizada no dia 03/07/2023