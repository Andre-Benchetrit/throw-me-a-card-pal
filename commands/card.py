import random
from discord.ext import commands

cards = [
    "A de Copas", "2 de Copas", "3 de Copas", "4 de Copas", "5 de Copas", "6 de Copas", "7 de Copas", "8 de Copas", "9 de Copas", "10 de Copas", "Valete de Copas", "Dama de Copas", "Rei de Copas", 
    "A de Ouro", "2 de Ouro", "3 de Ouro", "4 de Ouro", "5 de Ouro", "6 de Ouro", "7 de Ouro", "8 de Ouro", "9 de Ouro", "10 de Ouro", "Valete de Ouro", "Dama de Ouro", "Rei de Ouro", 
    "A de Paus", "2 de Paus", "3 de Paus", "4 de Paus", "5 de Paus", "6 de Paus", "7 de Paus", "8 de Paus", "9 de Paus", "10 de Paus", "Valete de Paus", "Dama de Paus", "Rei de Paus",
    "A de Espadas", "2 de Espadas", "3 de Espadas", "4 de Espadas", "5 de Espadas", "6 de Espadas", "7 de Espadas", "8 de Espadas", "9 de Espadas", "10 de Espadas", "Valete de Espadas", "Dama de Espadas", "Rei de Espadas"
]

deck = []

@commands.command(name="card", help="Sorteia uma carta aleatória.")
async def card(ctx):
    global deck

    if not deck:
        deck = cards.copy()
        random.shuffle(deck)

    card = deck.pop()
    await ctx.send(f"A carta sorteada foi: {card}")
    

@commands.command(name="shuffle", help="Embaralha o baralho.")
async def shuffle(ctx):
    global deck
    deck = cards.copy()
    random.shuffle(deck)
    await ctx.send("O baralho foi embaralhado.")