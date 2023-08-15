class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy
   
        # self.get_data()
        pass

    def get_data(self):
        print("get_data",self.name, self.age, self.isHappy)


catGod = {
    "name": "igor",
    "age": 2,
    "isHappy": True
    # "get_data": () => {}
} 

# print(catGod["name"])

cat1 = Cat("igor", 3, True)
# cat1.set-data("igor", 3, True)
# cat2 = Cat("andrew", 2, False)
# cat2.set-data("andrew", 2, False)
 
print(cat1.get_data())
# print(cat2.name).

