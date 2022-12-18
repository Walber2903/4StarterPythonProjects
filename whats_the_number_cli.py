import random

class WhatsTheNumber:
  def __init__(self):
    self.aleatory_value = 0
    self.minimum_value = 1
    self.maximum_value = 100
    self.try_again = True
    self.list_of_number_tried = []
  
  def Initiate(self):
    self.GenerateNumber()
    print(self.aleatory_value)
    self.GuessTheNumber()
    try:
      while self.try_again == True:
        if(int(self.number_tried) > 100 or int(self.number_tried) < 0):
          print('Just numbers between 1 and 100!!')
          self.GuessTheNumber()
        elif(int(self.number_tried) > self.aleatory_value):
          print('Try a lower number!')
          self.list_of_number_tried.append(self.number_tried)
          self.GuessTheNumber()
        elif(int(self.number_tried) < self.aleatory_value):
          print('Try a higher number!')
          self.list_of_number_tried.append(self.number_tried)
          self.GuessTheNumber()
        else: 
          self.list_of_number_tried.append(self.number_tried)
          print('Congrat\'s, you hit the number in %s shot(s)!!!' %len(self.list_of_number_tried))
          self.try_again = False
    except:
      print('Something went wrong, type only numbers....the game restart !!!')
      self.Initiate()

  def GuessTheNumber(self):
    self.number_tried = input('what\'s the number?')

  def GenerateNumber(self):
    self.aleatory_value =  random.randint(self.minimum_value, self.maximum_value)

try_to_hit = WhatsTheNumber()
try_to_hit.Initiate()