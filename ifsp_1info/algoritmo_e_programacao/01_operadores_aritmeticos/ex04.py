'''
Exercício: Construa um algoritmo para calcular a equação (4/r) * (w+r)
Aula: 17/02/2025
'''

# Resolução do professor:

r = 0.0
w = 0.0
equacao = (4/r) * (w+r)

r = float(input('Digite o valor de r: '))
w = float(input('Digite o valor de w: '))

print(f'O resultado da equação é: {equacao}\n')

# Minha resolução:

r = float(input('Digite o valor de r: '))
w = float(input('Digite o valor de w: '))
print(f'O resultado da equação é: {(4/r) * (w+r)}')