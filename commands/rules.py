from discord.ext import commands
from core.rag import answer_question
import discord

@commands.command(name="rules")
async def rules(ctx, *, question):
    loading_embed = discord.Embed(
        title="📖 Consultando o Livro do Sacramento...",
        description="O xerife está folheando as páginas...",
        color=0x8B4513
    )
    message = await ctx.send(embed=loading_embed)

    try:
        answer = answer_question(question)

        response_embed = discord.Embed(
            title="🤠 Regra Encontrada",
            description=answer,
            color=0xC19A6B
        )
        response_embed.set_footer(
            text="Sacramento RPG • O Velho Oeste não perdoa"
        )

        await message.edit(embed=response_embed)

    except Exception as e:
        # Check if it's a 429 RESOURCE_EXHAUSTED error from Google API
        error_str = str(e).lower()
        if "resource_exhausted" in error_str or ("429" in error_str and "exhausted" in error_str):
            error_embed = discord.Embed(
                title="Calma-la, cowboy! 🐎",
                description="Você está fazendo perguntas rápido demais. Me dá só um minutinho!",
                color=0xFFD700
            )
        else:
            error_embed = discord.Embed(
                title="💥 Algo deu errado...",
                description="O revólver emperrou ao consultar o livro.",
                color=0x8B0000
            )
        await message.edit(embed=error_embed)
        print(e)
