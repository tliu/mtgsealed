import json
f = open("KTK.json")
ktk = {}
for line in f:
    ktk = json.loads(line)

for card in ktk['cards']:
    print '%s,%s' % (card['name'], card['rarity'])
