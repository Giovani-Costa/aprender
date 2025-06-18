'''
Exercício: Faça um algoritmo que receberá o salário de um funcionário e a porcentagem do aumento, calcule e mostre o resultado final
Aula: 17/02/2025
'''

# Resolução do professor:

salario = 0.0
aumento = 0.0
salario_final = 0.0

salario = float(input('Salário do funcionário: '))
aumento = float(input('Aumento do funcionário em porcentagem: '))
salario_final = salario + (salario * aumento / 100)
print(f'O salário do funcionário com aumento é: {salario_final}\n')

# Minha resolução:

salario = float(input('Preço do produto: '))
aumento = float(input('Aumento do funcionário em porcentagem: '))
aumento = salario * aumento / 100
print(f'O salário do funcionário com aumento é: {salario + aumento}')