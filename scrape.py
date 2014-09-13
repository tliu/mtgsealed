f = open("khans.html")
for line in f:
    if "<i>" in line:
        print line.split("src=\"")[1]
        print line.split("<i>")[1].split("<")[0] + "," + line.split("src=\"")[1].split("\" ")[0]
