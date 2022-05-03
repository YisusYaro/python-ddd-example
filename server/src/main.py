import os
import flask
from waitress import serve

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

def main():
    env = os.environ.get("ENV")
    if(env=="production"):
        serve(app, host="0.0.0.0", port=5000)
        return

    app.debug = True
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
