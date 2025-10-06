from flask import Flask, request, jsonify, render_template
import os
import random

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Simulated DeepFake detection API
def CheckDeepFake(image_path):
    return random.choice([True, False])
# Ensure upload folder exists

@app.route('/')
def index():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', images=images)

@app.route('/check', methods=['POST'])
def check():
    image_name = request.json['image']
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
    result = CheckDeepFake(image_path)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
