'''
Exercício: Faça um algoritmo que calcula a área de um trapézio
Aula: 24/02/2025
'''

# Resolução do professor:

base_maior = 0.0
base_menor = 0.0
altura = 0.0
area = 0.0

base_maior = float(input('Medida da base maior: '))
base_menor = float(input('Medida da base menor: '))
altura = float(input('Medida da altura: '))
area = ((base_maior + base_menor) * altura) / 2

print(f'A área do trapézio é: {area}\n')

# Minha resolução:

base_maior = float(input('Medida da base maior: '))
base_menor = float(input('Medida da base menor: '))
altura = float(input('Medida da altura: '))
print(f'A área do trapézio é: {((base_maior + base_menor) * altura) / 2}')