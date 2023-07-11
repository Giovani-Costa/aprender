nome_selecao_de_atividade = input("Olá, insira seu nome para prosseguir: ")
print(
    f"Olá {nome_selecao_de_atividade}, seja bem-vindo ao 2º capítulo das minhas atividades."
)
atividade = input("Selecione a atividade que deseja (até Ativade 7 e Desafio 2): ")

if atividade == "Atividade 1":
    # Atividade 1
    print("oi meu nome é giovani")
elif atividade == "Atividade 2":
    # Atividade 2
    print(
        "'oq me preucupa n é o barulho dos maus, mas o silêncio dos bons'-Martin Luther King"
    )
elif atividade == "Atividade 3":
    # Atividade 3
    sentimento = "bem"
    print(f"eu estou me sentindo {sentimento}")
elif atividade == "Atividade 4":
    # Atividade 4
    haiku = """Adrienne enjoys
  Coffee,lots of coding, and
  Teaching you Python"""
    print(f"{haiku}")
elif atividade == "Atividade 5":
    # Atividade 5
    nome = input("nome: ")
    adjetivo = input("adjetivo: ")
    lanche = input("lanche: ")
    numero = input("número: ")
    arvore = input("tipo de árvore: ")
    historia = f"""Oi, meu nome é {nome}.
  Eu gosto muito de {lanche} {adjetivo}!
  Eu gosto tanto que eu tento comer pelo menos {numero} vezes por dia.
  O sabor é ainda melhor quando se comer sob um(a) {arvore}!"""
    print(historia)
elif atividade == "Atividade 6":
    # Atividade 6
    nome = input("nome: ")
    sobrenome = input("sobrenome: ")
    nome_completo = f"{nome} {sobrenome}"
    print(nome_completo)
elif atividade == "Atividade 7":
    # Atividade 7
    # Antes: 80 = "Adrienne"
    nome = "Adrienne"
    # Antes: 98_cookie_39 = "Chocolate chip cookies"
    cookie = "Cookie com gotas de chocolate"
    # Antes: fIrSt_NAMe = 20
    numero = 20
    # Antes: LAST_name = "Blue"
    cor = "Blue"
    # Antes: 309384 = "Adrienne Tacke"
    nome_completo = "Adrienne Tacke"
    # Antes: Hellllooooooooooooo_8392982r = "Software Engineer"
    profissao = "Desenvolvedor"
elif atividade == "Desafio 1":
    # Desafio 1
    print(
        """    (O)
    (OOO)
    (OOOOO)
  (OOOOOOO)
  (OOOOOOOOO)"""
    )
    print(
        """      @@@@
       {  }
      @@@@@@
     {      }
    @@@@@@@@@@
  {            }
      [**]
    [******]
  [*********]"""
    )
else:
    raise ValueError(
        f"Atividade/Desafio não encontrada! Tente certificar-se de que escreveu corretamente ou digitou uma ativade/desafio existente nesse capítulo! Valor recebido: {atividade}"
    )
