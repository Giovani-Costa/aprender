# GIOVANI E IAGO

salario_minimo = int(input('Qual o valor salário mínimo?\n'))
turno = input('Qual seu turno?\nM – Matutino\nV – Vespertino\nN – Noturno\n').upper()
categoria = input('\nQual sua categoria?\nO – Operário\nG – Gerente\n').upper()
horas_trabalhadas = int(input('Quantas horas você trabalhou? '))

if turno == 'M':
    salario_bruto = (salario_minimo * 0.10) * horas_trabalhadas
elif turno == 'V':
    salario_bruto = (salario_minimo * 0.15) * horas_trabalhadas
elif turno == 'N':
    salario_bruto = (salario_minimo * 0.12) * horas_trabalhadas

if categoria == 'O' and salario_bruto >= 300:
    salario_liquido = salario_bruto - (salario_bruto * 0.05)
elif categoria == 'O' and salario_bruto < 300:
    salario_liquido = salario_bruto - (salario_bruto * 0.03)
elif categoria == 'G' and salario_bruto >= 400:
    salario_liquido = salario_bruto - (salario_bruto * 0.06)
elif categoria == 'G' and salario_bruto < 400:
    salario_liquido = salario_bruto - (salario_bruto * 0.04)

if turno == 'N' and horas_trabalhadas > 80:
    salario_liquido += 50
else:
    salario_liquido += 30

if categoria == 'O' or horas_trabalhadas <= 25:
    salario_liquido += salario_bruto / 3
else:
    salario_liquido += salario_bruto / 2

if salario_liquido < 350:
    print(f'Você é mal remunerado. ({salario_liquido})')
elif salario_liquido > 350 and salario_liquido < 600:
    print(f'Você é normal. ({salario_liquido})')
elif salario_liquido > 600:
    print(f'Você é bem remunerado. ({salario_liquido})')
    