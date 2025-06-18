pessoas = int(input('Quantas pessoas participaram? '))
altura2m= 0 
alturas = []

for k in range (1, pessoas + 1):
    altura = float(input("Informe a altura: "))
    alturas.append(altura)
    if altura > 2:
        altura2m += 1

print(f"A altura media é: {sum(alturas) / len(alturas)}")
print(f"O numero de pessoas com altura superior a 2 metros: {altura2m}")