
# pralel

from dataclasses import dataclass

def rfile():

    entry_id  = [' ']* 30
    location = [''] * 30
    forname = [''] * 30
    surname = [''] * 30
    jumps = [0] * 30
    
    tempstring = ""
    temparray = [None, None]


    with open ("assignments/2021 cw/athletes.csv") as file:
        for i in range(30):
            tempstring = file.readline().strip()
            temparray = tempstring.split(",")
            entry_id[i] = temparray[0]
            location[i] = temparray[1]
            forname[i]  = temparray[2]
            surname[i]  = temparray[3]
            jumps[i]    =  int(temparray[4])
            
            
    return entry_id,location,forname,surname,jumps

def bib(entry_id,location,forname,surname,):
    with open("assignments/2021 cw/bib_value.csv","w") as writefile:
        for i in range (30):
            writefile.write(str(entry_id[i]) + "," + str(forname[i][0]) + str(surname[i])+ str(ord(location[i][0])) + "\n")


def  max_jumps(jumps):
    max_j = 0
    for i in range(len(jumps)):
        if jumps[i] > jumps[max_j]:
            max_j = i
            print(max_j)
        
            
    return max_j

def find_player(jumps,max_j,forname):
    mj = jumps[max_j]
    found = False
    for i in range (30):
        if  mj == jumps[i]:
          print(forname[i])
          found = True

    return found,mj

    


def display(jumps,max_j,forname):
       print (jumps[max_j])
       print (forname[max_j])


def main():
   entry_id,location,forname,surname,jumps = rfile()
   bib(entry_id,location,forname,surname)
   max_j = max_jumps(jumps)
   found,mj = find_player(jumps,max_j,forname)
   display (jumps,max_j)


main()