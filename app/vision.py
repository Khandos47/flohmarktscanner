
import os
from google.cloud import vision
import io

def detect_labels(file):
    client = vision.ImageAnnotatorClient()
    content = file.read()
    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = [label.description for label in response.label_annotations]

    return labels
