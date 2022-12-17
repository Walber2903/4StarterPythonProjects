#Dice simulator
#Simulate dice use, generate a value between 1 to 6.
import random

class DiceSimulator:
  def __init__(self):
    self.minumum_value = 1
    self.maximum_value = 6
    self.message = 'Do you like to roll a d6? (yes/no)'

  def Initiate(self):
    response = input(self.message)
    try:
      if response == 'yes' or response == 'y':
        print(self.GenerateDiceValue())
      elif response == 'no' or response == 'n':
        print('Thanks...Closing the program...')
      else:
        print('Please type yes or no.')
    except:
      print('Somethig wrong happened!')


  def GenerateDiceValue(self):
    return random.randint(self.minumum_value, self.maximum_value)

simulator = DiceSimulator()

simulator.Initiate()