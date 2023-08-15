import random
import heros

list = [heros.troll, heros.monster, heros.org, heros.elf, heros.witch]
heroList = [heros.tor, heros.witcher, heros.roland]

def getPerson(participants):
    index = random.randint(0, len(participants) - 1)
    return participants.pop(index)

def round(player, participant):
    winner = {}
    if participant.isEvil:
        #  enemy
        print("Meet your enemy in the magic forest " + participant.name)
        participant.get_msg()
        player.get_msg()
        player.__get_data()

        print("fight : " + player.name + " VS " + participant.name)
        playerPower = player.get_power()
        participantPower = participant.get_power()
        if playerPower >= participantPower:
            winner = player
        else:
            winner = participant

        print('winner: ' + winner.name) 
    else:
        # friend
    
        winner = player

    print("------------")
    return winner

def game():
    count = 0

    for hero in heroList:
        count = count +1
        print(count, hero.name)
        
    heroIndex = int(input("With wich hero do you want to play:" )) - 1
    print("------------")
    hero = heroList[heroIndex]
    
    enemy1 = getPerson(list)
    enemy2 = getPerson(list)
    enemy3 = getPerson(list)

    winner = round(hero, enemy1)
    
    winner = round(winner, enemy2)
    winner = round(winner, enemy3)

    print("Final winner: " + winner.name )


game()

