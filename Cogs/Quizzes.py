import discord
from discord.ext import commands
import random, QuestionGen

current_quiz_answers = []


def createQuizEmbed(questions):
  quizEmbed = discord.Embed(title='Quiz Time!', color=0x00ff00)

  for i in range(3):
    quizEmbed.add_field(name=f'Question {i + 1}', value = questions[i], inline=True)

  quizEmbed.set_footer(text='Seperate answers with a space, your next message will be recorded as your answer.')

  return quizEmbed



class Quizzes(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def quiz(self, ctx, *, subject='None'):
    #Number of correct answers
    score = 0
    questions = []
    answers = []

    if(subject.lower() == 'biology'):
      for i in range(3):
        QandA = QuestionGen.getBiologyQuestion()
        questions.append(QandA[0])
        answers.append(QandA[1])
    elif(subject.lower() == 'chemistry'):
      for i in range(3):
        QandA = QuestionGen.getChemistryQuestion()
        questions.append(QandA[0])
        answers.append(QandA[1])
    elif(subject.lower() == 'physics'):
      for i in range(3):
        QandA = QuestionGen.getPhysicsQuestion()
        questions.append(QandA[0])
        answers.append(QandA[1])
    else:
        QandA = QuestionGen.getBiologyQuestion()
        questions.append(QandA[0])
        answers.append(QandA[1])

        QandA = QuestionGen.getChemistryQuestion()
        questions.append(QandA[0])
        answers.append(QandA[1])

        QandA = QuestionGen.getPhysicsQuestion()
        questions.append(QandA[0])
        answers.append(QandA[1])
    

    await ctx.send(embed=createQuizEmbed(questions))

    def check(m):
      return m.author.id == ctx.message.author.id
      
    #Wait for response from command caller for answers
    message = await self.client.wait_for("message", check=check)
    message_content = message.content.lower().replace('%ans', '').replace(',', '').split()

    if len(message_content) > len(answers):
      for i in range(len(answers)):
        if message_content[i] == answers[i]:
          score += 1
    else:
      for i in range(len(message_content)):
        if message_content[i] == answers[i]:
          score += 1

    ansStr = (str(answers))[1:-1].replace(',', ' ').replace('\'', '')
    ansMsg = f'You got {str(score)}/3 correct!\nCorrect Answers: {ansStr} \nPlease note a beta system for questions is in implementation. Please contact @directors if you see an error!'

    await ctx.send(ansMsg)

def setup(client):
    client.add_cog(Quizzes(client))