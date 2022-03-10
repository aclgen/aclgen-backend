from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"


@app.route("/test")
def test():
    return jsonify(list(range(5)))


if __name__ == '__main__':
    app.run()