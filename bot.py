import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

import builtins

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='~', help_command=None, case_insensitive=True)
builtins.bot = bot

@bot.event
async def on_ready():
    print(f'{bot.user.name} has joined the chat!')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

# Unloads cog and loads again to reflect changes during dev
@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

# Load all cogs in cogs directory
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)