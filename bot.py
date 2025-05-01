import discord
import os
from discord.ext import commands
import json
import asyncio

with open("config.json") as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

async def load_extensions():
    await bot.load_extension("cogs.economy")
    await bot.load_extension("cogs.games")
    await bot.load_extension("cogs.auto_bump")

@bot.event
async def on_ready():
    print(f"Jack est prêt dans La Grange ! Connecté en tant que {bot.user}.")

asyncio.run(load_extensions())
bot.run(os.getenv("TOKEN"))
