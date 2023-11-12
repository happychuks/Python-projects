#Lists are mutable (they can be changed/modified)
#Lists are defined with []

x = ['Happy', 'Felix', 'Chukwuma', 'David']
x.append('Ademide') #this will attach the new name to the list of x
x.extend(['Diah', 'Mercy', 'Joy']) #this wil attach the new list to the existing list of x
""" x.pop() #this wil remove the last element on this list of x
print(x.pop(4)) #this wil remove the indicated element on this list of x """
print(x)
print(x[2]) #this will print the indicated element on this list of x
print(len(x))