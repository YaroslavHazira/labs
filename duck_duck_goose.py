# player1 = {
#   "name": "John"
# }

class Player:
  def __init__(self, name):
    self.name = name
    
  def str(self):
    return self.name + " pop"

player1 = Player("John")
player2 = Player("Jane")
player3 = Player("Jill")
player4 = Player("Jack")

playerList = [player1, player2, player3, player4]

def duck_duck_goose(players, position):
    print(len(players), position)
    


    pass





duck_duck_goose(playerList, 1) 
# should return a.name
duck_duck_goose(playerList, 5)
# should return a.name
duck_duck_goose(playerList, 4)
# should return d.name