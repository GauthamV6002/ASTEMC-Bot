import discord
from discord.ext import commands

CurrentQuizTakerIds = []

def createQuizEmbed(questions):
  quizEmbed = discord.Embed(title='Quiz Time!', 
      color=0x00ff00, 
      description='Take a quick quiz and test your scientific knowledge!')

  for i in range(questions):
    quizEmbed.add_field(name=f'Question {i + 1}', value='temp', inline=False)

  quizEmbed.set_footer(text='Answers should be in the form:\n 1. Answer\n 2. Answer...' )

  return quizEmbed

  

class Quizzes(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def quiz(self, ctx, questions=3):
    
    await ctx.send('Functionality Incomplete. Please give 2-3 days for the issue to be resolved.')
    #await ctx.send(embed=createQuizEmbed(questions))

def setup(client):
    client.add_cog(Quizzes(client))