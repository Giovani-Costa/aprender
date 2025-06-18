'''
Exercício: Construa um algoritmo para calcular quantos reais seriam gastos para encher um tanque de um carro. O usuário vai informar o tipo de combustível e o seu preço e a capacidade do tanque
Aula: 17/03/2025
'''

# Resolução do professor:

carro = ''
tanque = 0.0
valor_litro = 0.0

carro = input('Álcool (A) ou gasolina (G)?: ')
tanque = float(input('Qual a capacidade do tanque: '))

if carro == 'G':
    print('Seu carro é à gasolina')
elif carro == 'A':
    print('Seu carro é a álcool')

valor_litro = float(input('Qual o valor do litro?'))

print(f'Para encher o tanque do seu carro será preciso R$ {tanque * valor_litro}')


# Minha resolução:

carro = input('Álcool (A) ou gasolina (G)?: ')
tanque = float(input('Qual a capacidade do tanque: '))

if carro == 'G':
    combustivel = float(input('Seu carro é à gasolina, qual o preço do litro? '))
elif carro == 'A':
    combustivel = float(input('Seu carro é a álcool, qual o preço do litro? '))
else:
    print('Não foi possível identificar o modelo do seu carro')

print(f'Para encher o tanque do seu carro será preciso R$ {tanque * combustivel}')
