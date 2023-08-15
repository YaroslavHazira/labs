
x = 0
while x == 0:
    try:
        x = int(input("Write a numbre:"))
        x = x + 5 
        print(x)
    except ValueError:
        print("beter write a numbre:")
