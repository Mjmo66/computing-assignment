
speeds = [ 25.5, 26.2, 27.8, 28.6, 29.4, 30.1, 30.7, 31.4, 32.2, 33.0, 33.7, 34.3, 34.9, 25.9, 26.7, 27.3, 28.0, 28.8, 29.5, 30.3]

lowest_speed = 999
for i in range(20):

   if lowest_speed > speeds[i]:
        lowest_speed = i
print('you lowest', speeds[lowest_speed])