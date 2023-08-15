from player import Player  

witcher = Player({
    "name": "Genard",
    "health": 110,
    "attack": 60,
    "speed": 15,
    "msg" : "",
    "isEvil": False
})
# hero
roland = Player({
    "name": "Roland",
    "health": 100,
    "attack": 50,
    "speed": 20,
    "isEvil": False,
    "msg" : ""
})
# hero
tor = Player({
    "name": "Tor",
    "health": 110,
    "attack": 70,
    "speed": 5,
    "isEvil": False,
    "msg" : ""
})
# enemy
troll = Player({
    "name": "troll",
    "health": 70,
    "attack": 40,
    "speed": 20,
    "isEvil": True,
    "msg" : "You will not get what you want until you passe me"
})
# enemy
monster = Player({
    "name": "monster",
    "health": 70,
    "attack": 40,
    "speed": 20,
    "isEvil": True,
    "msg": "Oh how do we have here! let's fight!"
})
# enemy
org = Player({
    "name": "org",
    "health": 70,
    "attack": 60,
    "speed": 20,
    "isEvil": True,
    "msg": "I see a real warrior end i will kill him!"
})
# friend
elf = Player({
    "name": "elf",
    "health": 70,
    "attack": 40,
    "speed": 20,
    "isEvil": False,
    "award": {
        "key": "speed",
        "amount": 5
    },
    "msg": "Hello please do not kill me. I have a gift for you:"
})
# friend
witch = Player({
    "name": "witch",
    "health": 70,
    "attack": 40,
    "speed": 20,
    "isEvil": False,
    "award": {
        "key": "health",
        "amount": 50
    },
    "msg": "I am happy to meet you! Please accept my gift:"
})
