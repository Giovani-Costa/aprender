massa_inicial = int(input('Qual a massa inicial do material radioativo? '))
massa = massa_inicial
segundos = 0
while massa >= 0.5:
    massa = massa / 2
    segundos += 60
print(f'A massa inicial era de {massa_inicial}\nA massa final é de: {massa:,.2f}\nForam gastos {segundos} segundos para chegar nessa massa.')