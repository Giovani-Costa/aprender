'''
Exercício: Converta as medidas
Aula: 24/02/2025
'''


# Resolução do professor:

unidade = 0.0
polegada = 0.0
jarda = 0.0
milha = 0.0

unidade = float(input('Unidade: '))
polegada = unidade * 12
jarda = unidade / 3
milha = jarda / 1760

print(f'{unidade} pé(s) equivale a: {polegada} polegadas')
print(f'{unidade} pé(s) equivale a: {jarda:,.02f} jardas')
print(f'{unidade} pé(s) equivale a: {milha:,.05f} milhas\n')

# Minha resolução:

unidade = float(input('Unidade: '))
print(f'{unidade} pé(s) equivale a: {unidade * 12} polegadas\n{unidade} pé(s) equivale a: {unidade / 3} jardas\n{unidade} pé(s) equivale a: {(unidade / 3) / 1760} milhas')