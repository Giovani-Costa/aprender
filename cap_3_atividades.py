# Atividade 1
nome = "Giovani"
idade = 24 / 2
print(f"Meu nome é {nome} e tenho {idade} anos")
# Atividade 2
numero_magico = (70 % 6) ** 3 * 5 + 13  # 333
print(numero_magico)
# Atividade 3
# Dolores & Teddy
dolores_gotas_de_chocolate = 13
teddy_gotas_de_chocolates = 9
print(
    f"Dolores tem mais gotas que Teddy. Essa afirmação é {dolores_gotas_de_chocolate>teddy_gotas_de_chocolates}."
)
# Rey & Finn
rey_gotas_de_chocolate = 10
finn_gotas_de_chocolate = 18
print(
    f"Rey tem menos ou igual gotas de chocolate que Finn. Essa afirmação é {rey_gotas_de_chocolate<=finn_gotas_de_chocolate}."
)
# Tom e Jerry
tom_gotas_de_chocolate = 50
jerry_gotas_de_chocolate = "50"
print(
    f"Tom e Jerry não tem a mesma quantidade. Essa afirmação é {tom_gotas_de_chocolate!=jerry_gotas_de_chocolate}."
)
# Trinity & Neo
trinity_gotas_de_chocolate = 3
neo_gotas_de_chocolate = 3
print(
    f"Neo tem a mesma quantidade que Trinity. Essa afirmação é {trinity_gotas_de_chocolate==neo_gotas_de_chocolate}."
)
# Gigi & Kiki
gigi_gotas_de_chocolate = 31
kiki_gotas_de_chocolate = 30
print(
    f"Kiki tem menos que Gigi. Essa afirmação é {kiki_gotas_de_chocolate<gigi_gotas_de_chocolate}."
)
# Bernard & Elsie
bernard_gotas_de_chocolate = 1010
elsie_gotas_de_chocolate = 10101
print(
    f"Bernard tem pelo menos o mesmo que Elsie, mas talvez mais. Essa afirmação é {bernard_gotas_de_chocolate>=elsie_gotas_de_chocolate}."
)
# Atividade 4
total_pessoas = 124
bolacha_maizena = ("bolacha de maizena", 40)
wafer_baunilha = ("wafer de baunilha", 64)
oreo = ("oreo", 20)
tortas = {
    "chocolate e caramelo": {"borda": bolacha_maizena, "pedaços": 10},
    "frutas vermelhas": {"borda": wafer_baunilha, "pedaços": 12},
    "abobora": {"borda": bolacha_maizena, "pedaços": 12},
    "maça": {"borda": wafer_baunilha, "pedaços": 10},
    "banana": {"borda": wafer_baunilha, "pedaços": 10},
    "manga": {"borda": bolacha_maizena, "pedaços": 12},
    "s'mores": {"borda": oreo, "pedaços": 12},
}
for k, v in tortas.items():
    print(
        f"A torta de {k} pode ser divida igualmente entre os amantes de {v['borda'][0]}? {v['borda'][1]%v['pedaços']==0}"
    )
