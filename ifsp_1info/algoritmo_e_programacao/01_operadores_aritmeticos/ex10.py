'''
Exercício: Faça um algoritmo que receba o salário mínimo e o salário de um programador e calcule quantos salários mínimos esse trabalhor ganha
Aula: 24/02/2025
'''

# Resolução do professor:

salario_minimo = 0.0
salario = 0.0
quantidade = 0.0

salario_minimo = float(input('Salário mínimo: '))
salario = float(input('Salário do trabalhador: '))
quantidade = salario / salario_minimo

print(f'Ele ganha {quantidade} salários mínimos\n')

# Minha resolução:

salario_minimo = float(input('Salário mínimo: '))
salario = float(input('Salário do trabalhador: '))
print(f'Ele ganha {salario / salario_minimo} salários mínimos')