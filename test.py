"""
Content of "log.txt":
10.1.2.1 - car [01/Mar/2022:13:05:05 +0900] "GET /python HTTP/1.0" 200 2222
10.1.1.9 - bike [01/Mar/2022:13:05:10 +0900] "GET /python HTTP/1.0" 200 2222

Expected output:
01/Mar/2022:13:05:05 +0900
01/Mar/2022:13:05:10 +0900
"""

""" def parse1():
    for line in open("log.txt"):
        print(line.split("[")[1].split("]")[0]) """

    def parse3():
         for line in open("log.txt", "r"):
             print(" ".join(line.split("[" or "]")[3:5])) 

    print(parse3())


