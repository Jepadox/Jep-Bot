import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import aiohttp

class Dog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help="Test",
        brief="Rolls a random dog pic"
    )
    async def dog(self, ctx, *args):
        if not args:
            complete_url = 'https://dog.ceo/api/breeds/image/random'
        else:
            complete_url = 'https://dog.ceo/api/breed/' + '-'.join(args) +'/images/random'
            await ctx.send(complete_url)
        async with aiohttp.ClientSession() as session:
            async with session.get(complete_url) as response:
                if response.status != 200:
                    return await ctx.send('No dog found :(')

                x = await response.json()

                embed = discord.Embed(
                    title='Random Dog', color=0x7ce4f7, timestamp=ctx.message.created_at)
                embed.set_image(url=x['message'])

                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Dog(bot))