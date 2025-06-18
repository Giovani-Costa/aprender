num = int(input('Quantas pessoas estão participando? '))
idades = []
idade_t = 0

for k in range(1, num + 1):
    idade = int(input(f'Qual a idade da {k}º pessoa? '))
    idades.append(idade)
    idades.sort()

print(f'A menor idade é: {min(idades)}\nA maior idade é: {max(idades)}\nA média das idade é: {sum(idades) / num}')

# -----------------------------------------

for k in range(1, num + 1):
    idade = int(input(f'Qual a idade da {k}º pessoa? '))
    idade_t += idade

    if k == 1:
        idade_menor = idade
        idade_maior = idade
    else:
        if idade > idade_maior:
            idade_maior = idade
        elif idade < idade_menor:
            idade_menor = idade

print(f'A menor idade é: {idade_menor}\nA maior idade é: {idade_maior}\nA média das idade é: {idade_t / num}')