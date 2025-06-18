soma = []
vezes = int(input('Quantas vezes vai se repitir? '))
for k in range(1 , vezes+1):
    soma.append(k)
print(f"A soma dos números entre 1 e {vezes} é: {sum(soma)}")
