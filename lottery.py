from flask import Flask, request,Response,url_for,render_template
import json
import jsonpath
import time
import os
import logging
import logger
from PIL import Image
import numpy as np
from werkzeug.utils import secure_filename
import uuid
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html') 
if __name__ == '__main__':
    app.run(port=777, debug=True,use_reloader=False,host='172.16.24.38')
