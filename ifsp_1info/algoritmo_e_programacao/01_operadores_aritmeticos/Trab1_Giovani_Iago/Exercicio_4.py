horas = 0.0 
salario_minimo = 0.0
horas_extras = 0.0
salario_bruto = 0.0
salario_final = 0.0
he_receber = 0.0

horas = float(input('Digite a quantidade de horas trabalhadas: ')) 
salario_minimo = float(input('Digite o salário mínimo: ')) 
horas_extras = float(input('Digite a quantidade de extras horas trabalhadas: ')) 

salario_bruto = horas * (salario_minimo / 8)
if horas_extras >= 12:
    he_receber = (horas_extras * (salario_minimo / 4)) + 200
else:
    he_receber = horas_extras * (salario_minimo / 4)

salario_final = salario_bruto + he_receber

print(f'O salário final é de: {salario_final}')