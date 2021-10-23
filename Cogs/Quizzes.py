import discord
from discord.ext import commands
import random
import Data


current_quiz_takers = []
current_quiz_answers = []


def createQuizEmbed(answers, questions):
  quizEmbed = discord.Embed(title='Quiz Time!', 
      color=0x00ff00,)

  for i in range(3):
    quizEmbed.add_field(name=f'Question {i + 1}', value = questions[i])
  quizEmbed.set_footer(text='Seperate answers with a comma, and use the %ans command to answer.')

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

    def check(m, author):
      return m.author == ctx.message.author
      
    #Wait for response from command caller for answers
    message = self.client.wait_for("message", check=check).split()
    for i in range(len(message)):
      if message[i] == answers[i]:
        score += 1

    await ctx.send('You got ' + str(score) + '/3 correct!\nCorrect Answers: ' + str(answers)[1:-1].replace('\'', '') + '\nConfused about answer or see an error? Dm or mention a director or organizational commitee member!')

def setup(client):
    client.add_cog(Quizzes(client))