#this allows us to iterate over certain periods

for x in range(1,20,2): #range(start, stop, step)
    print(x)


y = [2,5,23,10,15,20,32,56]

for i, element in enumerate(y): #this will attach indexes to each element in the array
    print(i, element)