'''
Exercício: Construa um algoritmo que classifique o solo
Aula: 07/04/2025
'''

agua = int(input('Digite o nível de água do solo: '))

if agua >= 10:
    print(f'O solo é rochoso')
elif agua > 10 and agua < 40:
    print(f'O solo é firme')
elif agua > 40 and agua <= 80:
    print(f'O solo é pantanoso')
elif agua > 80:
    print(f'Quantidade inválida')