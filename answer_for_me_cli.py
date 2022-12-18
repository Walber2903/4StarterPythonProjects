import random

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
    input('Make your question: ')
    print(random.choice(self.resonses))

answers = AnswerByMe()
answers.Initiate()