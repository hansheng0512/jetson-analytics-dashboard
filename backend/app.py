import flask
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)
image_list = []


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/add-image", methods=["POST"])
def add_image():
    json_data = flask.request.json
    base64_image = json_data['base64_image']
    return str(base64_image)


app.run(host='0.0.0.0', port=8080, debug=True)
