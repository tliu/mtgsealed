from flask import Flask
from flask import request
from db import theDBMgr
import json
db = theDBMgr()
app = Flask(__name__)

@app.route("/boosters")
def get_boosters():
    num = request.args.get('count')
    print num
    print request.args
    if num is not None:
        print "ya"
        return json.dumps(db.get_n_boosters(num))

if __name__ == "__main__":
    app.run()
