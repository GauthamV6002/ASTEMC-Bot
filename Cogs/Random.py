import discord
from discord.ext import tasks, commands
import FunFactList.py
import random

class Random(commands.Cog):
  def init(self, client):
    self.client = client

  @commands.command()
  async def funfact(self, ctx):
    await ctx.send(random.choice(FunFactList.factList))

def setup(client):
  client.add_cog(Random(client))