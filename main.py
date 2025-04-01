
from flask import Flask, request, jsonify
from app.vision import detect_labels
from app.price import get_price_estimate

app = Flask(__name__)

@app.route("/")
def home():
    return "Flohmarktscanner API is running."

@app.route("/upload", methods=["POST"])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    labels = detect_labels(file)
    price = get_price_estimate(labels)

    return jsonify({
        "labels": labels,
        "estimated_price": price
    })

if __name__ == "__main__":
    app.run(debug=True)
