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
# Atividade 5
ana_vestido_cor = "rosa"
ana_sapato_cor = "branco"
ana_tem_brincos = True
maria_vestido_cor = "roxo"
maria_sapato_cor = "rosa"
maria_tem_brincos = True
print(
    f"Ana tem uma cor de vestido diferente de Maria? {ana_vestido_cor != maria_vestido_cor}"
)
print(f"As duas estão usando brincos? {maria_tem_brincos and ana_tem_brincos}")
print(
    f"Pelo menos alguém esta usando rosa? {ana_vestido_cor == 'rosa'or ana_sapato_cor == 'rosa'or maria_sapato_cor == 'rosa' or maria_vestido_cor == 'rosa'}"
)
print(
    f"Ninguém está usando verde? {ana_vestido_cor != 'verde'and ana_sapato_cor != 'verde'and maria_sapato_cor != 'verde' and maria_vestido_cor != 'verde'}"
)
print(f"Ana e Maria tem a mesma cor de sapatos? {maria_sapato_cor == ana_sapato_cor}")
# Atividade 6
beakers = 20
tubo_de_ensaio = 30
luvas_de_borracha = 10
oculos_de_protecao = 4
# Uma pessoa precisa de um par de oculos, duas luvas de borracha, 5 beakers e 10 tubos de ensaio
amigos = 4
oculos_de_protecao_e_suficiente = oculos_de_protecao >= 1 * amigos
beakers_e_suficiente = beakers >= 5 * amigos
luvas_de_borracha_e_suficiente = luvas_de_borracha >= 2 * amigos
tubo_de_ensaio_e_suficiente = tubo_de_ensaio >= 10 * amigos
relatorio_final = f"""
Relatório final: 

Cada amigo têm óculos de proteção o suficiente: {oculos_de_protecao_e_suficiente}
Cada amigo têm luvas de borrachas o suficiente: {luvas_de_borracha_e_suficiente}
Cada amigo têm tubos de ensaio o suficiente: {tubo_de_ensaio_e_suficiente}
Cada amigo têm beakers o suficiente: {beakers_e_suficiente}

Cada amigo têm luvas de borracha e óculos de proteção o suficiente: {luvas_de_borracha_e_suficiente and oculos_de_protecao_e_suficiente}
Cada amigo têm tubo de ensaio ou beakers o suficiente: {tubo_de_ensaio_e_suficiente or beakers_e_suficiente}
Cada amigo têm óculos de proteção e beakers ou tubos de ensaio e beakers o suficiente: {beakers_e_suficiente and (tubo_de_ensaio_e_suficiente or oculos_de_protecao_e_suficiente)}
Cada amigo têm todos o suficiente: {oculos_de_protecao_e_suficiente and tubo_de_ensaio_e_suficiente and beakers_e_suficiente and luvas_de_borracha_e_suficiente}"""
print(relatorio_final)

# Atividade 7
print(12345 % 88)

# Atividade 8
planetas = 8
numero_magico_pentatopia = 5
print(f"A galáxia de Pentatopia tem {planetas **numero_magico_pentatopia} planetas")
numero_magico_tripolia = 3
print(f"A galáxia de Tripoloia tem {planetas **numero_magico_tripolia} planetas")
numero_magico_deka = 10
print(f"A galáxia de Deka tem {planetas**numero_magico_deka} planetas")
numero_magico_heptaton = 7
print(f"A galáxia de Heptaton tem {planetas**numero_magico_heptaton} planetas")
numero_magico_oktopia = 8
print(f"A galáxia de Oktopia tem {planetas**numero_magico_oktopia} planetas")
