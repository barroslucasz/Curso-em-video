times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Atlético-MG', 'Fluminense',
         'São Paulo', 'Internacional', 'Bragantino', 'Fortaleza', 'Athletico-PR',
         'Cruzeiro', 'Santos', 'Bahia', 'Corinthians', 'Cuiabá', 'Goiás', 'América-MG',
         'Vasco da Gama', 'Coritiba')
print('-='*50)
print('Lista dos times do Brasileirão 2023:')
print(times)
print('-='*50)
print('Os cinco primeiros são:')
print(times[:5])
print('-='*50)
print('Os quatro últimos são:')
print(times[16:20])
print('-='*50)
# tentei usar o 'sorted' imprimindo igual fiz nas questões acima e não imprimiu
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*50)
# a solução a seguir fiz com ajuda do guanabara mesmo.
print(f'O Internacional está na {times.index("Internacional")+1}ª posição')
