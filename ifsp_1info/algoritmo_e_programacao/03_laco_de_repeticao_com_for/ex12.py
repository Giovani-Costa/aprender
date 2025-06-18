a = 0
e = 0
i = 0
o = 0
u = 0
consoantes = 0

for k in range(1, 21):
    letra = input('Digite uma letra: ').lower()
    if letra == 'a':
        a =+ 1
    elif letra == 'e':
        e =+ 1
    elif letra == 'i':
        i =+ 1
    elif letra == 'o':
        o =+ 1
    elif letra == 'u':
        u =+ 1    
    else:
        consoantes += 1
print(f"Foram digitados: \n{a} A's\n{e} E's\n{i} I's\n{o} O's\n{u} U's\n{consoantes} consoantes.")