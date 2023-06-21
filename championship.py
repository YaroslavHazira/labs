# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)

matchResults = ["3:1", "2:2", "0:1"]
count = 0
# "3:1" => game ["3", "1"]
for i in matchResults:
    game = i.split(":")

    x = game[0]
    y = game[1]

    if x > y:
        count = count + 3
    if x == y:
        count = count + 1
    if x < y:
        count = count + 0
print(count)
    
