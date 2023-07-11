# Atividade 1
minhas_coisas_favoritas = ["computador", "celular", "bicicleta", "paçoca"]
print(f"Minhas coisas favoritas são: {minhas_coisas_favoritas}")
print(f"Minhas coisas favoritas são: {', '.join(minhas_coisas_favoritas)}")
# Atividade 2
minhas_nuvens = ["circulo", "tartaruga", "golfinho", "caminhão", "maçã", "colher"]
nuvens_do_amigo = ["maçã", "tartaruga", "colher", "caminhão", "circulo", "golfinho"]
if minhas_nuvens[0] == nuvens_do_amigo[0]:
    print("A gente viu a mesma coisa")
else:
    print("A gente não viu a mesma coisa")
if minhas_nuvens[1] == nuvens_do_amigo[1]:
    print("A gente viu a mesma coisa")
else:
    print("A gente não viu a mesma coisa")
if minhas_nuvens[2] == nuvens_do_amigo[2]:
    print("A gente viu a mesma coisa")
else:
    print("A gente não viu a mesma coisa")
if minhas_nuvens[3] == nuvens_do_amigo[3]:
    print("A gente viu a mesma coisa")
else:
    print("A gente não viu a mesma coisa")
if minhas_nuvens[4] == nuvens_do_amigo[4]:
    print("A gente viu a mesma coisa")
else:
    print("A gente não viu a mesma coisa")
if minhas_nuvens[5] == nuvens_do_amigo[5]:
    print("A gente viu a mesma coisa")
else:
    print("A gente não viu a mesma coisa")
# Atividade 3
# Cenário 1
futebol = ["chuteira", "bola", "meia", "jogadores", "gol"]
print(futebol[4], futebol[1], "= gol bola")
# Cenário 2
ingredientes_paro_um_bolo = ["ovos", "farinha", "fermento", "manteiga", "açucar"]
print(ingredientes_paro_um_bolo[0], ingredientes_paro_um_bolo[2], "= ovos fermento")
# Cenário 3
letra_de_uma_musica = [
    "com",
    "cinco",
    "ou",
    "seis",
    "retas",
    "é",
    "fácil",
    "fazer",
    "um",
    "castelo",
]
print(letra_de_uma_musica[4], letra_de_uma_musica[5], "= retas é")
# Cenário 4
sports = ["futebol", "basquete", "volei", "corrida", "formula 1", "bola queimada"]
print(sports[2], sports[4], "= volei formula 1")
# Cenário 5
comidas = ["batata", "arroz", "feijão", "cenoura", "carne", "bolo", "paçoca"]
print(comidas[-1], comidas[-2], "= paçoca bolo")
# Cenário 6
jogos = [
    "minecraft",
    "god of war",
    "fortnite",
    "assassin's creed",
    "forza horizon",
    "genshin impact",
]
print(jogos[0], jogos[2], "= minecraft fortnite")
# Atividade 4
pet_parade_order = [
    "Pete the Pug",
    "Sally the Siamese Cat",
    "Beau the Boxer",
    "Lulu the Labrador",
    "Lily the Lynx",
    "Pauline the Parrot",
    "Gina the Gerbil",
    "Tubby the Tabby Cat",
]
pet_parade_order.remove("Gina the Gerbil")
pet_parade_order.remove("Pauline the Parrot")
pet_parade_order.reverse()
pet_parade_order.append("Pauline the Parrot")
pet_parade_order.reverse()
troca_1 = pet_parade_order[4]
troca_2 = pet_parade_order[5]
pet_parade_order[5] = troca_1
pet_parade_order[4] = troca_2
del pet_parade_order[1:4]
print("Esse é o desfile dos animais:", pet_parade_order)
# Atividade 5
ano = 2023
if ano == 2023:
    print(
        f"O ano é {ano}, eu tenho {ano - 2010}. Eu vou estar estudando Dirce Libano dos Santos, meu passatempo favorito é jogar"
    )
elif ano == 2028:
    print(
        f"O ano é {ano}, eu tenho {ano - 2010}. Eu vou estar estudando na E.T.E.C ou no Instituto Federal, meu passatempo favorito é jogar"
    )
elif ano == 2033:
    print(
        f"O ano é {ano}, eu tenho {ano - 2010}. Eu vou estar trabalhando Epic Games, meu passatempo favorito é jogar"
    )
else:
    print(
        f"O ano é {ano}, eu tenho {ano - 2010}. Eu vou estar trabalhando Mojang, meu passatempo favorito é jogar"
    )
# Atividade 6
crate_1 = ["onions", "peppers", "mushrooms", "apples", "peaches"]
crate_2 = ["lemons", "limes", "broccoli", "cauliflower", "tangerines"]
crate_3 = ["squash", "potatoes", "cherries", "cucumbers", "carrots"]
dicing = [crate_1[0], *crate_2[2:4], *crate_3[0:2], *crate_3[3:5]]
slicing = [*crate_1, *crate_2[0:2], crate_2[4], crate_3[2]]
print(dicing)
print(slicing)
# Atividade 7
informacao_pessoal = ("Giovani", "da Costa Silva", "Castanho", "Preto")
jogos_favoritos = ["Minecraft", "Fortnite", "Blox Fruits", "Allusions"]
cores_do_arcoiris = (
    "Vermelho",
    "Laranja",
    "Amarelo",
    "Verde",
    "Azul",
    "Anil",
    "Violeta",
)
# Desafio 1
nome = input("Seu nome é: ")
print(
    f"Bem-vindo ao jogo Escolha a Sua Aventura de {nome}! Conforme você segue a história, você será presenteado com escolhas que decidirão seu destino. Tome cuidado e escolha sabiamente! Vamos começar."
)
print(
    "Você se encontra em um quarto escuro com 2 portas. A primeira porta é vermelha, a segunda é branca!"
)
porta = input(
    "Qual porta você deseja escolher? vermelha=porta vermelha ou branca=porta branca"
)
if porta == "branca":
    print(
        "Ótimo, você entrou pela porta branca e agora está no passado! Você conhece uma princesa que pede para você ir em uma missão."
    )
    escolha = input(
        "Você quer aceitar a oferta dela e partir para a missão, ou quer ficar onde está? 1=Aceite e vá para a missão ou 2=Fique"
    )
    if escolha == "1":
        print("A princesa agradece por aceitar sua oferta. Você começa a missão.")
    else:
        print(
            """___FIM DO JOGO__
Bem, acho que sua história termina aqui!"""
        )
else:
    print(
        "Ótimo, você entra pela porta vermelha e agora está no futuro! Você conhece um cientista que lhe dá a missão de ajudá-lo a salvar o mundo!"
    )
    escolha = input("O que você quer fazer? 1=Aceitar ou 2=Recusar")
    if escolha == "1":
        print(
            """___SUCESSO__
Você ajudou o cientista a salvar o mundo! Em
gratidão, o cientista constrói uma máquina do tempo e
te manda para casa!"""
        )
    else:
        print(
            """__FIM DE JOGO__
Muito ruim! Você recusou a oferta do cientista e agora
você está preso no futuro!"""
        )
