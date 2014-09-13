from flask import Flask
from db import theDBMgr
import json
db = theDBMgr()
app = Flask(__name__, static_url_path="")


# from https://blog.skyred.fi/articles/better-crossdomain-snippet-for-flask.html
# because i hate cors
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


@app.route("/boosters/count", methods=['GET'])
@crossdomain(origin='*')
def get_num_boosters():
    return json.dumps(db.count_boosters())

@app.route("/boosters", methods=['GET'])
@crossdomain(origin='*')
def get_boosters():
    num = int(request.args.get('count'))
    if num is not None:
        return json.dumps(db.get_n_boosters(num))

@app.route("/boosters/add", methods=['GET'])
@crossdomain(origin='*')
def insert_booster():
    cards = request.args.get('cards')
    cards =  map(lambda x:int(x), cards.split(','))
    id = db.insert_booster(cards)
    return json.dumps(id)

@app.route("/cards")
@crossdomain(origin='*')
def get_cards():
    return json.dumps(db.get_cards())

@app.route("/cards/name/<name>")
@crossdomain(origin='*')
def get_card_id_by_name(name):
    return json.dumps(db.get_card_id_by_name(name))

@app.route("/cards/id/<int:id>")
@crossdomain(origin='*')
def get_card_by_id(id):
    return json.dumps(db.get_card_by_id(id))

if __name__ == "__main__":
    app.run()
