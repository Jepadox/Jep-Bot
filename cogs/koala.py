import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import aiohttp

class Koala(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help="Test",
        brief="Rolls a random koala pic"
    )
    async def koala(self, ctx):
        complete_url = 'https://some-random-api.ml/img/koala'
        
        async with aiohttp.ClientSession() as session:
            async with session.get(complete_url) as response:
                if response.status != 200:
                    return await ctx.send('No koala found :(')

                x = await response.json()

                embed = discord.Embed(
                    title='Random Koala', color=0x7ce4f7, timestamp=ctx.message.created_at)
                embed.set_image(url=x['link'])

                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Koala(bot))