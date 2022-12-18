# A decision game where I'll have to create several different endings based on the answers.

#I want to reach different endings in my story, according to the answers I send to the program.

#Scenario : I am in a war between two nations, and we have 2 sides: Side A and Side B. 
#Only side A will win, and side B will lose! so I have to make the right decisions to get to the win, which only side A will get.

import PySimpleGUI as sg

class AdventureGame():
  def __init__(self):
    self.question1 = 'Were you born in the North US or the South? (n/s) ' # north = Side A, south = Side B
    self.question2 = 'Do you prefer the sword or shield? (sword/shield)' # sword = Side1, shield = Side2
    self.question3 = 'What is your specialty?(frontline/tactical)' # frontline = Side1, tactical = Side2
    self.finalHistory1 = 'You will be a hero on the front line!'
    self.finalHistory2 = 'You will be a hero protecting all our troops!'
    self.finalHistory3 = 'You will sacrifice yourself in battle!'
    self.finalHistory4 = 'You are not able to fight in this battle!'
  
  def Iniciate(self):
        # Layout
        layout = [
            [sg.Output(size=(50,2))],
            [sg.Input(size=(25,0),key='choice')],
            [sg.Button('Begin'), sg.Button('Answer')]
        ]
        # create window
        self.window = sg.Window('Adventure Game!',layout=layout, finalize=True)
        while True:
            # read values
            self.ReadValues()
            #click to close the program when you want
            if self.event == sg.WIN_CLOSED:
              break
            # make something with values
            if self.event == 'Begin':
                print(self.question1)
                self.ReadValues()
                if self.values['choice'] == 'n':
                    print(self.question2)
                    self.ReadValues()
                    if self.values['choice'] == 'sword':
                        print(self.finalHistory1)
                    if self.values['choice'] == 'shield':
                        print(self.finalHistory2)
                if self.values['choice'] == 'y':
                    print(self.question3)
                    self.ReadValues()
                    if self.values['choice'] == 'front line':
                        print(self.finalHistory3)
                    if self.values['choice'] == 'tactical':
                        print(self.finalHistory4)
  def ReadValues(self):
        self.event, self.values = self.window.Read()    

game = AdventureGame()
game.Iniciate()