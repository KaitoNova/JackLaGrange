import discord
from discord.ext import commands, tasks
import json
import time

class AutoBump(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("config.json") as f:
            self.config = json.load(f)
        self.last_bump = 0
        self.bump_loop.start()

    @tasks.loop(minutes=1)
    async def bump_loop(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(self.config["bump_channel_id"])
        if channel:
            now = time.time()
            if now - self.last_bump >= self.config["bump_interval_minutes"] * 60:
                await channel.send("!d bump")
                self.last_bump = now

async def setup(bot):
    await bot.add_cog(AutoBump(bot))
