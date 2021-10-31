import discord
from discord.ext import commands
import datetime
import random
from math import floor

class Utilities(commands.Cog):
  def init(self, client):
    self.client = client

  @commands.command()
  async def countdown(self, ctx):
    contestDt = datetime.datetime(2021, 11, 27, 9, 0, 0, 0)
    dtUntilContest = contestDt - datetime.datetime.utcnow()
    rand = random.randint(1, 5)

    if rand == 1:
      secsUntil = dtUntilContest.seconds + (dtUntilContest.days * 86400) + 21600
      countdown = f'There are {secsUntil} seconds until the contest! Try converting that to days!'
    else:
      seconds = abs((dtUntilContest.seconds + 21600) - ((floor(dtUntilContest.seconds/3600 + 6))*3600))
      countdown = f'There are {dtUntilContest.days} days, {floor(dtUntilContest.seconds/3600) + 6} hours, {floor(seconds/60)} minutes, and {seconds % 60} seconds until the contest!'
      
    await ctx.send(countdown)


def setup(client):
  client.add_cog(Utilities(client))