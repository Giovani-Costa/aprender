'''
Exercício: Pedro comprou um saco de ração em quilos para seus gatos. Ele os alimenta em gramas diariamente. Faça um algoritmo que receba o peso do saco de ração e a quantidade de comida fornecida a cada gato e calcule o quanto resta no saco após cinco dias.
Aula: 10/03/2025
'''

# Resolução do professor:

saco = 0.0
gato_1 = 0.0
gato_2 = 0.0
comida_dias = 0.0
comida_final = 0.0

saco= float(input('Peso do saco (kg): '))
gato_1 = float(input('Comida do gato 1 por dia (g): '))
gato_2 = float(input('Comida do gato 2 por dia (g): '))
comida_dias = (gato_1 / 1000 + gato_2 / 1000) * 5
comida_final = saco - comida_dias
print(f'Após o quinto dia, resta {comida_final} kg no saco\n')

# Minha resolução:

saco = float(input('Peso do saco (kg): '))
gato_1 = float(input('Comida do gato 1 por dia (g): '))
gato_2 = float(input('Comida do gato 2 por dia (g): '))
print(f'Após o quinto dia, resta {saco - ((gato_1 / 1000 + gato_2 / 1000) * 5)} kg no saco')