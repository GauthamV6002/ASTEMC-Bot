import discord
from discord.ext import tasks, commands
import os

import Command
import CommandsInit

client = commands.Bot(command_prefix = "%")
TOKEN = os.environ['TOKEN']

client.load_extension("Cogs.Random")

@client.event
async def on_ready():
  print('Login Successful!')
  await client.change_presence(status=discord.Status.online, activity = discord.Game('%help'))



client.run(TOKEN)

