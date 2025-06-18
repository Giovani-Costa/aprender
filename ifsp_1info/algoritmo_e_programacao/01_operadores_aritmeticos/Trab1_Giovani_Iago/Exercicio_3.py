preco = 0.0 
a_vista = 0.0
a_prazo = 0.0

preco = float(input('Digite o preço do produto: ')) 

a_vista = preco - (preco * 0.05)
a_prazo = preco + (preco * 0.1)

print(f'O preço do produto a vista é: {a_vista}')
print(f'O preço do produto a prazo é: {a_prazo}')