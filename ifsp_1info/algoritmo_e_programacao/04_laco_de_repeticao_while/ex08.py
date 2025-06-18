produto1 = 0
produto2 = 0
produto3 = 0
produto4 = 0
pessoas = 0
produto = None

while produto != 0:
    produto = int(input("Qual seu produto favorito? "))
    if produto == 1:
        produto1 += 1
        pessoas += 1
    elif produto == 2:
        produto2 += 1
        pessoas += 1
    elif produto == 3:
        produto3 += 1
        pessoas += 1
    elif (produto < 1 or produto > 3) and produto != 0:
        print('Produto inválido')

print(f"{produto1 * (100 / pessoas)}% das pessoas preferem o produto 1\n{produto2 * (100 / pessoas)}% das pessoas preferem o produto 2\n{produto3 * (100 / pessoas)}% das pessoas preferem o produto 3")