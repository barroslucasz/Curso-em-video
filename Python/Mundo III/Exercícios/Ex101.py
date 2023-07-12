
def votacao (num=0):
    idade = 2023 - n
    if idade >= 18 < 70:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    elif idade == 16 or 17 :
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    elif idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO!')
    elif idade >= 70:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
        
    return idade


n = int(input('Digite seu ano de nascimento: '))
votacao()