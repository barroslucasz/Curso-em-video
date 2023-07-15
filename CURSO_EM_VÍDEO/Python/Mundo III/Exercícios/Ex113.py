def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: Por favor, digite um número inteiro válido!')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário!')
        else:
            return n


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')