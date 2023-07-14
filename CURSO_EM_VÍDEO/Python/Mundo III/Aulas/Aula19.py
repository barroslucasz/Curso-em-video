# DICIONÁRIOS:

dados = {
    'nome':'Lucas',
    'idade':'28'
}
print(dados['nome'])
print(dados['idade'])
print(f'O {dados["nome"]} tem {dados["idade"]} anos') # para imprimir formatado dentro precisa de aspas duplas

# append não funciona em dicionários!

dados['Sexo']='M' # dessa forma adicionamos um novo elemento dentro do dicionário!
del dados['idade'] # dessa forma deletamos um elemento dentro do dicionário!

filmes = {
    'Título':'Star Wars', # detalhe importante é não esquecer as virgulas!!
    'Ano':'1977',
    'Diretor':'George Lucas'
}
print(filmes.values()) # aqui imprime apenas o que está dentro do item ex: (['Star Wars', '1977', 'George Lucas'])
print(filmes.keys()) # aqui imprime apenas o nome do item ex: (['Título', 'Ano', 'Diretor'])
print(filmes.items()) # aqui imprime tudo ex: ([('Título', 'Star Wars'), ('Ano', '1977'), ('Diretor', 'George Lucas')])

# para cada chave no valor # for = enquanto
for k, v in filmes.items():
    print(f'O {k} é {v}')


brasil = []
estado1 = {
    'UF':'Pernambuco',
    'Sigla':'PE'
}
estado2 = {
    'UF':'Paraíba',
    'Sigla':'PB'
}
brasil.append(estado1) # aqui adicionamos o dicionário dentro de uma lista
brasil.append(estado2) # aqui adicionamos o dicionário dentro de uma lista
print(brasil)
print(brasil[0]) # aqui vai imprimir apenas o item 0 da lista
print(brasil[0]['UF']) # aqui vai imprimir apenas o item 0 da lista dentro da declaração 'UF'

estado = {}
br = []
for c in range (0,3):
    estado['UF'] = str(input('Unidade federativa: '))
    estado['Sigla'] = str(input('Sigla do estado: '))
    br.append(estado.copy())
for e in br:
    for v in e.values():
        print(v, end=' ')
    print()