import discord
from discord.ext import tasks, commands
from keep_alive import keep_alive
import os
#from itertools import cycle


client = commands.Bot(command_prefix = "%")
TOKEN = os.environ['TOKEN']

statusLoop = ['%funfact', '%randstat', '%help', '%quiz']

#COGS
client.load_extension("Cogs.FactsNStats")
client.load_extension("Cogs.Quizzes")

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("The command you used is missing arguments!")

@client.event
async def on_ready():
  print('Successful Login!')

  await client.change_presence(status=discord.Status.online, activity = discord.Game('| %help'))

keep_alive()
client.run(TOKEN)

