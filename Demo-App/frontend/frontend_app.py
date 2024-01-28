from flask import Flask, jsonify, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://backend-service:5000/version')
    data = response.json()
    return render_template_string(data['content'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
