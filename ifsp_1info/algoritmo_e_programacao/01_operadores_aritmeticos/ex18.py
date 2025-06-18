'''
Exercício: Faça um programa que receba as dimensões de um cômodo de um casa. Para iluminar o cômodo inteiro da forma correta, será necessário 18W de potência por metro quadrado. Calcule quantos W serão necessários para iluminar o cômodo
Aula: 10/03/2025
'''

# Resolução do professor:

d1 = 0.0
d2 = 0.0
area = 0.0
watts = 0.0

d1 = float(input('Dimensão 1 (m): '))
d2 = float(input('Dimensão 2 (m): '))
area = d1 * d2
watts = area * 18

print(f'Para iluminar o cômodo de {area}m², seria necessários {watts}W de potência\n')

# Minha resolução:

d1 = float(input('Dimensão 1 (m): '))
d2 = float(input('Dimensão 2 (m): '))
print(f'Para iluminar o cômodo de {d1 * d2}m², seria necessários {(d1 * d2) * 18}W de potência')