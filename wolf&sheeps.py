queue0 = ["sheep", "sheep", "sheep", "sheep", "sheep", "wolf", "sheep", "sheep"]

queue1 = ["wolf", "sheep", "sheep", "sheep", "sheep", "sheep", "sheep"]

count = 0

for i in queue1:
    if i == "wolf":
        break
    count = count + 1

msgGoAway = "Pls go away and stop eating my sheep"
msgAlert = "Oi! Sheep number " + str(count - 1) + "! You are about to be eaten by a wolf!"

if count == 0:
    print(msgGoAway)
else:
    print(msgAlert)
