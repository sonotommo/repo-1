# https://discord.com/api/oauth2/authorize?client_id=1001962911704563752&permissions=8&scope=bot
# pip install discord.py
# pip install pyChatGPT

from api import get_response

import discord
from discord.ext import commands
from time import sleep

client = commands.Bot(command_prefix='', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('bot online!')

@client.command(aliases=['chat:'])
async def chat(ctx, *, question):
    response = get_response(question)
    embed = discord.Embed(
        title=f'{question}',
        description=f'{response}'
    )
    await ctx.send(embed=embed)


@client.command(aliases=['info:'])
async def info(ctx):
    await ctx.send('chat: what you want to look for')


client.run('TOKEN')