import discord
from discord.ext import commands
import random
import Data


current_quiz_takers = []
current_quiz_answers = []


def createQuizEmbed(questions):
  quizEmbed = discord.Embed(title='Quiz Time!', 
      color=0x00ff00,)

  for i in range(3):
    quizEmbed.add_field(name=f'Question {i + 1}', value = questions[i])
  quizEmbed.set_footer(text='Seperate answers with a space, your next message will be recorded as your answer.')

  return quizEmbed



class Quizzes(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def quiz(self, ctx):
    #Number of correct answers
    score = 0
    #Generate 3 random questions and answers, stored in lists
    QAindices = [random.randrange(0, len(Data.quizQuestions)) for i in range(3)]
    questions = [Data.quizQuestions[QAindices[i]] for i in range(3)]
    answers = [Data.quizAnswers[QAindices[i]] for i in range(3)]

    await ctx.send(embed=createQuizEmbed(questions))

    def check(m):
      return m.author.id == ctx.message.author.id
      
    #Wait for response from command caller for answers
    message = await self.client.wait_for("message", check=check)
    message_content = message.content.split()
    for i in range(len(message_content)):
      if message_content[i] == answers[i]:
        score += 1

    await ctx.send('You got ' + str(score) + '/3 correct!\nCorrect Answers: ' + str(answers)[1:-1].replace('\'', '') + '\nConfused about answer or see an error? Dm or mention a director or organizational commitee member!')

def setup(client):
    client.add_cog(Quizzes(client))