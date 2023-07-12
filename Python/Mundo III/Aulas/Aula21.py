# >>>> INTERACTIVE HELP <<<<
# >>>> DOCSTRINGS <<<<

help(print)
print(input.__doc__)

def contador (i,f,p):
    """
    => SIGNIFICADO DOS PARAMETROS
    -----------------------------

    => parametro [i]: inicio
    => parametro [f]: fim
    => parametro [p]: passo

    Função criada por Lucas
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(2,10,2)
help(contador)
print('-='*35)
print()
# ---------------------------------------------------------------------------------------------------------------------------------------

# >>>> PARÂMETROS OPCIONAIS: <<<<

def somar (a=0,b=0,c=0): # vai receber [a], vai receber [b] e o [c] vai ser opcional e poderia ser para os três parâmetros!
    s = a+b+c
    print(s)


somar(1,2,3)
somar(20,10)
somar(10)
somar()
somar(a=5,c=2) # podemos nomear os parâmetros
print('-='*35)
print()
# ---------------------------------------------------------------------------------------------------------------------------------------

# >>>> ESCOPO DE VARIÁVEIS: <<<<

def teste ():
    x = 8 # variável local
    print(f'Na função teste [n] vale {n}')
    print(f'Na função teste [x] vale {x}')


# programa principal:
n = 2 # variável global
print(f'No programa principal [n] vale {n}')
teste()
# print(f'No programa principal [x] vale {x}') # a variavel x só existe dentro do teste. sendo assim um escopo local
print()
print()
# ---------------------------------------------------------------------------------------------------------------------------------------

def funcao ():
    global n1 # comando global torna o que está dentro da função em [GLOBAL]
    n1 = 4 # variável local
    print(f'[N1] local vale {n1}')


n1 = 2 # variável global
funcao()
print(f'[N1] global vale {n1}')
print('-='*35)
print()
# ---------------------------------------------------------------------------------------------------------------------------------------

# >>>> RETORNO DE VALORES:  RETURN <<<<

def soma (a=0,b=0,c=0):
    s = a+b+c
    return s


r1 = soma(1,2,3)
r2 = soma(1,2)
r3 = soma(1)
print(f'A soma dos valores é igual a {r1}, {r2} e {r3}')
print('-='*35)
print()

# ---------------------------------------------------------------------------------------------------------------------------------------

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
print()

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são: {f1}, {f2} e {f3}')
print()
# ---------------------------------------------------------------------------------------------------------------------------------------

def par(num = 0):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))

if par (num):
    print('É Par!')
else:
    print('É Ímpar!')