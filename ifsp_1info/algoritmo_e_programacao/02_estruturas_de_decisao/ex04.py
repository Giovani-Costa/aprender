'''
Exercício: Construa um algoritmo que peça o nome do usuário e os valores de venda do mês. Se estiver entre 10.000 e 50.000, escreva: {nome}, suas vendas estão ideais. Caso esteja menor que 10.000, escreva: {nome}, suas vendas estão baixas. E caso seja superior a 50.000, escreva: {nome}, suas vendas estão ótimas
Aula: 17/03/2025
'''

# Resolução do professor:

nome = ''
vendas = 0.0

nome = input('Nome: ')
vendas = float(input('Vendas: '))

if vendas >= 10_000:
    print(f'{nome}, suas vendas estão baixas.')
else:
    if vendas >= 10_000 and vendas <= 50_000:
        print(f'{nome}, suas vendas estão ótimas')    
    else: 
        print(f'{nome}, suas vendas estão ideais.')

# Minha resolução:

nome = input('Nome: ')
vendas = float(input('Vendas: '))

if vendas >= 10_000 and vendas <= 50_000:
    print(f'{nome}, suas vendas estão ideais.')
elif vendas >= 50_000:
    print(f'{nome}, suas vendas estão ótimas')    
else:
    print(f'{nome}, suas vendas estão baixas.')