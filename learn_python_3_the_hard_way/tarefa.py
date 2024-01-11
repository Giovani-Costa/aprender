# titulo_filmes = []
# for filme in filmes:
#    titulo_filmes.append(filme.titulo)

titulo_filmes = []
for filme in filmes:
    titulo_filmes.append(filme.titulo)

titulo_filmes = [filme.titulo for filme in filmes]


animais_nomes = []
for animal in zoologico:
    animais_nomes.append(animal.nome)

animais_nomes = [animal.nome for animal in zoologico]


animais_aquaticos = []
for animal in zoologico:
    if e_aquatico(animal):
        animais_aquaticos.append(animal)

animais_aquaticos = [animal for animal in zooligico if e_aquatico(animal)]


frutas_vermelhas = []
for fruta in salada_de_frutas:
    if e_vermelha(fruta):
        frutas_vermelhas.append(fruta)

frutas_vermelhas = [fruta for fruta in salada_de_fruta if e_vermelha(fruta)]


alunos_aprovados = []
for aluno in alunos:
    if aluno.nota >= 60:
        alunos_aprovados.append(aluno.nome)

alunos_aprovados = [aluno.nome for aluno in alunos if aluno.nota >= 60]


alunos_notas = {}
for aluno in alunos:
    alunos_notas[aluno.nome] = aluno.nota

alunos_notas = {aluno.nome: aluno.nota for aluno in alunos}


jogos_preco = {}
for jogo in jogos:
    if disponivel_para_windows(jogo):
        jogos_preco[jogo.nome] = jogo.preco

jogos_preco = {jogo.nome: jogo.preco for jogo in jogos if disponivel_para_windows(jogo)}


series_personagem_mapa = {}
for serie in series:
    series_personagem_mapa[serie.nome] = serie.protagonista

series_personagem_mapa = {serie.nome: serie.protanista for serie in series}
