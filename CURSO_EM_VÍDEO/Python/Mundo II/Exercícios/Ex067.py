while True:
    print('-='*20)
    num = int(input('QUAL NÚMERO DESEJA VER A TABUADA? '))
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} x {c} = {num*c}')
print('PROGRAMA ENCERRADO!')