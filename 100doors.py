doors = [False] * 100
for i in range(100):
   for j in range(i, 100, i+1):
       doors[j] = not doors[j]
   if doors[i] == True:
       print(i+doors[i])
#100doors
