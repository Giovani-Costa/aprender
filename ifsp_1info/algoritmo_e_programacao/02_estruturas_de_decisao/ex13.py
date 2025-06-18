lado1 = int(input('Qual o primeiro lado do triângulo?: '))
lado2 = int(input('Qual o segundo lado do triângulo?: '))
lado3 = int(input('Qual o terceiro lado do triângulo?: '))

if (lado1 + lado2) > lado3 and (lado2 + lado3) > 1 and (lado1 + lado3) > lado2:
    if lado1 == lado2 == lado3:
        print('Seu triângulo é equilátero')
    elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
        print('Seu triângulo é isóceles')
    elif (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
        print('Seu triângulo é escaleno')
else:
    print('Não foi possível formar um triângulo')