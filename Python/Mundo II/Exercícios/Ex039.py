from datetime import date
atual = date.today().year
print('--=='*20)
print('SOBRE O ALISTAMENTO MILITAR RESPONDA COM UMA DAS OPÇÕES ABAIXO:')
print('--=='*20)
print('SEU SEXO É:')
print('[ 1 ] Masculino')
print('[ 2 ] Feminino')
sexo = int(input('OPÇÃO: '))
if sexo == 1:
    print('Você é HOMEM e seu alistamento é obrigatório! Por favor digite abaixo seu ano de nascimento: ')
    nascimento = int(input('Ano de nascimento com 4 digítos: '))
    idade = atual - nascimento
    alistamento = 18 - idade
    print('Você nasceu em {} atualmente tem {} anos.'.format(nascimento, idade))
    if idade == 17:
        print('Falta apenas {} ano para seu alistamento'.format(alistamento))
    elif idade < 17:
        print('Faltam {} anos para seu alistamento que será em {}.'.format(alistamento, nascimento + 18))
    elif idade == 18:
        print('Você precisa de alistar IMEDIATAMENTE.')
    elif idade > 19:
        print('O ano do seu alistamento foi em {}.'.format(nascimento + 18))
if sexo == 2:
    print('Você é MULHER e seu alistamento não é obrigatório.')
    print('DESEJA CONTINUAR MESMO ASSIM?')
    print('[ 1 ] SIM')
    print('[ 2 ] NÃO')
    opcao = int(input('SELECIONE UMA OPÇÃO:'))
    if opcao == 1:
        nascimento = int(input('Ano de nascimento: '))
        idade = atual - nascimento
        alistamento = 18 - idade
        print('Você nasceu em {} atualmente tem {} anos.'.format(nascimento, idade))
        if idade == 17:
            print('Falta apenas {} ano para seu alistamento'.format(alistamento))
        elif idade < 17:
            print('Faltam {} anos para seu alistamento que será em {}.'.format(alistamento, nascimento + 18))
        elif idade == 18:
            print('As interessadas em seguir a carreira como militares precisarão prestar concurso público de escolas como:')
            print('')
            print('Escola de Formação Complementar do Exército (EsFCEx)')
            print('Escola de Saúde do Exército (EsSEx)')
            print('Instituto Militar de Engenharia (IME)')
            print('Escola de Sargentos de Logística (EsSLog).')
        elif idade > 19:
            print('O ano do seu alistamento foi em {}.'.format(nascimento + 18))
elif sexo >= 3:
    print('Opção Inválida')