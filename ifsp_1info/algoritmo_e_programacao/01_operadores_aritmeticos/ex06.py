'''
Exercício: Faça um algoritmo que receberá o preço do produto, calcule e mostre o novo preço sabendo que este sofreu 10%
Aula: 17/02/2025
'''

# Resolução do professor:

preco = 0.0
desconto = 0.0
preco_com_desconto = 0.0
preco_final = 0.0

preco = float(input('Preço do produto: '))
preco_com_desconto = preco * 0.1
preco_final = preco - preco_com_desconto
print(f'O preço do produto com desconto é: {preco_final}\n')

# Minha resolução:

preco = float(input('Preço do produto: '))
desconto = preco * 0.1
print(f'O desconto do produto é {desconto}\nO preço do produto com desconto é: {preco - desconto}')