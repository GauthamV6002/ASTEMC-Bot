import discord
from discord.ext import tasks, commands

import os
from itertools import cycle


client = commands.Bot(command_prefix = "%")
TOKEN = os.environ['TOKEN']

statusLoop = ['%funfact', '%randstat', '%help']

#COGS
client.load_extension("Cogs.FactsNStats")
client.load_extension("Cogs.Quizzes")


@client.event
async def on_ready():
  print('Successful Login!')

  await client.change_presence(status=discord.Status.online, activity = discord.Game('| %help'))

@tasks.loop(seconds=45)
async def change_status():
  for i in cycle(statusLoop):
    await client.change_presence(activity=discord.Game(i))


client.run(TOKEN)

