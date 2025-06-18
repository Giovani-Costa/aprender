'''
Exercício: Faça um programa que receba o valor do salário e quantidade de quilowatt. Sabendo que o quilowatt é um quinto do salário, calcule: o valor de cada quilowatt; o valor a ser pago pela casa; e o valor a ser pago com 15% de desconto
Aula: 10/03/2025
'''

# Resolução do professor:

salario = 0.0
gasto = 0.0
quilowatt = 0.0
q_gasto = 0.0
q_desconto = 0.0

salario = float(input('Salário: '))
gasto = float(input('Gasto de quilowatts da casa: '))
quilowatt = salario / 5
q_gasto = quilowatt * gasto
q_desconto = (quilowatt * gasto) - (quilowatt * gasto) * 0.15

print(f'Com o quilowatt custando {quilowatt} R$, a casa terá que pagar {q_gasto} R$, mas com um desconto de 15% passa a ser {q_desconto} R$\n')

# Minha resolução:

salario = float(input('Salário: '))
gasto = float(input('Gasto de quilowatts da casa: '))
print(f'Com o quilowatt custando {salario / 5} R$, a casa terá que pagar {(salario / 5) * gasto}, mas com um desconto de 15% passa a ser {((salario / 5) * gasto) - ((salario / 5) * gasto) * 0.15} R$')