lanche = ('Hamburguer', 'suco', 'pizza', 'pudim')

for comida in lanche:
    print(f'eu comi {comida}')
print('='*15)

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')
print('='*15)

for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')
print('='*15)

print('comi muuiitoo')
