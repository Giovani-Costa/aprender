'''
Exercício: Faça um programa que recebe: o preço de fábrica de um carro; o percentual do distribuidor; e o percentual de impostos ao preço de fábrica. E calcule o preço final do carro
Aula: 10/03/2025
'''

# Resolução do professor:

fab_preco = 0.0
pl_distribuidor = 0.0
l_distribuidor = 0.0
p_imposto = 0.0
imposto = 0.0
fin_preco = 0.0

fab_preco = float(input('Preço de fábrica: '))
pl_distribuidor = float(input('Percentual do vendedor: '))
p_imposto = float(input('Impostos: '))
l_distribuidor = fab_preco * (pl_distribuidor / 100)
imposto = fab_preco * (p_imposto / 100)
fin_preco = fab_preco + l_distribuidor + imposto

print(f'\nO lucro do distribuir é: {l_distribuidor}R$')
print(f'O valor do imposto é: {imposto}R$')
print(f'O preço final do carro é : {fin_preco}R$\n')

# Minha resolução:

fab_preco = float(input('Preço de fábrica: '))
pl_distribuidor = float(input('Percentual do vendedor: ')) / 100
p_imposto = float(input('Impostos: ')) / 100
print(f'\nO lucro do distribuir é: {fab_preco * pl_distribuidor}R$\nO valor do imposto é {fab_preco * p_imposto}R$\nO preço final do carro é {fab_preco + (fab_preco * pl_distribuidor) + (fab_preco * p_imposto)}R$')