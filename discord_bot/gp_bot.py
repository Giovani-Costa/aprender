import discord
import random
from key import key

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)
token = key.get("token")


@client.event
async def on_ready():
    print(f"{client.user} está online!")


@client.event
async def on_message(message):
    numero_do_dado = random.randint(1, 6)
    conteudo = message.content
    conteudo_lower = conteudo.lower()

    if message.author == client.user:
        return

    if conteudo_lower.startswith("!online"):
        await message.channel.send("GP Bot está online!")

    elif conteudo_lower.startswith("!regras"):
        await message.channel.send(
            'As regras do serveridor são as seguinte:\n **1-** Você deve manter o "respeito", com os membros não ultrapassando os limites da zuera \n **2-** Você não pode spawmar mensagem para spawnar um pokémon em nenhum outro chat a não ser o Poke-chat \n **3**- Você não pode mandar qualquer coisa que faça referencia a coisas obcenas \n **4-** Você deve colocar áudios estorados em algum bot de músic \n **5-** Você não pode mandar nenhum vírus/malware na central de downloa \n **6-** Caso esteje participando do GP Server, não desrespeitar as regras. Para saber quais são digite: !GP Server regras'
        )

    elif conteudo_lower.startswith("!gp server regras"):
        await message.channel.send(
            "As regras do servidor do minecraft são as seguintes:\n **1-**Proibido o uso de quaisquer armaduras do mod Project E, em caso de estar jogando em um modpack\n **2-** Proibido o assassinato de qualquer pet de qualquer jogador\n **3-** Proibido qualquer tipo de várzea contra qualquer estrutura oficial em alguma vila principal\n **4-** Proibido usar recursos de outros jogadores sem consentimento ou trato\n **5-** Qualquer residência ou estrutura que esteja dentro da vila que foi construída e não esteja dentro da temática da mesma corre o risco de ser destruída\n **6-** Qualquer baú que não está próximo de uma residência ou estrutura pode ser roubado\n **7-**Proibido qualquer dano a uma estrutura oficial ou a uma residência\n **8-** Proibido usa qualquer comando para alterar o tempo do server"
        )
    elif conteudo_lower.startswith("!d6"):
        await message.channel.send(
            f":game_die: Caiu no **{numero_do_dado}** :game_die:"
        )


client.run(token)

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print("Logged on as {0}!".format(self.user))

#     async def on_message(self, message):
#         print("Message from {0.author}: {0.content}".format(message))
#         if message.content == "teste":
#             await message.channel.send("funcioanado")

# async def on_member_join(self, member):
#     guild = member.guild
#     if guild.system_channel is not None:
#         mensagem = f"{member.mention} entrou na {guild.name}"
#         await guild.system_channel.send(mensagem)
