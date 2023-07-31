while True:
    idade = int(input('Digite sua idade: '))
    print(f'Você tem {idade} anos.')
    resp = str(input('Deseja continuar: [S / N]' ))
    if resp == 's':
        continue
    else:
        break