#FILE FOR ALL COMMANDS
#ALL COMMANDS ARE OBJECTS OF THE COMMAND CLASS
#PREFIX ALL COMMAND NAMES WITH 'C' EG. Chello

#HELP COMMAND MUST BE WRITTEN LAST!! 
import Command
import FunFactList

#Test
Ctest1 = Command.Command('%test', False)
Ctest1.replyList = ['Test Success']

#FunFact
Cfunfact = Command.Command('%funfact', False)
Cfunfact.replyList = FunFactList.factList 

#Help
Chelp = Command.Command('%help', False)
Chelp.replyList = [Command.parseHelpList()] 



