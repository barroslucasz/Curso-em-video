primeiro = int(input('Primeiro Valor: '))
segundo = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] ENCERRAR O PROGRAMA')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        soma = primeiro + segundo
        print('A soma entre {} e {} é igual a {}.'.format(primeiro, segundo, soma))
    elif opcao == 2:
        mult = primeiro * segundo
        print('A multiplicação entre {} e {} é igual a {}.'.format(primeiro, segundo, mult))
    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print('O maior número entre {} e {} é {}.'.format(primeiro, segundo, maior))
    elif opcao == 4:
        print('Informe os números novamente')
        primeiro = int(input('Primeiro Valor: '))
        segundo = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
    print('=-='*20)
print('Fim do Programa!')