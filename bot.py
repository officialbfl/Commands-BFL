#______________________IMPORT______________________#

import discord
from discord.utils import get
import json
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
import requests

from datetime import datetime, timezone

Client = discord.Client()
client = commands.Bot(command_prefix = "-")
client.remove_command('help')

#______________________EVENTS______________________#

@client.event 
async def on_ready():
    print("Bot is online and connected to Discord")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Bonk.io | -help'))

@client.command(pass_context=True)
async def roses(ctx):
	embed = discord.Embed(title="", description=" Roses is one of the dumbest clans currently in Bonk.io Football lead by xSmurf and Alex2810. \n \n It has one of the worst war records currently standing at : 0-30! \n \n It has bad players such as Nub1, Tuccio, xSmurf and more! \n \n It has a discord server with an inactive community \n \n Dont join roses today!", color=0x00EEEE)
	embed.add_field(name="Invite to this Server", value="[Click Here](https://discord.gg/rGfxT3b)")
	embed.set_image(url="https://images-ext-2.discordapp.net/external/M2Cx7oPf1mK4jtQ-Boa-n-Xxfwfz0ZD78lkViHXg2dc/https/discordapp.com/api/guilds/515609188047519744/icons/43d75d5e16516179ce4247d109f917ec.jpg?width=103&height=103")
	embed.set_author(name="Roses", icon_url="https://images-ext-2.discordapp.net/external/M2Cx7oPf1mK4jtQ-Boa-n-Xxfwfz0ZD78lkViHXg2dc/https/discordapp.com/api/guilds/515609188047519744/icons/43d75d5e16516179ce4247d109f917ec.jpg?width=103&height=103")
	embed.set_footer(text="Partner")
	await client.say(embed=embed)	

#______________________TOKEN______________________#

client.run(str(os.environ.get('BOT_TOKEN')))
