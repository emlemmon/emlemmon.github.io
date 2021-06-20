edlevel = {}

with open("emlemmon.github.io\python\Week9\census.csv") as census:
   for line in census:
        x = line.split(',')[3]
        
        x = x.replace(' ', '')
        count = edlevel.get(x)
        if count == None:
            count = 0
        edlevel[x] = count + 1

for x in edlevel:
    print("{} -- {}".format(x, edlevel[x]))


"""
with open("emlemmon.github.io\python\Week9\census.csv") as census:
    for line in census:
        x = line.split(' ')[3]
        #print(x)
        x = x.replace(' ', '')
        count = 0
        for x in edlevel:
            edLevel[x] = count + 1

for x in edlevel:
    print("{} -- {}".format(x, edlevel[x]))
"""