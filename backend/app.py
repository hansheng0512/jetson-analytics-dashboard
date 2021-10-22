import flask
from flask import Flask, jsonify
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app, support_credentials=True)
image_list = []
validated_image_list = []


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/add-image", methods=["POST"])
def add_image():
    json_data = flask.request.json
    base64_image = json_data['base64_image']
    image_list.append({
        "uuid": str(uuid.uuid4()),
        "base64_image": base64_image,
        "valid": False
    })
    return jsonify({
        "message": "Image Appended"
    }), 200


@app.route("/retrieve-image", methods=["GET"])
def retrieve_image():
    if len(image_list) == 0:
        return jsonify({
            "message": "No Image"
        }), 400
    retrieved_item = image_list[len(image_list) - 1]
    return retrieved_item


@app.route("/valid-image", methods=["POST"])
def valid_image():
    json_data = flask.request.json
    selected_uuid = json_data['image_uuid']
    result = json_data['result']
    if len(image_list) == 0:
        return jsonify({
            "message": "Image not found"
        }), 400
    else:
        selected_meta = image_list[len(image_list) - 1]
        image_list.pop()
        validated_image_list.append({
            "uuid": selected_uuid,
            "base64_image": selected_meta["base64_image"],
            "valid": bool(result)
        })
        return jsonify({
            "message": f"Validated Image {selected_uuid}"
        }), 200


@app.route("/all-image", methods=["GET"])
def all_image():
    if len(image_list) == 0 and len(validated_image_list) == 0:
        return jsonify({
            "message": "No Image"
        }), 400
    return jsonify({
        "invalid": image_list,
        "valid": validated_image_list
    })


app.run(host='0.0.0.0', port=8080, debug=True)
