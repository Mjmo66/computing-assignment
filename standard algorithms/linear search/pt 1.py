## Standard Algorithms - Linear Search Parallel Arrays


namelist = ["Ann", "Bob", "Charles", "Dave", "Eddie", "Frank"]
age = [15, 16, 17, 14, 15, 14]
found = False

searchname = input("Enter name to search for: ")

counter = 0
while not found and counter <= 5:
    if namelist[counter] == searchname:
        print(age[counter])
        found = True
    counter += 1

if not found:
    print("Name not found")