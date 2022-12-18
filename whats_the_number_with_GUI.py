import random
import PySimpleGUI as sg

class WhatsTheNumber:
  def __init__(self):
    self.aleatory_value = 0
    self.minimum_value = 1
    self.maximum_value = 100
    self.try_again = True
    self.list_of_number_tried = []
  
  def Initiate(self):
    #layout
    layout = [
      [sg.Text('What\'s your hit?', size=(39,0))],
      [sg.Input(size=(18,0),key='hit_value')],
      [sg.Button('Hit!')],
      [sg.Output(size=(39,10))]
    ]
    # Create a window
    self.window = sg.Window('Whats the number!', layout=layout, finalize=True)
    self.GenerateNumber()
    print(self.aleatory_value)
    try:
      while True:
        # Ready the input values from screen
        self.event, self.values = self.window.Read()
        # Make something with the values
        if self.event == sg.WIN_CLOSED:
          break
        if self.event == 'Hit!':
          self.number_tried = self.values['hit_value']
          while self.try_again == True:
            if(int(self.number_tried) > 100 or int(self.number_tried) < 0):
              print('Just numbers between 1 and 100!!')
              break
            elif(int(self.number_tried) > self.aleatory_value):
              print('Try a lower number!')
              self.list_of_number_tried.append(self.number_tried)
              break
            elif(int(self.number_tried) < self.aleatory_value):
              print('Try a higher number!')
              self.list_of_number_tried.append(self.number_tried)
              break
            else: 
              self.list_of_number_tried.append(self.number_tried)
              print('Congrat\'s, you hit the number in %s shot(s)!!!' %len(self.list_of_number_tried))
              self.try_again = False
              break
        self.window.close()
    except:
      self.Initiate()
      print('Something went wrong, type only numbers....the game restart !!!')
      
  def GenerateNumber(self):
    self.aleatory_value =  random.randint(self.minimum_value, self.maximum_value)

try_to_hit = WhatsTheNumber()
try_to_hit.Initiate()