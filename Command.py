#BASIC CHAT-REPLY COMMANDS
#ADVANCED COMMAND CLASSES WILL INHERIT FROM COMMAND
import random
chatCommandList = []
objCommandList = []

def parseHelpList():
  result = '**All Commands:**\n\n'

  for i in range(len(chatCommandList)):
    result += f'**{chatCommandList[i]}** \n\n'

  return result

class Command: 
  replyList = ['null']
  chatCommand = ''
  interpolate = False # whether chatCommand takes args to be interpolated

  def __init__(self, inp_chatCommand, inp_interpolate):
    self.chatCommand = inp_chatCommand
    self.interpolate = inp_interpolate

    chatCommandList.append(inp_chatCommand)
    objCommandList.append(self)

  def getReply(self):
    return random.choice(self.replyList)


   





      
