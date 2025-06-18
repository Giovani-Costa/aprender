'''
Exercício: Construa um algoritmo para calcular a média de duas notas. Caso a média seja no mínimo 6; mostrar a mensagem que o aluno foi aprovado, caso contrário mesmo está reprovado
Aula: 17/03/2025
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

if media >= 6:
    print(f'{nome}, sua média é: {media}. Você está aprovado\n')
else:
    if (nota1 + nota2) <= 6 and (nota1 + nota2) >= 4:
        print(f'{nome}, sua média é: {(nota1 + nota2) / 2}. Você está de exame')
    else:
        print(f'{nome}, sua média é: {media}. Você está reprovado')

# Minha resolução:

nome = input('Nome do aluno: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

