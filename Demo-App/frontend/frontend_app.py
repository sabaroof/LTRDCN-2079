from flask import Flask, jsonify, render_template_string, request, Response
import requests
import os
import logging
from werkzeug.wrappers import Response as ResponseBase

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

BACKEND_BASE_URL = 'http://' + os.getenv('BACKEND_URL') + ':' + os.getenv('BACKEND_PORT')

@app.route('/')
def home():
    try:
        response = requests.get(BACKEND_BASE_URL + '/version', timeout=5)
        response.raise_for_status()
    except (requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
            requests.exceptions.RequestException) as err:
        app.logger.error(f"Error occurred: {err}")
        return f"Error occurred: {err}"
    else:
        data = response.json()
        image_url = '/backend' + data['image_url']
        content = '<body style="background: url(' + image_url + '); background-size: cover; background-position: center; height: 100vh;">' + data['content'] + '</body>'


        return render_template_string(content)

@app.route('/backend/static/<path:path>')
def proxy(path):
    response = requests.get(BACKEND_BASE_URL + '/static/' + path)
    return ResponseBase(response.content, mimetype=response.headers['Content-Type'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
