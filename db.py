import sqlite3
from collections import defaultdict
import random



class theDBMgr:
    def __init__(self):
        self.open()

    def populate_table(self, filename):
        f = open(filename)
        for line in f:
            self.c.execute('insert into cards values (NULL,"?")', line.strip())
            self.conn.commit()

    def populate_images(self, filename):
        f = open(filename)
        for line in f:
            x = line.strip().split(',')
            self.c.execute('update cards set img=? where name=?', (x[1], x[0]))
            self.conn.commit()

    def get_card_id_by_name(self, name):
        name = self.c.execute("select id from cards where name=?", (name,))
        return name.fetchone()[0]

    def get_card_by_id(self, id):
        name = self.c.execute("select * from cards where id=?", (id,))
        return name.fetchone()

    def get_max_booster_id(self):
        id = self.c.execute("select max(booster_id) from boosters")
        max = id.fetchone()[0]
        return max if max != None else -1

    def get_booster(self, id):
        booster = self.c.execute("select c.name from boosters b join cards c on b.cards=c.id where b.booster_id=?", (id,))
        return booster.fetchall()

    def insert_booster(self, booster):
        new_id = self.get_max_booster_id() + 1
        for card_id in booster:
            self.c.execute("insert into boosters values (:booster_id, :card_id)", (new_id, card_id))
        self.conn.commit()
        return new_id

    def get_n_boosters(self, n):
        total_boosters = self.get_max_booster_id()
        boosters = range(1, total_boosters + 1)
        random.shuffle(boosters)
        if (len(boosters) < n):
            for x in range(n - len(boosters)):
                boosters.append(random.choice(boosters))
        boosters = boosters[:n]
        out = defaultdict(lambda: 0)
        for x in range(n):
            result = self.get_booster(boosters[x])
            for card in result:
                out[card[0]] = out[card[0]] + 1

        return out

    def get_cards(self):
        return self.c.execute("select * from cards").fetchall()

    def open(self):
        self.conn = sqlite3.connect('mtg.db')
        self.c = self.conn.cursor()
    def close(self):
        self.conn.close()

