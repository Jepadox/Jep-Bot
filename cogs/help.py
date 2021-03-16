import discord
from discord.ext import commands

version = '0.1.3'

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
                    title='JepBot Help', color=0x000080, timestamp=ctx.message.created_at, description="List of JepBot " + version + " commands")
        embed.add_field(name='Animal Pictures', value='`~cat`, `~dog`, `~duck`, `~fox`, `~koala`, `~lizard`, `~panda`, `~redpanda`')

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))