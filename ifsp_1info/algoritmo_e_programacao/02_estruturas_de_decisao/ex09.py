'''
Exercício: Construa um algoritmo que classifica o aumento do salário de um funcionário baseado no seu código e salário
Aula: 07/04/2025
'''

salario = int(input('Digite seu salário: '))
id = int(input('Digite seu código: '))


if id == 1:
    print(f'Seu salário agora é de {salario + (salario * 0.5)}, houve um aumento de {salario * 0.5} no salário de escrituário')
elif id == 2:
    print(f'Seu salário agora é de {salario + (salario * 0.35)}, houve um aumento de {salario * 0.35} no salário de secretário')
elif id == 3:
    print(f'Seu salário agora é de {salario + (salario * 0.2)}, houve um aumento de {salario * 0.2} no salário de caixa')
elif id == 4:
    print(f'Seu salário agora é de {salario + (salario * 0.1)}, houve um aumento de {salario * 0.1} no salário de gerente')
elif id == 5:
    print(f'Seu salário agora é de {salario}, não houve aumento no salário de diretor')
else:
    print(f'Seu código está inválido')