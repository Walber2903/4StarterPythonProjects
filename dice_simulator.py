#Dice simulator
#Simulate dice use, generate a value between 1 to 6.
import random
import PySimpleGUI as sg

class DiceSimulator:
  def __init__(self):
    self.minumum_value = 1
    self.maximum_value = 6
    self.message = 'Do you like to roll a d6? (yes/no)'
    # Layout
    self.layout = [
      [sg.Text('Roll the dice?')],
      [sg.Button('Yes'), sg.Button('No')]
    ]

  def Initiate(self):
    # Create a window
    self.window = sg.Window('Dice Simulator', layout=self.layout)
    # Ready the input values from screen
    self.events, self.values = self.window.Read()
    # Make something with the values
    try:
      if self.events == 'Yes' or self.events == 'y':
        print(self.GenerateDiceValue())
      elif self.events == 'No' or self.events == 'n':
        print('Thanks...Closing the program...')
      else:
        print('Please type yes or no.')
    except:
      print('Somethig wrong happened!')


  def GenerateDiceValue(self):
    return random.randint(self.minumum_value, self.maximum_value)

simulator = DiceSimulator()

simulator.Initiate()