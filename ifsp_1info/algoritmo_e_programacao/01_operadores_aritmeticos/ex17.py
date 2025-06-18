'''
Exercício: Faça um programa que receba o número de lados de um polígono convexo e calcule a quantidade de diagonais desse
Aula: 10/03/2025
'''

# Resolução do professor:

lados = 0
diagonais = 0

lados = int(input('Número de lados: '))
diagonais = lados * (lados - 3) // 2
print(f'O número de diagonais desse polígono é {diagonais}\n')

# Minha resolução:

lados = int(input('Número de lados: '))
print(f'O número de diagonais desse polígono é {lados * (lados - 3) // 2}')