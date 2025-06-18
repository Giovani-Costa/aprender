'''
Exercício: Construa um algoritmo para calcular a média de duas notas
Aula: 10/02/2025
'''

# Resolução do professor:

nome = ''
nota1 = 0.0
nota2 = 0.0
media = 0.0

nome = input('Nome do aluno: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2
print(f'{nome}, sua média é: {media}\n')

# Minha resolução:

nome = input('Nome do aluno: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
print(f'{nome}, sua média é: {(nota1 + nota2) / 2}')