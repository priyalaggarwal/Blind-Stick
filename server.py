import json
from watson_developer_cloud import VisualRecognitionV3

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def apicall():
    """
    API Call
    """
    try:
	visual_recognition = VisualRecognitionV3(version='2018-03-19',
    iam_api_key='pCUfPyi7eiXFPqQqYAXqbQvIYpipVEjZrOsEe6KSRJe1')
	with open('./1.png', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        parameters = json.dumps({
            'classifier_ids': ["food"]
        }))
	print(json.dumps(classes, indent=2))