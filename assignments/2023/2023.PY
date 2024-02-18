
from dataclasses import dataclass

def rfile():
        
    with open ("assignments/2023/attractions.csv") as file:
        lines = file.readlines()
        linecount = len(lines)


        attraction  = [' ']* linecount
        catergory = [''] * linecount
        visitors = [0] * linecount
        days_open = [0] * linecount
        hieght = [''] * linecount
    
        tempstring = ""*5
        temparray = [None, None,None,None,None]


    with open ("assignments/2023/attractions.csv") as file:
        for i in range(linecount):
            tempstring = file.readline().strip()
            temparray = tempstring.split(",")
            attraction[i] = temparray[0]
            catergory[i]  = temparray[1]
            visitors[i]   = int(temparray[2])
            days_open[i]  = int(temparray[3])
            hieght[i]     = temparray[4]
            
            
    return attraction,catergory,visitors,days_open,hieght

def visited(attraction,visitors):
    least = 0
    max = 0
    for i in range(len(visitors)):
        if visitors[i] > max:
            max = i
            

    for i in range(len(visitors)):        
        if visitors[least] > visitors[i]:
            least = i



            print(attraction[max], attraction[least])
            print(visitors[max], visitors[least])



        
def r_t_f(attraction,catergory,days_open):
     days=0
     with open("assignments/2023/service.csv","w") as writefile:
        for i in range (len(catergory)):
            if catergory[i] == 'Roller Coaster':
                days = (days_open[i] % 90)
                if (90 - days) <= 7 :
                    writefile.write(str(attraction[i]) +"\n")

def hieght_r(hieght):
    count = 0
    for i in range (len(hieght)):
        if ((hieght[i]) [0]) == '1':
            count +=1 
    print(count)





def main():
   attraction,catergory,visitors,days_open,hieght = rfile()
   visited(attraction,visitors)
   r_t_f(attraction,catergory,days_open)
   hieght_r(hieght)

main()