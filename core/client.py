import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

from commands.card import card
bot.add_command(card)

from commands.coin import coin
bot.add_command(coin)

from commands.dice import on_message as dice_on_message
@bot.event
async def on_message(message):
    await dice_on_message(message)
    await bot.process_commands(message)