i = None
while i != 0:
    i = int(input('Digite um número de 1 a 5: '))
    if i == 1:
        print('Um')
    elif i == 2:
        print('Dois')
    elif i == 3:
        print('Três')
    elif i == 4:
        print('Quatro')
    elif i == 5:
        print('Cinco')
    elif i != 0 and i != 1 and i != 2 and i != 3 and i != 4 and i != 5:
        print('Número inválido')