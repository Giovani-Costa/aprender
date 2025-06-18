num = None
tabuada = 1
while num != 0:
    num = int(input('Digite um número: '))
    if num != 0:
        while tabuada <= 10:
            print(f'{tabuada}x{num} = {num * tabuada}')
            tabuada += 1
        print('')
        tabuada = 1