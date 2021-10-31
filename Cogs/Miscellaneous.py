import discord
from discord.ext import commands

class Miscellaneous(commands.Cog):
  def init(self, client):
    self.client = client



def setup(client):
  client.add_cog(Miscellaneous(client))