

## this is for a parallel array

import time
count = 0
start  = time.time()
found = False


with open("csv/boysnames.csv") as file:
    lines= file.readlines()
    linecount= len(lines)

names  = [' ']* linecount
number = [0] * linecount

tempstring = ""
temparray = [None, None]
target = str(input('enter a name'))

with open ("csv/boysnames.csv") as file:
    for i in range(linecount):
     tempstring = file.readline().strip()
     temparray = tempstring.split(",")
     names[i] = temparray[0]
     number[i] = int(temparray[1])

    for i in range (len(names[i])) :
        if names[i] == target:
            print("Name found at position",  i  )
            found = True
        
count += 1

if  found ==  False:
    print("Name not found")


end= time.time()

print('time taken:',
  (end-start), 's')
