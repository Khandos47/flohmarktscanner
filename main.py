from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import vision
import io
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'FlohmarktScanner API läuft!'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        content = file.read()
        client = vision.ImageAnnotatorClient()
        image = vision.Image(content=content)
        response = client.label_detection(image=image)
        labels = [label.description for label in response.label_annotations]

        estimated_price = "46,75 €"  # Dummy-Preis solange eBay API noch fehlt

        return jsonify({
            'estimated_price': {
                'keywords': labels,
                'estimated_price': estimated_price
            }
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
