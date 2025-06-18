'''
Exercício: Um trabalhador quer saber o seu saldo em sua conta (0) após emitir dois cheques com imposto de 0.38% cade um
Aula: 24/02/2025
'''

# Resolução do professor:

salario = 0.0
cheque1 = 0.0
cheque2 = 0.0
resultado = 0.0

salario = float(input('Salário do trabalhador: '))
cheque1 = float(input('Valor do cheque 1: '))
cheque2= float(input('Valor do cheque 2: '))
resultado = salario - (cheque1 + cheque1 * 0.038) - (cheque2 + cheque2 * 0.038)

print(f'O saldo da conta é: {resultado}\n')

# Minha resolução:

salario = float(input('Salário do trabalhador: '))
cheque1 = float(input('Valor do cheque 1: '))
cheque2= float(input('Valor do cheque 2: '))
print(f'O saldo da conta é:{salario - (cheque1 + cheque1 * 0.038) - (cheque2 + cheque2 * 0.038)}')