'''
Exercício: Construa um algoritmo que peça o nome do usuário e sua idade. Se a idade for maior ou igual que 18, escreva: {nome}, você já pode obter CNH. Caso contrário, escreva: {nome}, você não pode obter CNH.
Aula: 17/03/2025
'''

# Resolução do professor:

nome = ''
idade = 0.0

nome = input('Nome: ')
idade = float(input('Idade: '))

if idade >= 18:
    print(f'{nome}, você já pode obter CNH.\n')
else:
    print(f'{nome}, você não pode obter CNH.\n')

# Minha resolução:

nome = input('Nome: ')
idade = float(input('Idade: '))

if idade >= 18:
    print(f'{nome}, você já pode obter CNH.\n')
else:
    print(f'{nome}, você não pode obter CNH.\n')