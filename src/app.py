#!/usr/bin/env python
from flask import Flask, render_template, Response, send_from_directory, jsonify, request

app = Flask(__name__)
image_num = 0
@app.route('/_add_numbers')
def add_numbers():
    global image_num
    image_num += 1
    image_num = image_num % 3
    return jsonify(result=image_num + 1)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
