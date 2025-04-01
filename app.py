from flask import Flask, request, jsonify
from flask_cors import CORS
from classifier import classify_expression
from ocr import extract_text_from_image
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/classify", methods=["POST"])
def classify():
    data = request.json
    expression = data.get("expression", "")
    if not expression:
        return jsonify({"error": "No expression provided"}), 400

    result = classify_expression(expression)
    return jsonify(result)

@app.route("/classify-image", methods=["POST"])
def classify_image():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    extracted_text = extract_text_from_image(file_path)
    result = classify_expression(extracted_text)
    return jsonify({"extracted_text": extracted_text, **result})

if __name__ == "__main__":
    app.run(debug=True)
# Note: Ensure that the OCR and classifier modules are in the same directory as this script.
# This Flask app provides two endpoints: