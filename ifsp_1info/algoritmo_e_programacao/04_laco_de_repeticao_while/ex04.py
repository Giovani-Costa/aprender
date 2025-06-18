num = None
num_lista = []
while num != 0:
    num = int(input('Digite um número: '))
    if num != 0:
        num_lista.append(num)
print(f"O maior número digitado foi: {max(num_lista)}\nO menor número digitado foi: {min(num_lista)}")