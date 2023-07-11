# Atividade 1
nomes = ["Giovani", "Ana", "Gabriel", "João", "Pedro"]
sobremesas = ["Goiabada", "Paçoca", "Brigadeiro", "Chocalate", "Pé de moleque"]
for nome in nomes:
    for sobremesa in sobremesas:
        print(f"Oi, meu nome é {nome} e minha sobremesa favorita é {sobremesa}.")
# Atividade 2
amigos = [
    "atlético",
    "não atlético",
    "mais velho",
    "atlético",
    "mais jovem",
    "atlético",
    "não atlético",
    "mais velho",
    "atlético",
    "mais velho",
    "atlético",
]
balanco = 0
basquete = 0
for amigo in amigos:
    if amigo == "atlético" or amigo == "mais jovem":
        balanco += 1
    elif amigo == "não atlético" or amigo == "mais velho":
        basquete += 1
print(f"{balanco} foram para o balanço, e {basquete} foram para o basquete.")
# Atividade 3
tem_0_perna = 0
tem_2_perna = 0
tem_4_perna = 0
alce = 4
cobra = 0
pinguim = 2
leao = 4
macaco = 2
golfinho = 0
urso = 2
elefante = 4
girafa = 4
coala = 2
tubarao = 0
canguru = 2
dragao_de_komodo = 4
animais = [
    alce,
    cobra,
    pinguim,
    leao,
    macaco,
    golfinho,
    urso,
    elefante,
    girafa,
    coala,
    tubarao,
    canguru,
    dragao_de_komodo,
]
for animal in animais:
    if animal == 0:
        tem_0_perna += 1
    elif animal == 2:
        tem_2_perna += 1
    elif animal == 4:
        tem_4_perna += 1
print(
    f"{tem_4_perna} animais tem 4 pernas, {tem_2_perna} animais tem 2 pernas e {tem_0_perna} animais não tem nenhuma perna."
)
# Atividade 4
senha = "1"
while input("Digite a senha: ") != senha:
    print("Senha Incorreta")
print("Senha correta!")
# Atividade 5
import random

valor_aleatorio = random.randint(1, 10)
print(valor_aleatorio)
vidas = 3
while vidas > 0:
    numero = int(input("Qual o número? "))
    if numero == valor_aleatorio:
        print("Acertou!")
        break
    else:
        print("Errou")
        vidas -= 1
if vidas == 0:
    print("Acabou suas vidas")
# Atividades 6
palavra = input("Digite uma palavra: ")
a = 0
e = 0
i = 0
o = 0
u = 0
for letra in palavra.lower():
    if letra == "a":
        a += 1
    elif letra == "e":
        e += 1
    elif letra == "i":
        i += 1
    elif letra == "o":
        o += 1
    elif letra == "u":
        u += 1
print(f"Na palavra que você escolheu tem {a} A's, {e} E's, {i} I's, {o} O's e {u} U's")
# Desafio 1
cookies = [
    "R6",
    "C5",
    "C3",
    "C8",
    "R7",
    "R7",
    "C6",
    "C9",
    "C10",
    "R8",
    "C2",
    "C7",
    "R4",
]
maximo = "C0"
for cookie in cookies:
    if cookie[0] == "C":
        if int(cookie[1:]) > int(maximo[1:]):
            maximo = cookie
print(f"O melhor cookie é o {maximo}")
# Desafio 2
numero_aleatorio = random.randint(1, 20)
vidas_2 = 6
while vidas_2 > 0:
    numero = int(input("Qual o número? "))
    if numero == numero_aleatorio:
        print("Acertou!")
        break
    else:
        vidas_2 -= 1
        if numero_aleatorio < numero:
            print(f"Errou, vc ainda tem {vidas_2} vidas e o número é menor q {numero}")
        else:
            print(f"Errou, vc ainda tem {vidas_2} vidas e o número é maior q {numero}")
if vidas_2 == 0:
    print("Acabou suas vidas")
