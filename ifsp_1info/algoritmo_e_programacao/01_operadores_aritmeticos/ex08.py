'''
Exercício: Faça um algoritmo que receberá o salário de um funcionário e o valor total de vendas. O funcionário recebe 4% de comissão pelas vendas. Calcule e mostre o resultado final
Aula: 24/02/2025
'''

# Resolução do professor:

salario = 0.0
vendas = 0.0
salario_final = 0.0
comissao = 0.0

salario = float(input("Salário do funcionário: "))
vendas = float(input("Total de vendas: "))
comissao = vendas / 100 * 4
salario_final = salario + comissao

print(f'O salário final é de: {salario_final}')
print(f'A comissão é de: {comissao}\n')

# Minha resolução:

salario = float(input("Salário do funcionário: "))
vendas = float(input("Total de vendas: "))
print(f'O salário final é de : {salario + (vendas * 0.04)}\nA comissão é de: {vendas * 0.04}')