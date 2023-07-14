# inicio do programa aqui apenas estamos lendo os dados do programa!
time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [ S/N ]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas com [S ou N]')
    if resp == 'N':
        break
print('-'*20)

# a partir daqui é a análise de dados solicitados.
print('Cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*20)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro! Jogador inexistente')
    else:
        print(f'--- Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-='*20)
print('>>> Volte sempre <<<')

# exercício copiado por etapa da resposta do guanabara!!
# exercício feito no dia 06/07/2023