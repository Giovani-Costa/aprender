num_lista = []
vezes = int(input('Quantas vezes vai se repitir? '))
for k in range(1 , vezes+1):
    num = int(input("Informe um número: "))
    num_lista.append(num)
print(f"\nO menor numero é {min(num_lista)}\nO maior numero é {max(num_lista)}")