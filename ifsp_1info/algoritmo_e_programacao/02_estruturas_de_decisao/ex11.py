nome = input('Qual seu nome?: ')
idade = int(input('Qual a sua idade?: '))

if idade <= 5 and idade >= 7:
    print(f'{nome}, você está na classe Infantil A')
elif idade <= 8 and idade >= 11:
    print(f'{nome}, você está na classe Infantil B')
elif idade <= 12 and idade >= 13:
    print(f'{nome}, você está na classe Juvenil A')
elif idade <= 14 and idade >= 17:
    print(f'{nome}, você está na classe Juvenil B')
elif idade < 18:
    print(f'{nome}, você está na classe Adulto')
else:
    print('Idade inválida')