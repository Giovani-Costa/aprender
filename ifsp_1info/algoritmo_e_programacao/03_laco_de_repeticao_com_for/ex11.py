vogais = 0
consoantes = 0
for k in range(1, 21):
    letra = input('Digite uma letra: ').lower()
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        vogais += 1
        print(f'{letra.upper()} é uma vogal')
    else:
        consoantes += 1
        print(f'{letra.upper()} é uma consoante')
print(f'Foram digitados {vogais} vogais e {consoantes} consoantes.')