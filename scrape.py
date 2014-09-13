f = open("khans.html")
for line in f:
    if "<i>" in line:
        print line.split("<i>")[1].split("<")[0]
