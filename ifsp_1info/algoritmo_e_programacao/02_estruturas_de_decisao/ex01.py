'''
Exercício: Construa um algoritmo que eia o valor de uma conta de luz e, caso seja maior que R$ 80,00 apresente a mensagem: 'Você está gastando muito!!!'. Caso contrário exiba a mensagem: 'Seu gasto está normal!!!'
Aula: 17/03/2025
'''

# Resolução do professor:

valor_conta = 0.0
x = ''
y = 0

valor_conta = float(input('Informe o valor da conta: \n'))

if(valor_conta > 80):
    print(f'Você está gastando muito!!!')
else:
    print(f'Seu gasto está normal!!!')

# Minha resolução:

valor_conta = float(input('Informe o valor da conta: '))

if(valor_conta > 80):
    print(f'Você está gastando muito!!!')
else:
    print(f'Seu gasto está normal!!!')