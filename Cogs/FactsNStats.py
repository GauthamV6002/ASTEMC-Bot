import discord
from discord.ext import commands
import Data
import random

class FactsNStats(commands.Cog):
  def init(self, client):
    self.client = client

  @commands.command()
  async def randstat(self, ctx):
      await ctx.send(random.choice(Data.randstats))

  @commands.command()
  async def funfact(self, ctx):
    await ctx.send(random.choice(Data.funfactList))

def setup(client):
  client.add_cog(FactsNStats(client))