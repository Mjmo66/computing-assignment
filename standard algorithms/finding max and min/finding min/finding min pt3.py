speeds = [0.0] * 20
license = [""] * 20
speeds = [ 25.5, 26.2, 27.8, 28.6, 29.4, 30.1, 30.7, 31.4, 32.2, 33.0, 33.7, 34.3, 34.9, 25.9, 26.7, 27.3, 28.0, 28.8, 29.5, 30.3]
license= [ "AB12 CDE", "FG34 HJK", "LM56 NOP", "QR78 STU", "VW90 XYZ", "AB11 CDE", "FG33 HJK", "LM55 NOP", "QR77 STU", "VW89 XYZ", "AB10 CDE",  "FG32 HJK", "LM54 NOP", "QR76 STU", "VW88 XYZ", "AB09 CDE", "FG31 HJK", "LM53 NOP", "QR75 STU", "VW87 XYZ" ]

minspeed = 0

mincount = 0
for i in range (20):
   if speeds[i] < speeds[minspeed]:
     minspeed = i
     mincount+= 1
print ('the lowest is ',license[minspeed], 'found in ', mincount),