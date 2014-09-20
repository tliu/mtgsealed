f = open("khans.html")
color = ""
for line in f:
    if '<div id="divwhite">' in line:
        color = "W"
    if '<div id="divblue">' in line:
        color = "U"
    if '<div id="divblack">' in line:
        color = "B"
    if '<div id="divred">' in line:
        color = "R"
    if '<div id="divgreen">' in line:
        color = "G"
    if '<div id="divmulticolored">' in line:
        color = "M"
    if '<div id="divartifact">' in line:
        color = "A"
    if '<div id="divland">' in line:
        color = "L"
    if "<i>" in line:
        print line.split("<i>")[1].split("<")[0] + "," + color
