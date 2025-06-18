salario = int(input('Qual seu salário atual?: '))
ac_bon = 0

if salario < 500:
    ac_bon = salario * 0.05
elif salario >= 500 and salario <= 1200:
    ac_bon = salario * 0.12

if salario <= 600:
    salario += 150
elif salario >= 600:
    salario += 100

print(f'Seu novo salário é de {salario + ac_bon}')