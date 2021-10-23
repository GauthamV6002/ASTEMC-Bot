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
    await ctx.send("The command you used is missing arguments!\n Eg. %ans answer1, answer2, answer3")

@client.event
async def on_ready():
  print('Successful Login!')

  await client.change_presence(status=discord.Status.online, activity = discord.Game('| %help'))

# @tasks.loop(seconds=10)
# async def change_status():
#   for i in cycle(statusLoop):
#     await client.change_presence(activity=discord.Game(i))

# change_status.start()

keep_alive()
client.run(TOKEN)

