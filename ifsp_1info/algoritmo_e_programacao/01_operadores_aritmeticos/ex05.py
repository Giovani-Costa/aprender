'''
Exercício: Desenvolva um algoritmo que:
    - Solicite o nome
    - Solicite o ano de nascimento e o ano atual
    - Calcule a idade em dias
    - Mostre nome e a idade calculada
    
Aula: 17/02/2025
'''

# Resolução do professor:

nome = ''
ano_nascimento = 0
ano_atual = 0

nome = input('Digite seu nome: ')
ano_nascimento = int(input('Digite seu ano de nascimento: \n'),)
ano_atual = int(input('Digite o ano atual: '))

idade_anos = ano_atual - ano_nascimento
dias = idade_anos * 365
print(f'{nome}, você tem aproximadamente {dias}')

# Minha resolução:

nome = input('Digite seu nome: ')
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
print(f'{nome}, você tem aproximadamente {(ano_atual - ano_nascimento) * 365}')