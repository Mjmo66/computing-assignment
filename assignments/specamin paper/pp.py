
from dataclasses import dataclass

def r_file():
        
    with open ("assignments/specamin paper/beachData.csv") as file:
        lines = file.readlines()
        linecount = len(lines)

        name = [''] * linecount
        rating = [0] * linecount

        tempstring = ""*2
        temparray = [None, None]


    with open ("assignments/specamin paper/beachData.csv") as file:
        for i in range(linecount):
            tempstring = file.readline().strip()
            temparray = tempstring.split(",")
            name[i]  = temparray[0]
            rating[i]   = int(temparray[1])

            
            
    return name,rating

   

def avg_rating(name,rating):
    average = 0
    for i in range (len(name)):
        average = average + rating[i]
    average = average / (len(rating))

    return average 


def find (name,rating):
    user = int(input('what rating do you want'))
    for i in range (len(name)):
        if user == rating[i]:
            print(name[i])

def display(average):
    print(average)





def main():
   name,rating = r_file()
   average = avg_rating(name,rating)
   display(average)
   find (name,rating)
main()