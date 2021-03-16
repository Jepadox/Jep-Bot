import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(
        help="Test",
        brief="Returns your ping in ms"
    )
    async def ping(self, ctx):
        await ctx.send(f'I\'d say about {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(Ping(bot))