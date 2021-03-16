import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import aiohttp

class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help="Test",
        brief="Dev commands for terminal data",
    )

    # (self, ctx) no arguments needed
    # (self, ctx, arg1, arg2, etc..) list amount of arguments taken, separated by space, quotes make one arg "this is one arg"
    # (self, ctx, *args) take all arguments and put them in library args 
    # (self, ctx, *, args) take all arguments as one arg 

    async def test(self, ctx, *args):
        if args[0] == 'cat':
            apiCall = 'https://api.thecatapi.com/v1/images/search'
            jsonLinkTag = 'url'
        elif args[0] == 'dog':
            if len(args) > 1:
                apiCall = 'https://dog.ceo/api/breed/' + args[1] +'/images/random'
                jsonLinkTag = 'message'
            else:
                apiCall = 'https://dog.ceo/api/breeds/image/random'
                jsonLinkTag = 'message'
        elif args[0] == 'duck':
            apiCall = 'https://random-d.uk/api/v2/random'
            jsonLinkTag = 'url'
        elif args[0] == 'fox':
            apiCall = 'https://randomfox.ca/floof'
            jsonLinkTag = 'image'
        elif args[0] == 'koala':
            apiCall = 'https://some-random-api.ml/img/koala'
            jsonLinkTag = 'link'
        elif args[0] == 'lizard':
            apiCall = 'https://nekos.life/api/lizard'
            jsonLinkTag = 'url'
        elif args[0] == 'panda':
            apiCall = 'https://some-random-api.ml/img/panda'
            jsonLinkTag = 'link'
        elif args[0] == 'redpanda':
            apiCall = 'https://some-random-api.ml/img/red_panda'
            jsonLinkTag = 'link'
        else:
            apiCall = None
        
        if apiCall:
            async with aiohttp.ClientSession() as session:
                async with session.get(apiCall) as response:
                    if response.status != 200:
                        return await ctx.send('No ' + args[0] + ' found :(')

                    x = await response.json()

                    embed = discord.Embed(
                        title='Random ' + args[0], color=0x7ce4f7, timestamp=ctx.message.created_at)
                    if args[0] == 'cat':
                        embed.set_image(url=x[0][jsonLinkTag])
                    else:
                        embed.set_image(url=x[jsonLinkTag])

                    await ctx.send(embed=embed)
        else:
            await ctx.send("Can't work with that input, try again :c")

        
def setup(bot):
    bot.add_cog(Test(bot))