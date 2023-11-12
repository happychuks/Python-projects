#for dict {key: value}. they key could be in string or int. The value could be a string or an integer or an array of strings. 
x = {'key': [5,6,8]}
x['key2'] = 'Happy'
x[3] = 123456
x[2] = 10

for key in x:
    print(key, x[key])

print(x)

print(3 in x)

#To list all the keys in the dictionary
print(list(x.keys())) 
