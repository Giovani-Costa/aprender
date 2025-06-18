soma = 0
for k in range(1, 1000):
    if k % 2 == 0:
        soma += k
print(f'A resposta é {soma}')
print(soma == 249500)