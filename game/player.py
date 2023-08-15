class Player:
    name = None
    speed = None
    attack = None
    health = None
    msg = None
    isEvil = None

    # options = {
    # "name": "Genard",
    # "health": 110,
    # "attack": 60,
    # "speed": 15,
    # "msg" : "",
    # "isEvil": False
    # }

    def __init__(self, options):
        self.name = options["name"]
        self.attack = options["attack"]
        self.speed =  options["speed"]
        self.health =  options["health"]
        self.msg =  options["msg"]
        self.isEvil = options["isEvil"]

        pass

    def get_power(self):
        return self.attack * self.speed
        #  player["attack"] * player["speed"]

    def __get_data(self):
        print("get_data", self.name, self.attack, self.speed, self.health, self.msg, self.isEvil)


    def get_msg(self):
        print(self.name + ": " + self.msg)

    
# {} - object     =>   cat = { "name": "Bob" }    =>    cat["name"]
# [] - array      =>   cats = ["Bob", "Tom"]      =>    cats[1]
# () - function   =>   def get_power():           =>    get_power()  exemple   print("string")
# "" - sting
