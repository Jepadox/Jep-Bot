import discord
from discord.ext import commands

version = '0.2.0'

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
                    title='JepBot Help', color=0x000080, timestamp=ctx.message.created_at, description="List of JepBot " + version + " commands")
        embed.add_field(name='`~ANIMAL`', value='Call a random image of a requested animal\n' +
        '`~cat`, `~dog`, `~dog <breedname>`, `~duck`, `~fox`, `~koala`, `~lizard`, `~panda`, `~redpanda`')
        embed.add_field(name='`~PING`', value='Returns ping in ms', inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))