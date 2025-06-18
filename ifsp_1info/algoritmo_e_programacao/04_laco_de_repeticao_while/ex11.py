confirmacao = 'sim'
num = 0
while confirmacao == 'sim' or confirmacao != 'não':
    print('')
    num = int(input('Digite um número: '))
    if num > 0:
        print(f'{num} é um número positivo')
    elif num < 0:
        print(f'{num} é um número negativo')
    elif num == 0:
        print(f'{num} é zero')
    num = input('Deseja continuar? ').lower()