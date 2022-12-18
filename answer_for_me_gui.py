import random
import PySimpleGUI as sg

class AnswerByMe:
  def __init__(self):
    self.resonses = [
      'Absolutely!',
      'Dunno!',
      'Do it!',
      'Don\'t do it!',
      'Right on time!',
      'You know!'
    ]

  def Initiate(self):
    #layout
    layout = [
      [sg.Text('Make your question: ')],
      [sg.Input()],
      [sg.Output(size=(50,10))],
      [sg.Button('Answer for me!')]
    ]

    #create window
    self.window = sg.Window('Answer for me!', layout=layout, finalize=True)

    while True:
      #read values
      self.events, self.values = self.window.Read()
      #Make something with values
      if self.events == 'Answer for me!':
        print(random.choice(self.resonses))
      #click to close the program when you want
      if self.events == sg.WIN_CLOSED:
          break

answers = AnswerByMe()
answers.Initiate()