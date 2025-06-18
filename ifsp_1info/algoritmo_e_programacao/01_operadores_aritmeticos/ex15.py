'''
Exercício: Faça um programa que vai receber o curso de um espetáculo teatral e o preço do convite e calcule o mínimo de convites para no mínimo pagar o espetáculo
Aula: 10/03/2025
'''

# Resolução do professor:

espetaculo = 0.0
convite = 0.0
convites_minimos = 0.0

espetaculo = float(input('O espetáculo irá custar: '))
convite = float(input('O convite irá custar: '))
convites_minimos = espetaculo // convite + 1

print(f'Será necessário vender {convites_minimos} convites\n')

# Minha resolução:

espetaculo = float(input('O espetáculo irá custar: '))
convite = float(input('O convite irá custar: '))
print(f'Será necessário vender {espetaculo // convite + 1} convites')