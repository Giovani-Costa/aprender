pessoas = int(input(f'Quantas pessoas participaram? '))
produto_1 = 0
produto_2 = 0
produto_3 = 0

for k in range(1, pessoas+1):
    opniao = int(input('Qual é melhor? Produto Um (1); Produto Dois (2); Produto Três (3): '))
    if opniao == 1:
        produto_1 += 1
    elif opniao == 2:
        produto_2 += 1
    elif opniao == 3:
        produto_3 += 1

print(f'{produto_1} pessoas preferiram o Produto Um\n{produto_2} pessoas preferiram o Produto Dois\n{produto_3} pessoas preferiram o Produto Três')