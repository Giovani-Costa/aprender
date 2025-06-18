saldo = 0.0 
dolar = 0.0
euro = 0.0
libra = 0.0

saldo = float(input('Digite seu saldo: '))
dolar = saldo / 5.25
euro = saldo / 6.20
libra = saldo / 7.37

print(f'Seu saldo em dólares é: {dolar:,.2f}')
print(f'Seu saldo em euros é: {euro:,.2f}')
print(f'Seu saldo em libras esterlinas é: {libra:,.2f}')