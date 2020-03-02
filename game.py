import random
import itertools

class Game(object):
  def __init__(self, players, numTiles, numDice):
    self.players = players
    self.numDice = numDice
    self.tiles = []
    for i in range(numTiles):
      self.tiles.append(i+1) 
  
  def rollDice(self):
    roll = 0 
    for i in range(self.numDice):
      roll += random.randint(1, 6)
    print('Dice roll: ', roll)
    return roll

  def validCombos(self, roll):
    valid = []
    for i in range(len(self.tiles)+1):
      for combo in itertools.combinations(self.tiles, i):
        if sum(combo) == roll:
          valid.append(combo)
    print('All valid combinations: ', valid)
    return valid

  def playCombo(self, combos):
    selected = combos[random.randint(0, len(combos)-1)]
    for i in range(len(selected)):
      self.tiles.remove(selected[i])
    print('tiles remaining: ', self.tiles)
    

if __name__ == '__main__':
  game = Game(2, 9, 2)
  roll = game.rollDice()
  combos = game.validCombos(roll)
  game.playCombo(combos)
  
