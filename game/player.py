class Player:
    name = None
    speed = None
    attack = None
    health = None
    msg = None
    isEvil = None

    def __init__(self, options):
        self.name = options["name"]
        self.attack = options["attack"]
        self.speed =  options["speed"]
        self.health =  options["health"]
        self.msg =  options["msg"]
        self.isEvil = options["isEvil"]
        self.award = options["award"]
        pass

    def get_power(self):
        return self.attack * self.speed

    def get_msg(self):
        print(self.name + ": " + self.msg)

    # friend
    def get_award(self):
        return self.award

    def set_award(self, award):
        key = award["key"]
        amount = award["amount"]
        updatedAmount = getattr(self, key) + amount
    
        setattr(self, key, updatedAmount)

