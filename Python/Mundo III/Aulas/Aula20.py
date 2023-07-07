# funções sem parametro:
def mostralinha():
    print('-='*20)


mostralinha()


# -------------------------------------------------------------------------------
# funções com parametros:
def mensagem(msg):
    print('-='*20)
    print(msg)
    print('-='*20)


mensagem('Sistema de alunos')
mensagem('Alunos')


# -------------------------------------------------------------------------------
def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é {s}')


soma(30,25)


# -------------------------------------------------------------------------------
def contador(*num):
    print(num)


contador(1, 2, 3, 4, 5)
contador(6, 7, 8, 9)
contador(10, 11, 12)


# -------------------------------------------------------------------------------
def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim')


contador(1, 2, 3, 4, 5)
contador(6, 7, 8, 9)
contador(10, 11, 12)


# -------------------------------------------------------------------------------
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} que são ao todo {tam} números.')


contador(1, 2, 3, 4, 5)
contador(6, 7, 8, 9)
contador(10, 11, 12)


# -------------------------------------------------------------------------------
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos += 1


valores = [6, 3, 2, 1]
dobra(valores)
print(valores)


# -------------------------------------------------------------------------------
def soma (*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(2,3,5,6)
soma(1,2)
soma(20,55,0)