
import csv

with open("./2022_june_dev.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    if row[4] == "Python":
      print(row)
    # for cell in row:
    #   print(cell)

# task1: Print List Python Developers 

# csvreader = [
#  ['2700', 'Senior', 'від  4 до 6 років', 'Інше', 'Інша', '1'],
#  ['3000', 'Senior', 'від 4 до 6 років', 'Інше', 'Python', '1'],
#  ['3275', 'Senior', 'від 4 до 6 років', 'Інше', 'Інша', '1'],
#  ['3650', 'Senior', 'від 4 до 6 років', 'Інше', 'Інша', '1'],
#  ['4200', 'Senior', 'від 4 до 6 років', 'Інше', 'Інша', '2'],
#  ['4300', 'Senior', 'від 4 до 6 років', 'Інше', 'Інша', '1'],
#  ]

