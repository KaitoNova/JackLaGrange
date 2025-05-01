import discord
from discord.ext import commands
import json
import os

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data_file = "data/users.json"
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.data_file):
            with open(self.data_file, "w") as f:
                json.dump({}, f)
        with open(self.data_file, "r") as f:
            self.users = json.load(f)

    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.users, f, indent=4)

    def get_balance(self, user_id):
        return self.users.get(str(user_id), 100)

    def update_balance(self, user_id, amount):
        uid = str(user_id)
        if uid not in self.users:
            self.users[uid] = 100
        self.users[uid] += amount
        self.save_data()

    @commands.command()
    async def balance(self, ctx):
        money = self.get_balance(ctx.author.id)
        await ctx.send(f"💰 Tu as {money} coins.")

    @commands.command()
    async def give(self, ctx, member: discord.Member, amount: int):
        if amount <= 0:
            await ctx.send("Montant invalide.")
            return
        if self.get_balance(ctx.author.id) < amount:
            await ctx.send("Tu n'as pas assez d'argent.")
            return
        self.update_balance(ctx.author.id, -amount)
        self.update_balance(member.id, amount)
        await ctx.send(f"💸 {ctx.author.display_name} a donné {amount} coins à {member.display_name}.")

async def setup(bot):
    await bot.add_cog(Economy(bot))
