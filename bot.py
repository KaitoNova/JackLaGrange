import discord
import os
from discord.ext import commands
import json
import asyncio

# Chargement de la configuration
with open("config.json") as f:
    config = json.load(f)

# Configuration des intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Création de l'instance du bot
bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

# Fonction de chargement des extensions
async def load_extensions():
    await bot.load_extension("cogs.economy")
    await bot.load_extension("cogs.games")
    await bot.load_extension("cogs.auto_bump")

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}.")

# Chargement des extensions avant de lancer le bot
asyncio.run(load_extensions())

# Exécution du bot en utilisant la variable d'environnement 'TOKEN'
bot.run(os.getenv("TOKEN"))
