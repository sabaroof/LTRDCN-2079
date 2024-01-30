from flask import Flask, jsonify, render_template_string
import requests
import os

app = Flask(__name__)

BACKEND_URL = 'http://' + os.getenv('BACKEND_URL') + ':' + os.getenv('BACKEND_PORT') + '/version'

@app.route('/')
def home():
    try:
        response = requests.get(BACKEND_URL, timeout=5)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error occurred: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"Something went wrong: {err}"
    else:
        data = response.json()
        return render_template_string(data['content'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
