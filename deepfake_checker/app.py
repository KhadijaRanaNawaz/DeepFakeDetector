
from flask import Flask, request, jsonify, render_template, url_for
import os
import json
import random


app = Flask(__name__)
CONFIG_FILE = 'config.json'

# Load configuration from JSON file
with open(CONFIG_FILE, 'r') as f:
    config_data = json.load(f)


# Simulated DeepFake detection API
def CheckDeepFake(image_path):
    return random.choice([True, False])




@app.route('/')
def index():
    return render_template('index.html', config=config_data)

@app.route('/check', methods=['POST'])
def check():
    image_name = request.json['image']
    result = CheckDeepFake(image_name)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

