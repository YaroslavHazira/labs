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

# for i in playerList:
#    print(i.name)

def duck_duck_goose(players, position):
    index = position - 1
    allplayers = len(players)
    if position <= allplayers:
      player = players[index]
      print(player.name)
      return player.name

    i = position
    while i > allplayers:
      i = i - allplayers

    index = i - 1 
    print(i)  
    
    player = players[index]
    print(player.name)
    return player.name

    pass





# duck_duck_goose(playerList, 1) 
# should return a.name
duck_duck_goose(playerList, 15)
# should return a.name
# duck_duck_goose(playerList, 4)
# should return d.name