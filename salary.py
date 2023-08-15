
import csv

count = 0
devList = []


with open("./2022_june_dev.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
      
    # if row[4] == "Python":
    if row[1] == "Junior" and row[4] == "Python":
        count = count + 1
        devList.append(row)
        # print(row[0])
  
# print(devList)
sum = 0
for row in devList:
  # row = ['2700', 'Senior', 'від  4 до 6 років', 'Інше', 'Інша', '1']
  sum = sum + int(row[0])
  
print(sum / count) 
# print(len(devList))



    # for cell in row:
    #   print(cell)

# task1: Print List Python Developers 

# devList = [
#  ['2700', 'Senior', 'від  4 до 6 років', 'Інше', 'Інша', '1'],
#  ['3000', 'Senior', 'від 4 до 6 років', 'Інше', 'Python', '1'],
#  ['3275', 'Senior', 'від 4 до 6 років', 'Інше', 'Інша', '1'],
#  ['3650', 'Senior', 'від 4 до 6 років', 'Інше', 'Інша', '1'],
#  ['4200', 'Senior', 'від 4 до 6 років', 'Інше', 'Інша', '2'],
#  ['4300', 'Senior', 'від 4 до 6 років', 'Інше', 'Інша', '1'],
#  ]

