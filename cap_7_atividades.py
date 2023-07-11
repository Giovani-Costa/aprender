# Atividade 1
def poder(nome: str, poder: str) -> None:
    print(f"Oi, meu nome é {nome} e meu poder é {poder}")


poder("Giovani", "Portal")


# Atividade 2
def frase_engracada(cor: str, sobremesa: str) -> None:
    print(
        f"Minha sobre mesa favorita é {cor} porque é muito gostoso e minha cor favorita é {sobremesa} porque sim"
    )


frase_engracada("preto", "bolo")

# Atividade 3
from datetime import datetime, timedelta


def horario_mundial() -> None:
    minha_cidade = datetime.now()
    norman = minha_cidade + timedelta(hours=-2)
    sydney = minha_cidade + timedelta(hours=13)
    tokyo = minha_cidade + timedelta(hours=12)
    budapest = minha_cidade + timedelta(hours=5)
    print(
        f"Em Cardoso são {minha_cidade:%I:%M}, em Norman são {norman:%I:%M}, em Sydney {sydney:%I:%M}, em Tokyo são {tokyo:%I:%M} e em Budapest são {budapest:%I:%M}."
    )


horario_mundial()


# Atividade 4
def fatorial(numero: int) -> int:
    if numero == 1:
        return 1
    return numero * fatorial(numero - 1)


print(fatorial(4))


# Atividade 5
def foobar(numero: int) -> None:
    if numero % 3 == 0 and not numero % 5 == 0:
        print("foo")
    elif numero % 5 == 0 and not numero % 3 == 0:
        print("bar")
    elif numero % 5 == 0 and numero % 3 == 0:
        print("foobar")
    else:
        print(numero)


# for i in range(1, 201):
#   foobar(i)
# Atividade 6


def linha_horizontal(quantidade: int) -> None:
    print(" ---" * quantidade)


def linha_vertical(quantidade: int) -> None:
    print("|   " * quantidade)


tamanho = int(input("Qual o tamanho do tabuleiro? "))
for i in range(tamanho):
    linha_horizontal(tamanho)
    linha_vertical(tamanho + 1)
linha_horizontal(tamanho)

# Atividade 7
from enum import Enum


class Opcoes(Enum):
    PEDRA = "pedra"
    PAPEL = "papel"
    TESOURA = "tesoura"


def parse_opcoes(opcao: str) -> Opcoes:
    opcao = opcao.lower()
    if opcao == "pedra":
        return Opcoes.PEDRA
    elif opcao == "papel":
        return Opcoes.PAPEL
    elif opcao == "tesoura":
        return Opcoes.TESOURA
    else:
        raise ValueError(f"Opção não encontrada! Valor recebido: {opcao}")


def comparar(jogador_1: Opcoes, jogador_2: Opcoes) -> None:
    if jogador_1 == Opcoes.PEDRA:
        if jogador_2 == Opcoes.PEDRA:
            print("Empate")
        elif jogador_2 == Opcoes.PAPEL:
            print("Jogador 2 ganhou")
        elif jogador_2 == Opcoes.TESOURA:
            print("Jogador 1 ganhou")
    if jogador_1 == Opcoes.PAPEL:
        if jogador_2 == Opcoes.PEDRA:
            print("Jogador 1 ganhou")
        elif jogador_2 == Opcoes.PAPEL:
            print("Empatou")
        elif jogador_2 == Opcoes.TESOURA:
            print("Jogador 2 ganhou")
    if jogador_1 == Opcoes.TESOURA:
        if jogador_2 == Opcoes.PEDRA:
            print("Jogador 2 ganhou")
        elif jogador_2 == Opcoes.PAPEL:
            print("Jogador 1 ganhou")
        elif jogador_2 == Opcoes.TESOURA:
            print("Empate")


jogador_1 = parse_opcoes(input("Jogador 1: "))
jogador_2 = parse_opcoes(input("Jogador 2: "))
comparar(jogador_1, jogador_2)

# Desafio 1
from random import choice

tentativas = 6
lista_de_palavras = ["banana", "pera", "uva", "kiwi", "laranja", "tangerina"]
letras = []
segredo = choice(lista_de_palavras)
palavra = segredo
while tentativas > 0:
    letra = input("Qual a letra? ")
    letra = letra.lower()[0]
    letras.append(letra)
    for l in segredo:
        if l in letras:
            print(l, end="")
            palavra = palavra.replace(l, "")
        else:
            print("_", end="")
    if letra not in segredo:
        tentativas -= 1
    if palavra == "":
        print("\nGanhou!")
        break
    print(
        f"\nVocê tem {tentativas} tentivas e você chutou {[l for l in letras if l not in segredo]}"
    )
if tentativas == 0:
    print("Perdeu")
