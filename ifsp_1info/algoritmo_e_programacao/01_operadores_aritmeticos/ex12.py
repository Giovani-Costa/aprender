'''
Exercício: Calcule o salário de um funcionário que recebe 50 reais de bônus e paga um imposto de 10%
Aula: 24/02/2025
'''

# Resolução do professor:

salario = 0.0

salario = float(input('Salário do funcionário: '))
imposto = salario * 0.1
salario_final = salario - imposto + 50

print(f'O salário do funcionário é: {salario_final}\n')

# Minha resolução:

salario = float(input('Salário do funcionário: '))
print(f'O salário do funcionário é: {salario - (salario * 0.1) + 50}')