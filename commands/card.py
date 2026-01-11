import discord
from discord.ext import commands
from logic.card_logic import card_throw, card_shuffle, normalize_card_name
from utils.voice import play_audio

@commands.command(name="card", help="Sorteia uma carta aleatória.")
async def card(ctx):
    drawn_card, cards_left, is_special = card_throw()

    card_name = normalize_card_name(drawn_card)

    image_path = f"assets/cards/{card_name}.png"
    audio_path = f"music/{card_name}.mp3"

    embed = discord.Embed(
        title="🃏 Carta sorteada",
        description=f"{drawn_card}\n {cards_left} cartas faltando.",
        color=0xFFDF00
    )

    embed.set_image(url="attachment://card.png")

    image_file = discord.File(image_path, filename="card.png")

    await ctx.reply(
        embed=embed,
        file=image_file
    )

    if is_special:
        await play_audio(ctx, audio_path)


@commands.command(name="shuffle", help="Embaralha o baralho.")
async def shuffle(ctx):
    total = card_shuffle()
    await ctx.send(
        f"🔀 O baralho foi embaralhado!\n"
        f"Total de cartas no baralho: **{total}**"
    )