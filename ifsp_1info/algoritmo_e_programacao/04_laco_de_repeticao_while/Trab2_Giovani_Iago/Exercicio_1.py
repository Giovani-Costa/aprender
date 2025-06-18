# GIOVANI E IAGO

candidato_1_nome = None
candidato_1_votos = 0
candidato_2_nome = None
candidato_2_votos = 0
candidato_3_nome = None
candidato_3_votos = 0
branco = 0
nulo = 0

candidato_1_nome = input('Qual o nome do candidato 1: ')
candidato_2_nome = input('Qual o nome do candidato 2: ')
candidato_3_nome = input('Qual o nome do candidato 3: ')
candidato_vencedor_nome = None
candidato_vencedor_numero = 0

voto = 0
votos = 0
while voto != -1:
    voto = int(input(f'\nQual seu voto?\n1 - {candidato_1_nome}\n2 - {candidato_2_nome}\n3 - {candidato_3_nome}\n0 - Branco\n4 - Nulo\n\nSe quiser encerrar a votação digite "-1"\n'))
    if voto == 1: 
        candidato_1_votos += 1
        votos += 1
    elif voto == 2:
        candidato_2_votos += 1
        votos += 1
    elif voto == 3:
        candidato_3_votos += 1
        votos += 1
    elif voto == 0:
        branco += 1
        votos += 1
    elif voto == 4:
        nulo += 1
        votos += 1
    elif voto != 1 or voto != 2 or voto != 3 or voto != 4 or voto != 0 or voto != -1:
        print('Número inválido. Tente novamente\n')
if candidato_1_votos > candidato_2_votos and candidato_1_votos > candidato_3_votos:
    print(f'O candidato {candidato_1_nome} (1) venceu com {candidato_1_votos} votos!\nNúmero de votos em branco: {branco}\nNúmero de votos nulos: {nulo}\n{votos} eleitores votaram.')
elif candidato_2_votos > candidato_1_votos and candidato_2_votos > candidato_3_votos:
    print(f'O candidato {candidato_2_nome} (2) venceu com {candidato_2_votos} votos!\nNúmero de votos em branco: {branco}\nNúmero de votos nulos: {nulo}\n{votos} eleitores votaram.')
elif candidato_3_votos > candidato_1_votos and candidato_3_votos > candidato_2_votos:
    print(f'O candidato {candidato_3_nome} (3) venceu com {candidato_3_votos} votos!\nNúmero de votos em branco: {branco}\nNúmero de votos nulos: {nulo}\n{votos} eleitores votaram.')
elif candidato_1_votos == candidato_2_votos == candidato_3_votos:
    print(f'Houve um empate entre os 3 candidatos, {candidato_1_nome} (1), {candidato_2_nome} (2), {candidato_3_nome} (3). Ambos tiveram {candidato_1_votos} votos.\nNúmero de votos em branco: {branco}\nNúmero de votos nulos: {nulo}\n{votos} eleitores votaram.')
elif candidato_1_votos == candidato_2_votos:
    print(f'Houve um empate entre 2 candidatos, {candidato_1_nome} (1) e {candidato_2_nome} (2). Ambos tiveram {candidato_2_votos} votos.\nNúmero de votos em branco: {branco}\nNúmero de votos nulos: {nulo}\n{votos} eleitores votaram.')
elif candidato_1_votos == candidato_3_votos:
    print(f'Houve um empate entre 2 candidatos, {candidato_1_nome} (1) e {candidato_3_nome} (3). Ambos tiveram {candidato_1_votos} votos.\nNúmero de votos em branco: {branco}\nNúmero de votos nulos: {nulo}\n{votos} eleitores votaram.')
elif candidato_2_votos == candidato_3_votos:
    print(f'Houve um empate entre 2 candidatos, {candidato_2_nome} (2) e {candidato_3_nome} (3). Ambos tiveram {candidato_2_votos} votos.\nNúmero de votos em branco: {branco}\nNúmero de votos nulos: {nulo}\n{votos} eleitores votaram.')