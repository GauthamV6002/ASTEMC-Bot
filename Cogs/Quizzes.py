import discord
from discord.ext import commands
import random
import Data


current_quiz_takers = []
current_quiz_answers = []


def createQuizEmbed():
  quizEmbed = discord.Embed(title='Quiz Time!', 
      color=0x00ff00,)

  QAindices = [random.randrange(0, len(Data.quizQuestions)) for i in range(3)]
  ans_list = []

  for i in range(3):
    quizEmbed.add_field(name=f'Question {i + 1}', value=Data.quizQuestions[QAindices[i]], inline=False)
    ans_list.append(Data.quizAnswers[QAindices[i]])

  current_quiz_answers.append(ans_list)
  quizEmbed.set_footer(text='Seperate answers with a comma, and use the %ans command to answer.')

  return quizEmbed



class Quizzes(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def quiz(self, ctx):
      await ctx.send(embed=createQuizEmbed())
      current_quiz_takers.append(ctx.message.author)

  @commands.command()
  async def ans(self, ctx, *, answers):
    answers_list = (answers.replace(' ', '').lower()).split(',')
    
    if len(answers_list) < 3:
      await ctx.send('Please answer all the questions!')
    else:
      if ctx.message.author in current_quiz_takers:
        ctxAns = current_quiz_answers[current_quiz_takers.index(ctx.message.author)]

        score = 0
        for i in range(len(ctxAns)):
          if ctxAns[i] == answers_list[i]:
            score += 1
        
        current_quiz_answers.pop(current_quiz_takers.index(ctx.message.author))
        current_quiz_takers.remove(ctx.message.author)

        await ctx.send('You got ' + str(score) + '/3 correct!\nCorrect Answers: ' + str(ctxAns)[1:-1].replace('\'', ''))

      else:
        await ctx.send("Looks like you aren't taking a quiz! Use %quiz to start one!")

def setup(client):
    client.add_cog(Quizzes(client))