from flask import Flask, abort, request
import json
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> Hello my app.</h1>"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        # recive data from post request is JSON form
        recv = json.loads(request.data) 
        resp = "Pet data is a {0}, name is {1} and sex {2}".format(recv["pet"],recv["name"],recv["sex"])
        return  resp , 200
    else:
        abort(400)

if __name__ == "__main__":
    app.run(debug = True)
