def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda = 'R$: '):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0, taxaa=0, taxar=0):
    print('-='*20)
    print('Resumo do valor'.center(40))
    print('-='*20)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'O dobro do preço é: \t{dobro(preco, True)}')
    print(f'A metade do preço é: \t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento é: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxaa}% de desconto é: \t{diminuir(preco, taxaa, True)}')
    print('-='*20)
