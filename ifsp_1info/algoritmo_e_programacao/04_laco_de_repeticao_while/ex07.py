filhos = []
salarios = []
salarios_100 = []
continuar = 1
while continuar == 1:
    print('')
    filhos.append(int(input("Quantos filhos você têm? ")))
    salario = int(input("Qual o seu salário? "))
    salarios.append(salario)
    
    if salario >= 100:
        salarios_100.append(salario)
    
    continuar = int(input('Digite 1 se gostaria de continuar e 2 caso queira sair: '))
print(f'\nA média do salário da população: R$ {(sum(salarios) / len(salarios)):,.2f}.\nA média de filhos da população: {sum(filhos) / len(filhos)}.\nO maior salário da população é de: {max(salarios)}.\n{len(salarios_100) * (100 / len(salarios))}% da população ganha acima de R$ 100.')