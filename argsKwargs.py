def func(x,y,z):
    print(x,y,z)

pairs = [(1,2,6), (3,4,1)]

for pair in pairs:
    func(*pair)