import random
import discord
from discord.ext import commands
from logic.coin_logic import coin_flip

results = [
    "Cara", "Coroa"
]

@commands.command(name="coin", help="Sorteia uma lado da moeda.")
async def coin(ctx):
    coin = coin_flip()

    image_path = f"assets/coins/{coin}.png"

    embed = discord.Embed(
        title="🪙 Moeda lançada para o alto!",
        description=f"A prata disse: {coin}!",
        color=0xFFDF00
    )

    embed.set_image(url="attachment://coin.png")

    image_file = discord.File(image_path, filename="coin.png")

    await ctx.reply(
        embed=embed,
        file=image_file
    )
