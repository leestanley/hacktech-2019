import numpy as np
import pandas as pd
from flask import Flask
from flask import url_for, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8080, debug=True)
