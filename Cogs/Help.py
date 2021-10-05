import discord
from discord.ext import tasks, commands
import os

class Help(commands.Cogs):
  
  def init(self, client):
    self.client = client

  @commands.command()
  async def help(self, ctx):
    helpEmbed = discord.Embed(title = "Help")

    for cogname in os.listdir():
      cog = self.client.get_cog(cogname)
      commands = cog.get_commands()
      helpEmbed.add_field(name = cogname, value = )