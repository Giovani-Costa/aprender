continuar = None
total = 0.0
hamburger = 0
cheeseburger = 0
misto_quente = 0
americano = 0
queijo_prato = 0
comanda = f'Foram comprados:\n'
print('\nCódigo |    Produto    | Preço |\n   H   |   Hamburger   |  1.50 |\n   C   |  Cheeseburger |  1.80 |\n   M   |  Misto Quente |  1.20 |\n   A   |   Americano   |  2.00 |\n   Q   | Queijo Prato  |  1.00 |\n')

while continuar != 'x':
    produto = input('Digite o código do produto: ').lower()
    if produto == 'h':
        hamburger += 1
        total += 1.5
        print('Hamburger adicionado na comanda!')
    elif produto == 'c':
        cheeseburger += 1
        total += 1.8
        print('Cheeseburger adicionado na comanda!')
    elif produto == 'm':
        misto_quente += 1
        total += 1.2
        print('Misto Quente adicionado na comanda!')
    elif produto == 'a':
        americano += 1
        total += 2.0
        print('Americano adicionado na comanda!')
    elif produto == 'q':
        queijo_prato += 1
        total += 1.0
        print('Queijo Prato adicionado na comanda!')
    elif produto == 'x':
        break
    else:
        print('Código Inválido!')

if hamburger > 0:
    comanda += f'{hamburger}x Hamburger\n'
if cheeseburger > 0:
    comanda += f'{cheeseburger}x Cheeseburger\n'
if misto_quente > 0:
    comanda += f'{misto_quente}x Misto Quente\n'
if queijo_prato > 0:
    comanda += f'{queijo_prato}x Queijo Prato\n'
if americano > 0:
    comanda += f'{americano}x Americano\n'

print(f'\n{comanda}\nO total a ser paga é {total}')