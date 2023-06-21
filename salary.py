
import csv

with open("./2022_june_dev.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)
