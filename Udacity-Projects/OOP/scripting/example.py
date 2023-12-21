# reads in the file a little at a time by passing an integer argument to .read().
with open("./camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

camelot_lines = []
# this create a list of lines in the file by stripping the newline character
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

"""
def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    return cast_list
cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
"""