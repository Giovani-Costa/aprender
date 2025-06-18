apto = 0
n_apto = 0
situacao = None

while situacao != 'não':
    nome = input('Informe seu nome: ')
    sexo = input('Informe seu sexo: ').lower()
    idade = int(input('Informe sua idade: '))
    saude = input('Informe sua saúde: ').lower()
    if sexo == 'masculino' or sexo == 'm':
        if idade < 18:
            print(f'O candidato {nome} está apta a servir ao exército por ser menor de idade')
            n_apto += 1
        else:
            if saude == 'boa':
                print(f'O candidato {nome} é apto a servir o exército')
                apto += 1
            else:
                print(f'A candidata {nome} está apta a servir ao exército por motivos de saúde')
                n_apto += 1         
    elif sexo == 'feminino' or sexo == 'f':
        print(f'A candidata {nome} está apta a servir ao exército por ser do sexo feminino')
        n_apto += 1
    situacao = input('Gostaria de verificar se outro candidato está apto? ').lower()
print(f'\nO número de pessoas aptas é de: {apto}\nO número de pessoas nâo aptas é de: {n_apto}')