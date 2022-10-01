import os
import sys
import tempfile
from flask import Flask
from flask import request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from werkzeug.utils import secure_filename

import torch

app = Flask(__name__)
FlaskJSON(app)

# or yolov5n - yolov5x6, custom
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
temp_path = tempfile.gettempdir()


@app.route('/process_image', methods=['POST'])
@as_json
def process_image():
    if request.method == 'POST':
        # Images
        # or file, Path, PIL, OpenCV, numpy, list
        img = request.files['image']
        filename = secure_filename(img.filename)
        img_path = os.path.join(temp_path, filename)
        img.save(img_path)
        results = model(img_path)
        #      xmin    ymin    xmax   ymax  confidence  class    name
        # 0  749.50   43.50  1148.0  704.5    0.874023      0  person
        # 2  114.75  195.75  1095.0  708.0    0.624512      0  person
        # 3  986.00  304.00  1028.0  420.0    0.286865     27     tie
        return results.pandas().xyxy[0].to_dict(orient='records')
    else:
        return "GET"
