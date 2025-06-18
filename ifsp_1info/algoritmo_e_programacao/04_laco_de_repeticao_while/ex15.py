numeros = 0
cont = 0
num = 1
while num >= 0:
    num = int(input('Digite um número inteiro positivo: '))
    if num >= 0:
        cont += 1
        numeros += num
print(f'A média dos números citados é: {numeros / cont}')