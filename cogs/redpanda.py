import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import aiohttp

class Redpanda(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help="Test",
        brief="Rolls a random red panda pic"
    )
    async def redpanda(self, ctx):
        complete_url = 'https://some-random-api.ml/img/red_panda'
        
        async with aiohttp.ClientSession() as session:
            async with session.get(complete_url) as response:
                if response.status != 200:
                    return await ctx.send('No red panda found :(')

                x = await response.json()

                embed = discord.Embed(
                    title='Random red Panda', color=0x7ce4f7, timestamp=ctx.message.created_at)
                embed.set_image(url=x['link'])

                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Redpanda(bot))