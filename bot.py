import discord
import os
from discord.ext import commands
import json

# Charger la configuration du bot depuis le fichier JSON
with open("config.json") as f:
    config = json.load(f)

# Définir les intents pour que le bot puisse accéder aux messages
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Créer une classe personnalisée pour le bot
class JackBot(commands.Bot):
    async def setup_hook(self):
        # Charger les extensions ici
        await self.load_extension("cogs.economy")
        await self.load_extension("cogs.games")
        await self.load_extension("cogs.auto_bump")

# Créer une instance du bot avec la classe personnalisée
bot = JackBot(command_prefix=config["prefix"], intents=intents)

# Quand le bot est prêt, afficher un message de connexion
@bot.event
async def on_ready():
    print(f"Jack est prêt dans La Grange ! Connecté en tant que {bot.user}.")

# Lancer le bot avec le token récupéré depuis les variables d'environnement
bot.run(os.getenv("TOKEN"))
