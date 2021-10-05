import discord
import os

import Command
import CommandsInit

client = discord.Client()
TOKEN = os.environ['TOKEN']

@client.event
async def on_ready():
  print('Login Successful!')
  await client.change_presence(status=discord.Status.online, activity = discord.Game('%help'))

@client.event
async def on_message(message):
    if(message.content in Command.chatCommandList):
        objIndex = Command.chatCommandList.index(message.content)
        reply = Command.objCommandList[objIndex].getReply()

        await message.channel.send(reply)

client.run(TOKEN)

