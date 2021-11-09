import random
import Data

#Questions return a list, of question then answer
def p_sdt(): #physics_speedDistanceTime
  ftime = random.randint(1, 12)
  distance = random.randint(1, 200) * ftime
  speed = round(distance/ftime)

  qList = [
    f'Vivek moves {distance}km for {ftime}h. What is his speed in km/h? Answer to the nearest integer, without units.',
    f'Bill moves at {speed}km/h for {ftime}h. How far does he travel in km? Answer to the nearest integer, without units.',
    f'Bob moves at {speed}km/h for {distance}km. How long does he travel, in hours? Answer to the nearest integer, without units.',
  ]

  aList = [speed, distance, ftime]

  rand = random.randint(0, len(qList) - 1)
  return [str(qList[rand]), str(aList[rand])]

def p_acceleration():
  acceleration = random.randint(2, 10) * 2#m/s^2
  timeAccelerated = random.randint(1, 60) #s
  startSpeed = random.randint(40, 80) #m/s
  endSpeed = int(startSpeed + (acceleration * timeAccelerated))#m/s
  displacement = int((startSpeed + endSpeed)/2 * timeAccelerated)

  qList = [
    f'There is an object which moves (yes, its crazy, I know). It starts at {startSpeed}m/s, and accelerates at {acceleration}m/s² for {timeAccelerated}s. What velocity does it end at? Answer to the nearest integer, without units.',
    f'Billy in his prototype spaceship is going towards mars. He is currently moving at {startSpeed}m/s, but has to speed up. His rocket boosters fire for exactly {timeAccelerated}, and he needs to get up to {endSpeed}m/s. In m/s², what acceleration does he have to go at to reach his target velocity? Answer to the nearest integer, without units.',
    f'North Korea launched a missile, and its heading for the USA at {startSpeed * 3.6}km/h. For successful detonation, this missle needs to reach a velocity{endSpeed}m/s. If it accelerates at {acceleration}m/s², how long before it reaches its target velocity, in seconds? Answer to the nearest integer, without units.',
    f'You\'re in a game of spaceship-tag, moving at x m/s. You accelerate from x m/s to {endSpeed}m/s, accelerating at {acceleration}m/s² for {timeAccelerated}s. Find x to the nearest integer, and answer without units.',
    f'If earth orbitted the sun at a relative velocity of {startSpeed}m/s, and a massive commet flies by, accelerating it by {acceleration}m/s² for {timeAccelerated}s. In that {timeAccelerated}s, how far does it travel?'
  ]
  aList = [endSpeed, acceleration, timeAccelerated, startSpeed, displacement]

  rand = random.randint(0, len(qList) - 1)
  return [str(qList[rand]), str(aList[rand])]

def p_threeLaws():
  mass = random.randint(1, 2021)
  acceleration = random.randint(4, 50)
  force = mass * acceleration

  qList = [
    f'A car accelerates at {acceleration}m/s², with a mass of {mass}kg. How much force, in Newtons, does it have? Answer to the nearest integer, without units.',
    f'Object X weighs 800kg. To move it at a force of {force}N, how much acceleration would you need to push it at? Answer to the nearest integer, without units.',
    f'You threw a ball with an acceleration of {acceleration}m/s². How much does it wiegh if it broke the neighbor\'s window with {force}N of force. Answer to the nearest integer, without units. (Air resistance is negligible.)'
  ]

  aList = [force, acceleration, mass]

  rand = random.randint(0, len(qList) - 1)
  return [str(qList[rand]), str(aList[rand])]

def getPhysicsQuestion():
  if(random.randint(1, 3) == 1):
    index = random.randrange(0, len(Data.physicsQuizQuestions))
    return [Data.physicsQuizQuestions[index], Data.physicsQuizAnswers[index]]
  
  else:
    Qmakers = [p_sdt, p_acceleration, p_acceleration, p_threeLaws] #repeated for increased frequency
    return (random.choice(Qmakers)())

#CHEM QUESTION GETTERS
def getChemistryQuestion():
  index = random.randrange(0, len(Data.chemQuizQuestions))
  return [Data.chemQuizQuestions[index], Data.chemQuizAnswers[index]]

#BIO QUESTION GETTERS
def getBiologyQuestion():
  index = random.randrange(0, len(Data.bioQuizQuestions))
  return [Data.bioQuizQuestions[index], Data.bioQuizAnswers[index]]