import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import aiohttp

class Duck(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help="Test",
        brief="Rolls a random duck pic"
    )
    async def duck(self, ctx):
        complete_url = 'https://random-d.uk/api/v2/random'
        
        async with aiohttp.ClientSession() as session:
            async with session.get(complete_url) as response:
                if response.status != 200:
                    return await ctx.send('No duck found :(')

                x = await response.json()

                embed = discord.Embed(
                    title='Random Duck', color=0x7ce4f7, timestamp=ctx.message.created_at)
                embed.set_image(url=x['url'])

                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Duck(bot))