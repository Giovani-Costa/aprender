'''
Exercício: Construa um algoritmo para calcular a média de quatro notas
Aula: 10/02/2025
'''

# Resolução do professor:

nome = ''
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
nota4 = 0.0
media = 0.0

nome = input('Nome do aluno: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'{nome}, sua média é: {media}\n')

# Minha resolução:

nome = input('Nome do aluno: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
print(f'{nome}, sua média é: {(nota1 + nota2 + nota3 + nota4) / 4}')