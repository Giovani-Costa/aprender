operacao = input('Qual a operação? Adição (A); Subtração (S); Multiplicação (M); Divisão (D): ').upper()
num1 = int(input('Qual o primeiro número? '))
num2 = int(input('Qual o segundo número? '))

if operacao == 'A':
    resultado = num1 + num2
elif operacao == 'S':
    resultado = num1 - num2
elif operacao == 'M':
    resultado = num1 * num2
elif operacao == 'D':
    if num1 <= 0 or num2 <= 0:
        print('O resultado é zero')
    else:
        resultado = num1 / num2
else:
    print('Operação inválida')

if resultado >= 0:
    print(f'O resultado é: {resultado * -1}')
else:
    print(f'O resultado é: {resultado}')