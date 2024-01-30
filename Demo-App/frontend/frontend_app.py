from flask import Flask, jsonify, render_template_string
import requests
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

BACKEND_URL = 'http://' + os.getenv('BACKEND_URL') + ':' + os.getenv('BACKEND_PORT') + '/version' + '/version'

@app.route('/')
def home():
    try:
        response = requests.get(BACKEND_URL, timeout=5)
        response.raise_for_status()
    except (requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
            requests.exceptions.RequestException) as err:
        app.logger.error(f"Error occurred: {err}")
        return f"Error occurred: {err}"
    else:
        data = response.json()
        image_url = BACKEND_BASE_URL + data['image_url']
        content = '<body style="background: url(' + image_url + ');">' + data['content'] + '</body>'
        return render_template_string(content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
