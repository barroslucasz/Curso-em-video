# LISTAS:

dados = []
pessoas = []
pessoas1 = []
dados.append('Lucas') # aqui adiciona um elemento a uma lista!
pessoas.append(dados[:]) # aqui adiciona uma lista em outra lista!
pessoas1 = [['Lucas', 28], ['Maria', 50], ['Pedro', 60]] # outra forma de adicionar uma lista dentro de outra lista!
print(pessoas)
print(pessoas1[0][0]) # posicionamento de elementos em lista composta!
print(pessoas1[2][0])
print(pessoas1[1][1])
# -------------------------------

galera = []
dado = []
totmai = totmen = 0 # aqui podemos fazer isso com variaveis simples, mas não podemos fazer com variaveis compostas. ex: totmai = totmen = galera = dado = 0
for c in range(0,2):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua idade: ')))
    galera.append(dado[:]) # não podemos esquecer de usar os dois pontos para poder criar uma cópia de dados.
    dado.clear()
print(galera)

for p in galera:
    print(f'{p[0]} tem {p[1]} anos.') # aqui imprime o que tem dentro da lista.

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1 # aqui funcionou sem precisar adicionar esta linha!
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1 # aqui funcionou sem precisar adicionar esta linha!
