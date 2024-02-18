
##Standard Algorithms - Counting Occurrences Parallel Arrays


speeds = [0.0] * 20
manufacturers = [""] * 20
speeds =  [ 25.5, 26.2, 27.8, 32.6, 29.4, 30.0, 30.7, 31.4, 32.2, 33.0, 33.7, 34.3, 34.9, 25.9, 26.7, 27.3, 28.0, 28.8, 31.5, 30.3]
manufacturers = ["Volkswagen", "Toyota", "Audi", "Volkswagen", "Volkswagen", "Nissan", "BMW", "Mercedes-Benz", "Audi", "Hyundai", "Volkswagen", "Toyota", "Mazda", "Subaru", "Toyota", "Volkswagen", "Tesla", "Fiat", "Volkswagen", "Toyota"]
count = 0
car = str(input('what are are you looking for'))
carspeed = float(input('what speed are you looking for '))
for i in range (len(speeds)):
    if car == manufacturers[i] and   carspeed >=  speeds[i]:
       count += 1
       print (i)
print('the num of car is',count)