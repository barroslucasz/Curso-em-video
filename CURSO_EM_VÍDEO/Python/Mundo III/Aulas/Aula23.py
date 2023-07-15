try: # aqui ele tenta realizar o solicitado
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: # aqui é o tratamento do erro para não mostrar o erro e sim uma 'mensagem' dizendo o problema
    print(f'Problema encontrado foi {erro.__class__}')
else: # aqui serve para caso der certo o problema ele venha mostrar a solução
    print(f'A divisão é igual a: {r:.1f}')
finally: # mensagem opcional que será mostrada no final independente se houve erro ou não!
    print('Obrigado volte sempre!')