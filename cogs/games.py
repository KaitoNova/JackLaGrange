import discord
from discord.ext import commands
import random

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.economy = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.economy = self.bot.get_cog("Economy")

    @commands.command()
    async def pileface(self, ctx, bet: int, choice: str):
        if choice.lower() not in ["pile", "face"]:
            await ctx.send("Choisis 'pile' ou 'face'.")
            return

        user_balance = self.economy.get_balance(ctx.author.id)
        if bet > user_balance:
            await ctx.send("Pas assez de coins.")
            return

        result = random.choice(["pile", "face"])
        if choice.lower() == result:
            self.economy.update_balance(ctx.author.id, bet)
            await ctx.send(f"🎉 C'était **{result}** ! Tu gagnes {bet} coins.")
        else:
            self.economy.update_balance(ctx.author.id, -bet)
            await ctx.send(f"😢 C'était **{result}**. Tu perds {bet} coins.")

    @commands.command()
    async def slots(self, ctx, bet: int):
        symbols = ["🍒", "🍋", "🍉", "⭐", "💎"]
        user_balance = self.economy.get_balance(ctx.author.id)
        if bet > user_balance:
            await ctx.send("Pas assez de coins.")
            return

        result = [random.choice(symbols) for _ in range(3)]
        await ctx.send("🎰 | " + " | ".join(result) + " |")

        if len(set(result)) == 1:
            gain = bet * 5
            self.economy.update_balance(ctx.author.id, gain)
            await ctx.send(f"Jackpot ! Tu gagnes {gain} coins.")
        else:
            self.economy.update_balance(ctx.author.id, -bet)
            await ctx.send(f"Pas de chance ! Tu perds {bet} coins.")

async def setup(bot):
    await bot.add_cog(Games(bot))
