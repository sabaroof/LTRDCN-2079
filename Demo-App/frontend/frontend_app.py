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
    except requests.exceptions.HTTPError as errh:
        app.logger.error(f"HTTP Error occurred: {errh}")
        return f"HTTP Error occurred: {errh}"
    except requests.exceptions.ConnectionError as errc:
        app.logger.error(f"Error Connecting: {errc}")
        return f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        app.logger.error(f"Timeout Error: {errt}")
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        app.logger.error(f"Something went wrong: {err}")
        return f"Something went wrong: {err}"
    else:
        data = response.json()
        return render_template_string(data['content'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
